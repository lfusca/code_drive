# 🚗 Code Drive — Controle de Rover via Rede

Projeto de controle remoto de um Rover (carrinho) via rede local (Wi-Fi/LAN), utilizando uma interface gráfica com `pygame` e um painel web com `streamlit`.

---

## 📁 Estrutura do Projeto

```
code_drive/
├── controle.py      # Cliente: captura teclas WASD e envia comandos via socket
├── menu.py          # Interface web (Streamlit) para abrir o controle
├── requirements.txt # Dependências do projeto
└── README.md
```

---

## 🚀 Passo a Passo — Como Instalar e Executar

### ✅ Passo 1 — Instale o Python

Certifique-se de ter o **Python 3.8 ou superior** instalado.

Verifique com:

```bash
python --version
```

Caso não tenha, baixe em: [python.org/downloads](https://www.python.org/downloads/)

> ⚠️ Durante a instalação no Windows, marque a opção **"Add Python to PATH"**.

---

### ✅ Passo 2 — Clone o Repositório

```bash
git clone https://github.com/lfusca/code_drive.git
```

Entre na pasta do projeto:

```bash
cd code_drive
```

---

### ✅ Passo 3 — Crie um Ambiente Virtual (recomendado)

```bash
python -m venv venv
```

Ative o ambiente:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

---

### ✅ Passo 4 — Instale as Dependências

Com o ambiente virtual ativado, instale tudo de uma vez usando o `requirements.txt`:

```bash
pip install -r requirements.txt
```

Isso instalará:
- `pygame-ce` — interface gráfica para captura de teclas
- `streamlit` — painel web para abrir o controle

---

### ✅ Passo 5 — Configure o IP do Rover

Abra o arquivo `controle.py` e edite a linha 11, substituindo o IP pelo endereço IP do Rover na sua rede local:

```python
# controle.py — linha 11
cliente.connect(("192.168.7.149", 5000))  # ← altere o IP aqui
```

> Para descobrir o IP do Rover, execute `ipconfig` (Windows) ou `ip a` (Linux) no dispositivo do Rover.

---

### ✅ Passo 6 — Execute o Projeto

**Opção A — Interface Web (recomendado):**

```bash
streamlit run menu.py
```

Acesse no navegador: `http://localhost:8501`

Clique em **"Abrir Controle"** para abrir a janela de controle.

---

**Opção B — Controle direto:**

```bash
python controle.py
```

---

## 🎮 Como Usar o Controle

Com a janela do controle aberta, use as teclas:

| Tecla | Ação |
|-------|------|
| `W` | Mover para frente |
| `S` | Mover para trás |
| `A` | Virar à esquerda |
| `D` | Virar à direita |
| *(soltar qualquer tecla)* | Parar |

> O controle envia comandos em tempo real via **socket TCP** para o servidor rodando no Rover.

---

## 🔌 Protocolo de Comunicação

| Comando enviado | Significado |
|-----------------|-------------|
| `b"w"` | Frente |
| `b"s"` | Ré |
| `b"a"` | Esquerda |
| `b"d"` | Direita |
| `b"p"` | Parar |

---

## ❗ Possíveis Erros

| Erro | Solução |
|------|---------|
| `ConnectionRefusedError` | O servidor do Rover não está rodando ou o IP está errado |
| `ModuleNotFoundError: pygame` | Execute `pip install -r requirements.txt` |
| `ModuleNotFoundError: streamlit` | Execute `pip install -r requirements.txt` |
| `python: command not found` | Python não está instalado ou não está no PATH |
