"сравнение производительности альтернативных реализаций стека"

import stack2 # стек на основе списка: [x]+y
import stack3 # стек на основе дерева кортежей: (x,y)
import stack4 # стек, выполняющий модификацию списка в памяти: y.append(x)
import timer # вспомогательная функция хронометража

rept = 200
from sys import argv
pushes, pops, items = (int(arg) for arg in argv[1:])

def stackops(stackClass):
    x = stackClass('spam') # создать объект стека
    for i in range(pushes): x.push(i) # применить его методы
    for i in range(items): t = x[i] # 3.X: range - генератор
    for i in range(pops): x.pop()
                                    # или mod = __import__(n)

for mod in (stack2, stack3, stack4): # rept*(push+pop+ix)
    print('%s:' % mod.__name__, end=' ')
    print(timer.test(rept, stackops, getattr(mod, 'Stack')))