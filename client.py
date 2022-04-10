import socket

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1234
Client.connect((Host,Port))

while True:
    msg_to_Send = input("Please enter a Message: ")
    Client.send((msg_to_Send).encode('utf-8'))
    message = Client.recv(1024).decode('utf-8')
    print(f"Message from the server : {message}")