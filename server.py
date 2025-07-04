import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"server listening on {HOST}:{PORT}")

    conn, addr = server.accept()
    print(f"Connected by {addr}")
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("receiver:", data.decode())
            conn.sendall(data) #echo back



