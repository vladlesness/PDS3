import socket

messages = {'hi!': 'Hi there! How are you?',
            'how are you?': 'I am good, thanks. And you?',
            'what is the weather today?': 'Very nice and sunny!!!',
            'i want to eat something': 'Great, come on, let\'s eat out!'}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running...')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    decoded_data = data.decode('utf-8')
    print(decoded_data)
    message = messages[decoded_data.lower()] + '\n' + f'The amount of words in your phrase is {len(decoded_data.split())}'
    conn.send(bytes(message, encoding='UTF-8'))
    conn.close()