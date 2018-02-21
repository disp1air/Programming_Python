"класс стека, позволяющий создавать множество экземпляров"

class error(Exception): pass

class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for x in start: self.push(x)
        self.reverse()                      # переупорядочивает операции push
                                            # в обратном порядке
    def push(self, obj):
        self.stack = [obj] + self.stack

    def pop(self):
        if not self.stack:
            raise error('stack underflow')
        top, *stack = self.stack                     # удалить элемент в начале
        return top

    def top(self):
        if not self.stack:
            raise error('stack underflow')
        return self.stack[0]

    def empty(self): return not self.stack

    # методы перегрузки операторов
    def __repr__(self):
        return '[Stack:%s]' % self.stack            # print, repr(),..

    def __eq__(self, other):
        return self.stack == other.stack # '==', '!='?

    def __len__(self):
        return len(self.stack) # len(instance), not instance
    
    def __add__(self, other):
        return Stack(self.stack + other.stack) 
    
    def __mul__(self, reps):
        return Stack(self.stack * reps)
    
    def __getitem__(self, offset):
        return self.stack[offset] 
    
    def __getattr__(self, name):
        return getattr(self.stack, name)
    