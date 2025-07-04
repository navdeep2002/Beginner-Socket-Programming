import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    while True:
        msg = input("Enter message (or 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        client.sendall(msg.encode())
        data = client.recv(1024)
        print("Echo from server:", data.decode())
