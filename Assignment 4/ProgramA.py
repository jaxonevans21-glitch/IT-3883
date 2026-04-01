import socket

host = "127.0.0.1"
port = 40028

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while True:
    user = input("Type anything: ")

    if user.lower() == "quit":
        break

    sock.send(user.encode())

    data = sock.recv(1024)
    data = data.decode()

    print("From Program B:", data)

sock.close()
