---
# 📢 WebChat – Chat em tempo real com Django Channels e WebSockets

## 📌 Sobre o Projeto

#### O **WebChat** é uma aplicação simples que permite conversas em tempo real em salas de chat usando **Django Channels** e **WebSockets**.

#### Utiliza o **Redis** como backend para gerenciamento do canal de mensagens, e o servidor **Daphne** para suportar ASGI e WebSockets.

---

## 🔎 Como Funciona

1.  🖥️ O servidor Daphne é iniciado para suportar conexões WebSocket.
2.  🌐 O usuário acessa uma sala de chat específica pela URL, ex: `/chat/sala1/`.
3.  📩 As mensagens enviadas são transmitidas via WebSocket para o servidor.
4.  🔄 O servidor utiliza Redis para distribuir as mensagens para todos os clientes conectados na mesma sala.
5.  💬 As mensagens aparecem instantaneamente para todos os participantes da sala.

---

## 🧰 Tecnologias Utilizadas

- **Python + Django** – framework backend
- **Django Channels** – suporte para WebSockets e comunicação assíncrona
- **Redis** – servidor para gerenciar o channel layer
- **Daphne** – servidor ASGI para rodar o projeto com suporte WebSocket
- **JavaScript** – código frontend para comunicação WebSocket
- **HTML/CSS** – interface do chat

---

## 🚀 Como Utilizar

### ✅ Pré-requisitos:

- Python 3.8+
- Redis instalado e rodando (local ou remoto)
- Git instalado

---

### 🛠️ Passo a Passo

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/henrique151/WebChat-Simples.git
    cd WebChat-Simples
    ```

2.  **Crie e ative um ambiente virtual** (opcional, mas recomendado):

    ```bash
    python -m venv venv

    # Windows
    venv\Scripts\activate

    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Redis no arquivo `settings.py`:**

    ```python
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("127.0.0.1", 6379)],
            },
        },
    }
    ```

5.  **Execute as migrações do Django:**

    ```bash
    python manage.py migrate
    ```

6.  **Inicie o servidor Daphne** (substitua `webchat` pelo nome do seu projeto Django):

    ```bash
    daphne -p 8000 webchat.asgi:application
    ```

7.  **Acesse o chat no navegador:**

    - Abra `http://127.0.0.1:8000/chat/sala1/` para entrar na sala "sala1".
    - Abra `http://127.0.0.1:8000/chat/outrasala/` para entrar em uma sala diferente.

---

## 💬 Exemplo de Uso

Ao acessar uma sala, você verá a interface do chat. Digite seu nome, sua mensagem e pressione "Enviar". A mensagem aparecerá instantaneamente para todos os participantes da mesma sala.

```
[Sala: sala1]

Henrique: Olá, pessoal! Bem-vindos ao WebChat!
Maria: Oi, Henrique! Funcionando perfeitamente.
João: Incrível essa comunicação em tempo real!
```

---

## 🤝 Contribuições

Sinta-se livre para abrir issues ou pull requests. Melhorias são sempre bem-vindas\! 💬

---

## 📄 Licença

Este projeto está sob a licença [MIT](https://www.google.com/search?q=LICENSE).

---

## 📫 Contato

Para dúvidas, sugestões ou parcerias, entre em contato: `henriqueporto949@gmail.com`

---
