"""всегда выводит 200 - благодаря синхронизации доступа к глобальному ресурсу"""
import threading, time
count = 0

def adder(addlock):             # совместно используемый объект блокировки
    global count
    with addlock:                # блокировка приобретается/освобождается автоматически
        count = count + 1
    time.sleep(0.5)
    with addlock:               # в конкретный момент времени только 1 поток может
        count = count + 1       # изменить значение переменной

addlock = threading.Lock()
threads = []

for i in range(100):
    thread = threading.Thread(target=adder, args=(addlock, ))
    thread.start()
    threads.append(thread)

for thread in threads: thread.join()
print(count)