"""
синхронизирует доступ к stdout: так как это общий глобальный объект, данные,
которые выводятся из потоков выполнения, могут перемешиваться, если не
синхронизировать операции
"""

import _thread as thread, time

def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        
        print('[%s] => %s' % (myId, i))

mutex = thread.allocate_lock()     # создать объект блокировки

for i in range(5):
    thread.start_new_thread(counter, (i, 5))

time.sleep(6)
print('Main thread exiting')    # задержать выход из программы