"""
экземпляры класса Thread, сохраняющие информацию о состоянии и обладающие
методом run() для запуска потоков выполнения; в реализации используется
высокоуровневый и Java-подобный метод join класса Thread модуля threading
(вместо мьютексов и глобальных переменных), чтобы известить главный родительский
поток о завершении дочерних потоков;
"""
import threading

class Mythread(threading.Thread):               # подкласс класса Thread
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count                      # информация для каждого потока
        self.mutex = mutex                      # совместно используемые объекты
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))

stdoutmutex = threading.Lock()                  # то же, что и thread.allocate_lock()

threads = []

for i in range(9):
    thread = Mythread(i, 10, stdoutmutex)      # создать/запустить 10 потоков
    thread.start()                              # вызвать метод run потока
    threads.append(thread)

for thread in threads:
    thread.join()                               # ждать завершения потока

print('Main thread exiting.')