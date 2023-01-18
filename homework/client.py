import os
import socket
import struct


def send_file(sck: socket.socket, filename):
    # Получение размера файла.
    filesize = os.path.getsize(filename)
    # В первую очередь сообщим серверу,
    # сколько байт будет отправлено.
    sck.sendall(struct.pack("<Q", filesize))
    # Отправка файла блоками по 1024 байта.
    with open(filename, "rb") as f:
        while read_bytes := f.read(1024):
            sck.sendall(read_bytes)


with socket.create_connection(("localhost", 6190)) as conn:
    print("Подключение к серверу.")
    print("Передача файла...")
    send_file(conn, "1.json")
    print("Отправлено.")
print("Соединение закрыто.")
