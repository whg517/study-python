import socket

HOST = '127.0.0.1'  # localhost
PORT = 60000  # 监听端口（非特权端口 > 1023）

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, address = s.accept()
    with conn:
        print('Connected by', address)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
