# Beginner Socket Programming

A simple Python project demonstrating basic TCP client-server communication using the built-in `socket` module.

## 💡 Features

- TCP communication between a client and server
- Server handles messages and can reply interactively
- Client connects and exchanges messages with the server

## 📁 Files

| File       | Description                      |
|------------|----------------------------------|
| `server.py` | Accepts a connection and replies |
| `client.py` | Connects to the server and sends messages |

## ▶️ How to Run

1. Open **two terminal tabs**:
   - In one, run the server:
     ```bash
     python3 server.py
     ```
   - In the other, run the client:
     ```bash
     python3 client.py
     ```

2. Type messages from the client and receive responses from the server.

3. Type `exit` to close the connection.

## ✅ Requirements

- Python 3.9+ 

## 📜 License

This project is licensed under the MIT License.
