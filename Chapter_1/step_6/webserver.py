import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'   # место где находятся файлы html
port = 80

os.chdir(webdir)   # перейти в корневой каталог html
srvraddr = ("", port)   # имя хоста и номер порта
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()   # запустить как бесконечный фоновый процесс