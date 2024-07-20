import asyncio

HOST = '127.0.0.1'
PORT = 65432

async def chat_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)

    while True:
        message = input('Ответьте на сообщение: ')
        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(1024)
        if not data:
            break
        print(f'Получено: {data.decode()}')

    writer.close()
    await writer.wait_closed()

asyncio.run(chat_client())
