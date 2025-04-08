import asyncio

import websockets

async def client():
    # адрес сервера
    uri = "ws://localhost:8765"
    # с помощью контекстного менеджера устанавливаем соединение с сервером
    async with websockets.connect(uri) as websocket:
        # сообщение, которое отправить клиент
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        # отправляем сообщение
        await websocket.send(message)

         # получаем ответ от сервера
        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")

asyncio.run(client())