import asyncio

HOST = '127.0.0.1'
PORT = 65432


async def handle_client(reader, writer):
    print('New connection')
    while True:
        data = await reader.read(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received {message!r}")

        response = input('Enter your response: ')
        writer.write(response.encode())
        await writer.drain()

    print('Connection closed')
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print(f'Serving on {HOST}:{PORT}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
