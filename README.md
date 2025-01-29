# Diferentes Tipos de Políticas de Substituição de Cache

## FIFO (First In, First Out)
**Função:** Remove o item que entrou primeiro no cache quando o limite de capacidade é atingido.

**Vantagem:** Simples de implementar e mantém uma ordem clara de substituição.

**Desvantagem:** Não considera a frequência de acesso ou a relevância dos dados. Pode remover itens populares ou frequentemente acessados.

**Exemplo prático:** Uma fila em que os primeiros a entrar são os primeiros a sair, como em um restaurante de fast food.

---

## LRU (Least Recently Used)
**Função:** Remove o item menos recentemente acessado.

**Vantagem:** Baseia-se no comportamento de acesso recente, garantindo que itens mais usados recentemente permaneçam no cache.

**Desvantagem:** Pode ser mais complexo de implementar, já que é necessário manter uma estrutura de dados para rastrear a ordem de uso.

**Exemplo prático:** Quando você volta a um site frequentemente acessado, ele carrega mais rápido porque os dados são mantidos no cache.

---

## LFU (Least Frequently Used)
**Função:** Remove o item que foi acessado menos vezes.

**Vantagem:** Dá prioridade aos itens mais usados ao longo do tempo.

**Desvantagem:** Pode penalizar itens que foram acessados muito no passado, mas que não são mais necessários atualmente. Também pode ser mais complexo devido ao rastreamento da frequência.

**Exemplo prático:** Um aplicativo de música mantém no cache as músicas mais tocadas para evitar baixar novamente.

---

# Configurando e Usando a Simulação de Cache com Flask

Este tutorial irá guiar você para configurar e usar a simulação de cache com Flask no seu computador, usando o VS Code no Windows.

## Passo 1: Preparando o Ambiente

### Instalar o Python:
1. Acesse o site oficial do Python: [Python Downloads](https://www.python.org/downloads/)
2. Baixe a versão mais recente do Python.
3. Durante a instalação, marque a opção **"Add Python to PATH"** e clique em **"Install Now"**.

### Instalar o Visual Studio Code (VS Code):
1. Acesse o site oficial do VS Code: [VS Code Downloads](https://code.visualstudio.com/Download)
2. Baixe e instale o VS Code.

### Instalar o Flask:
Abra o **Prompt de Comando** ou **PowerShell** e digite:
```sh
pip install flask
```

---

## Passo 2: Preparando os Arquivos do Sistema

### Criando os Arquivos:
1. Crie uma nova pasta em seu computador para o projeto.
2. Dentro dessa pasta, crie dois arquivos principais:
   - **app.py**: Contém o código da simulação de cache.
   - **templates/index.html**: Interface do usuário.

### Adicionando os Códigos:
- Copie o código da API Flask para o arquivo **app.py**.
- Copie o código da interface HTML para o arquivo **index.html**, dentro da pasta **templates**.

---

## Passo 3: Rodando o Sistema

### Abrir o VS Code:
1. No VS Code, clique em **File > Open Folder** e selecione a pasta do projeto.

### Abrir o Terminal no VS Code:
1. No menu superior, clique em **Terminal > New Terminal**.

### Rodar o Flask:
Digite o comando:
```sh
python app.py
```

O Flask iniciará e você verá algo como:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Isso significa que o sistema está rodando localmente.

---

## Passo 4: Usando a Simulação de Cache

### Abrir no Navegador:
Digite na barra de endereços:
```
http://127.0.0.1:5000/
```

### Testando a Simulação:
1. **Acessar um Animal**: Digite um número de 1 a 20 e clique em **Acessar**.
2. **Alterar a Política de Substituição**: Escolha entre FIFO, LRU ou LFU e clique em **Alterar Política**.
3. **Verificar o Cache**: Veja os animais armazenados e as estatísticas de acertos e erros.

---

## Passo 5: Parar o Servidor
Para parar o servidor Flask, no terminal, pressione **CTRL+C**.

---

## Dicas Finais
- **Alterando Animais**: Edite a lista de animais no **app.py**.
- **Mudando o Estilo**: Edite o **index.html** para personalizar a interface.

---

## Imagens

![Imagem 1]( Captura de Tela (499).png)

![Imagem 2](Captura de Tela (501).png)

