# 🚗 Code Drive — Controle de Rover via Rede

Projeto de controle remoto de um Rover (carrinho) via rede local (Wi-Fi/LAN), utilizando uma interface gráfica com `pygame` e um painel web com `streamlit`.

---

## 📁 Estrutura do Projeto

```
code_drive/
├── controle.py   # Cliente: captura teclas WASD e envia comandos via socket
├── menu.py       # Interface web (Streamlit) para abrir o controle
└── README.md
```

---

## ⚙️ Pré-requisitos

- **Python 3.8+** instalado
- **pip** para instalar as dependências

### Instalar dependências

```bash
pip install pygame streamlit
```

---

## 🌐 Configuração de Rede

O arquivo `controle.py` se conecta a um servidor (o Rover) via socket TCP.

> **Importante:** antes de executar, edite a linha abaixo em `controle.py` e substitua o IP pelo endereço IP do Rover na sua rede local:

```python
# controle.py — linha 11
cliente.connect(("192.168.7.149", 5000))  # ← altere o IP aqui
```

Para descobrir o IP do Rover, execute `ipconfig` (Windows) ou `ip a` (Linux) no dispositivo do Rover.

---

## ▶️ Como Executar

### Opção 1 — Interface Web (recomendado)

Inicia um painel no navegador com um botão para abrir a janela de controle:

```bash
streamlit run menu.py
```

Acesse no navegador: `http://localhost:8501`

Clique em **"Abrir Controle"** para abrir a janela de controle.

---

### Opção 2 — Controle direto

Abre a janela de controle diretamente, sem passar pelo menu:

```bash
python controle.py
```

---

## 🎮 Como Usar o Controle

Com a janela do controle aberta, use as teclas:

| Tecla | Ação        |
|-------|-------------|
| `W`   | Mover para frente |
| `S`   | Mover para trás   |
| `A`   | Virar à esquerda  |
| `D`   | Virar à direita   |
| *(soltar qualquer tecla)* | Parar (`p`) |

> O controle envia comandos em tempo real via **socket TCP** para o servidor rodando no Rover.

---

## 🔌 Protocolo de Comunicação

| Comando enviado | Significado |
|-----------------|-------------|
| `b"w"`          | Frente      |
| `b"s"`          | Ré          |
| `b"a"`          | Esquerda    |
| `b"d"`          | Direita     |
| `b"p"`          | Parar       |

---

## ❗ Possíveis Erros

| Erro | Solução |
|------|---------|
| `ConnectionRefusedError` | O servidor do Rover não está rodando ou o IP está errado |
| `ModuleNotFoundError: pygame` | Execute `pip install pygame` |
| `ModuleNotFoundError: streamlit` | Execute `pip install streamlit` |
