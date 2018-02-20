"""
На стороне клиента: использует сокеты для передачи данных серверу
и выводит ответ сервера на каждую строку сообщения; 'localhost' означает,
что сервер выполняется на одном компьютере с клиентом, что позволяет
тестировать клиента и сервер на одном компьютере; для тестирования
через Интернет запустите сервер на удаленном компьютере и установите
serverHost или argv[1] равными доменному имени компьютера или его IP-адресу;
сокеты Python являются переносимым интерфейсом к сокетам BSD,
с методами объектов для стандартных функций сокетов, доступных
в системной библиотеке C;
"""

import sys
from socket import *

serverHost = 'localhost'
serverPort = 50007

message = [b'Hello network world']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print('client received:', data)

sockobj.close()