"универсальный инструмент хронометража"

def test(reps, func, *args):
    import time
    start = time.clock()            # текущее время CPU в секундах
    for i in range(reps):           # вызвать функцию reps раз
        func(*args)                 # отбросить возвращаемое значение
    return time.clock() - start     # время конца - время начала