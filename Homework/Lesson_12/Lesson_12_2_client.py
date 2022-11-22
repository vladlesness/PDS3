import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
message = input('Enter two numbers with a whitespace between them to do addition, subtraction and multiplication: ')
sock.send(bytes(message, encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data.decode('utf-8'))