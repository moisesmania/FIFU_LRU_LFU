from flask import Flask, render_template, request, jsonify
from collections import deque, Counter

app = Flask(__name__)

# Classe de Cache com suporte para FIFO, LRU, LFU
class Cache:
    def __init__(self, size, policy):
        self.size = size
        self.policy = policy
        self.cache = []
        self.freq = Counter()  # Para LFU
        self.use_order = deque()  # Para LRU e FIFO

    def access(self, item):
        if item in self.cache:
            self.freq[item] += 1
            if self.policy == "LRU":
                self.use_order.remove(item)
                self.use_order.append(item)
            return True  # Cache HIT
        else:
            if len(self.cache) >= self.size:
                self.evict()
            self.cache.append(item)
            self.freq[item] += 1
            self.use_order.append(item)
            return False  # Cache MISS

    def evict(self):
        if self.policy == "FIFO":
            evicted = self.cache.pop(0)
            self.use_order.popleft()
        elif self.policy == "LRU":
            evicted = self.use_order.popleft()
            self.cache.remove(evicted)
        elif self.policy == "LFU":
            least_used = min(self.freq, key=self.freq.get)
            self.cache.remove(least_used)
            self.freq.pop(least_used)
            self.use_order.remove(least_used)

    def update_policy(self, policy):
        """ Atualiza a política do cache sem limpar o conteúdo. """
        self.policy = policy

# Inicializa o Cache e variáveis globais
cache = Cache(size=5, policy="FIFO")
hits = 0
misses = 0
current_item = None
forest_animals = [
    "Leão", "Tigre", "Elefante", "Urso", "Lobo", "Cervo", "Raposa", "Macaco",
    "Coelho", "Girafa", "Zebra", "Chita", "Leopardo", "Falcão", "Coruja", "Águia",
    "Búfalo", "Rinoceronte", "Canguru", "Coala"
]
animal_dict = {i + 1: animal for i, animal in enumerate(forest_animals)}  # Ajusta IDs de 1 a 20

@app.route('/')
def index():
    return render_template('index.html',
                           cache=cache.cache,
                           animals=animal_dict,
                           hits=hits,
                           misses=misses,
                           policy=cache.policy,
                           current_item=current_item)

@app.route('/access', methods=['POST'])
def access():
    global hits, misses, current_item
    try:
        data = int(request.form['animal_id'])
        if data < 1 or data > 20:  # Verifica ID entre 1 e 20
            return jsonify({"error": "Por favor, insira um número entre 1 e 20."}), 400
    except ValueError:
        return jsonify({"error": "Entrada inválida."}), 400

    animal = animal_dict.get(data)
    if animal is None:
        return jsonify({"error": "Animal não encontrado."}), 404

    current_item = animal
    if cache.access(animal):
        hits += 1
        result = "Cache HIT"
    else:
        misses += 1
        result = "Cache MISS"

    return jsonify({
        "result": result,
        "cache": cache.cache,
        "hits": hits,
        "misses": misses
    })

@app.route('/policy', methods=['POST'])
def change_policy():
    global cache, hits, misses, current_item
    policy = request.form['policy']
    if policy not in ["FIFO", "LRU", "LFU"]:
        return jsonify({"error": "Política inválida."}), 400

    # Atualiza a política sem limpar o cache atual
    cache.update_policy(policy)
    
    # Não reiniciar as estatísticas de hits e misses aqui, para manter o histórico
    return jsonify({
        "message": "Política alterada para " + policy,
        "cache": cache.cache,
        "hits": hits,
        "misses": misses
    })

if __name__ == "__main__":
    app.run(debug=True)
