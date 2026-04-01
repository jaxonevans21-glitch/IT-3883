import socket

host = "127.0.0.1"
port = 40028

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host, port))
serv.listen(1)

print("Waiting for Program A")

c, addr = serv.accept()
print("Connected by:", addr)

while True:
    data = c.recv(1024)
    data = data.decode()

    if not data:
        break

    user = data.upper()

    print("Uppercase string:", user)

    c.send(user.encode())

c.close()
serv.close()
