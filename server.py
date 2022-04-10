import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1234
s.bind((Host,Port))
s.listen(5)
Comunication_socket,address = s.accept()
print(f"Connection to {address} established" )

while True:
    message=Comunication_socket.recv( 1024).decode('utf-8')
    print(f"Message from client : {message} ")
    msg_toSend= input("Enter a Message: ")
    Comunication_socket.send((msg_toSend).encode( 'utf-8'))
    
Comunication_socket.close()