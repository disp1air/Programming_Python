"""
На стороне сервера: открыть сокет TCP/IP с указанным номером порта,
ждать появления сообщения от клиента, отправить это же сообщение обратно;
это реализация простого одноступенчатого диалога вида запрос/ответ,
но сценарий выполняет бесконечный цикл и пока он действует, способен
обслужить множество клиентов; клиент может выполняться как на удаленном,
так и на локальном компьютере, если в качестве имени сервера
будет использовать 'localhost' 
"""

from socket import *

myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

while True:
    connection, address = sockobj.accept()

    print('Server connected by', address)

    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(b'Echo=>' + data)
    connection.close()