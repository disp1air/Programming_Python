"Модуль реализации стека"

stack = []

class error(Exception): pass        # локальные исключения, stack1.error

def push(obj):
    global stack
    stack = [obj] + stack

def pop():
    global stack
    if not stack:
        raise error('stack underflow')
    top, *stack = stack                     # удалить элемент в начале
    return top

def top():
    if not stack:
        raise error('stack underflow')
    return stack[0]

def empty(): return not stack               # стек пуст?
def member(obj): return obj in stack        # элемент имеется в стеке?
def item(offset): return stack[offset]      # элемент стека по индексу
def length(): return len(stack)             # количество элементов на стеке
def dump(): print('<Stack:%s>' % stack)