" оптимизация за счет непосредственного изменения списка в памяти"

class error(Exception): pass # при импортировании: локальное исключение

class Stack:
    def __init__(self, start=[]): # self - объект экземпляра
        self.stack = [] # start - любая последовательность: stack...
        for x in start: self.push(x)
    
    def push(self, obj): # методы: подобно модулю + self
        self.stack.append(obj) # вершина в конце списка
    
    def pop(self):
        if not self.stack: raise error('underflow')
        return self.stack.pop() # подобно извлечению и удалению stack[-1]
    
    def top(self):
        if not self.stack: raise error('underflow')
        return self.stack[-1]
    
    def empty(self):
        return not self.stack # instance.empty()
    
    def __len__(self):
        return len(self.stack) # len(instance), not instance
    
    def __getitem__(self, offset):
        return self.stack[offset] # instance[offset], in, for
    
    def __repr__(self):
        return '[Stack:%s]' % self.stack
