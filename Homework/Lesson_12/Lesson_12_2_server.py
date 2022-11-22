import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running...')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    decoded_data = data.decode('utf-8')
    numbers = decoded_data.split()
    numbers = [float(i) for i in numbers]
    print(f'Number 1: {numbers[0]}', f'Number 2: {numbers[1]}', sep='\n')

    async def addition():
        print('Addition started')
        await asyncio.sleep(0)
        result = numbers[0] + numbers[1]
        print('Addition completed')
        return result

    async def subtraction():
        print('Subtraction started')
        await asyncio.sleep(0)
        result = numbers[0] - numbers[1]
        print('Subtraction completed')
        return result

    async def multiplication():
        print('Multiplication started')
        await asyncio.sleep(0)
        result = numbers[0] * numbers[1]
        print('Multiplication completed')
        return result

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(addition()), ioloop.create_task(subtraction()), ioloop.create_task(multiplication())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)

    message = ['Addition: ' + str(tasks[0].result()), 'Subtraction: ' + str(tasks[1].result()),
               'Multiplication: ' + str(tasks[2].result())]
    message = '\n'.join(message)
    conn.send(bytes(message, encoding='UTF-8'))
    conn.close()