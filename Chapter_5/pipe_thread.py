# анонимные каналы и потоки выполнения вместо процессов;

import os, time, threading

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                     # заставить родителя подождать
        msg = ('Spam %03d' % zzz).encode()  # каналы - двоичные данные
        os.write(pipeout, msg)              # отправить данные родителю
        zzz = (zzz + 1) % 5

def parent(pipein):
    while True:
        line = os.read(pipein, 32)
        print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)
