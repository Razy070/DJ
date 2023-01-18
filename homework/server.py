import socket
import struct


def receive_file_size(sck: socket.socket):
    # Эта функция обеспечивает получение байтов,
    # указывающих на размер отправляемого файла,
    # который кодируется клиентом с помощью
    # struct.pack(), функции, которая генерирует
    # последовательность байтов, представляющих размер файла.
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()
    while received_bytes < expected_bytes:
        chunk = sck.recv(expected_bytes - received_bytes)
        stream += chunk
        received_bytes += len(chunk)
    filesize = struct.unpack(fmt, stream)[0]
    return filesize


def receive_file(sck: socket.socket, filename):
    # Сначала считываем из сокета количество
    # байтов, которые будут получены из файла.
    filesize = receive_file_size(sck)
    # Открываем новый файл для сохранения
    # полученных данных.
    with open(filename, "wb") as f:
        received_bytes = 0
        # Получаем данные из файла блоками по
        # 1024 байта до объема
        # общего количество байт, сообщенных клиентом.
        while received_bytes < filesize:
            chunk = sck.recv(1024)
            if chunk:
                f.write(chunk)
                received_bytes += len(chunk)


with socket.create_server(("localhost", 6190)) as server:
    print("Ожидание клиента...")
    conn, address = server.accept()
    print(f"{address[0]}:{address[1]} подключен.")
    print("Получаем файл...")
    receive_file(conn, "1.json")
    print("Файл получен.")
print("Соединение закрыто.")
