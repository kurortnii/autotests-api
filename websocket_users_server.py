import asyncio

import websockets
from websockets import ServerConnection

# обработчик входящих сообщений
async  def echo (websocket: websockets.ServerConnection):
    # асинхронно обрабатываем входящие сообщения
    async for message in websocket:
        # логируем полученное сообщение
        print(f"Получено сообщение от пользователя: {message}")

        # формируем ответное сообщение
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)


# запуск вебсокет-сервера на порту 8765
async def main():
    # запускаем сервер
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket сервер запущен на ws://localhost:8765")

    # ожидаем закрытия сервера (обычно он работает вечно)
    await server.wait_closed()

asyncio.run(main())