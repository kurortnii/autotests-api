# импортируем модуль socket для работы с сетевыми соединениями
import socket

# определяем функцию, которая запускает сервер
def server():
    # создаем TCP-сокет. AF_INET -- IPv4, SOCK_STREAM -- тип сокета -- TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # привязываем сокет к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # начинаем слушать входящие подключения (максимум 10 в очереди)
    server_socket.listen(10)
    print("Сервер запущен и ждет подключений на localhost:12345")

    # создаем пустой список, где будем хранить сообщения
    messages = []

    # запускаем бесконечный цикл, чтобы сервер всегда ждал новые подключения
    while True:
        # принимаем соединение от клиента и логгируем его
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # получаем данные от клиента, логгируем отправку сообщения клиентом и добавляем в список
        # recv(1024) -- ждет и получает данные от клиента, макс 1014 байта
        # .decode() -- преобразует байты в строку (обычно в UTF-8)
        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
        messages.append(data)

        # отправляем ответ клиенту
        client_socket.send('\n'.join(messages).encode())

        # закрываем соединение с клиентом
        client_socket.close()

if __name__ == '__main__':
    server()