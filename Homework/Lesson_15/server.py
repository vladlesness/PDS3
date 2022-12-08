import socket
import logging

logger = logging.getLogger('Server')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('server_logs.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

messages = {'hi!': 'Hi there! How are you?',
            'how are you?': 'I am good, thanks. And you?',
            'what is the weather today?': 'Very nice and sunny!!!',
            'i want to eat something': 'Great, come on, let\'s eat out!'}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running...')
logger.info('Server started')

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    logger.info('connected: ' + str(addr))
    try:
        data = conn.recv(1024)
    except ConnectionResetError:
        logger.error('ConnectionResetError', exc_info=True)
        continue
    decoded_data = data.decode('utf-8')
    print(decoded_data)
    try:
        message = messages[decoded_data.lower()] + '\n' + f'The amount of words in your phrase is {len(decoded_data.split())}'
    except KeyError:
        logger.warning('KeyError', exc_info=True)
        conn.send(bytes('Value not found', encoding='UTF-8'))
        conn.close()
    except Exception:
        logger.warning('Exception', exc_info=True)
        conn.send(bytes('Error occurred', encoding='UTF-8'))
        conn.close()
    else:
        conn.send(bytes(message, encoding='UTF-8'))
        conn.close()