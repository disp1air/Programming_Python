"оптимизация за счет использования дерева кортежей"

class Stack:
    def __init__(self, start=[]):
        self.stack = None
        for i in range(-len(start), 0):
            self.push(start[-i - 1])            # втолкнуть в обратном порядке

    def push(self, node):
        self.stack = node, self.stack

    def pop(self):
        node, self.stack = self.stack
        return node

    def empty(self):
        return not self.stack

    def __len__(self):
        len, tree = 0, self.stack
        while tree:
            len, tree = len+1, tree[1]           # обойти правые поддеревья
        return len

    def __getitem__(self, index):                # для операций: x[i], in, for
        len, tree = 0, self.stack
        while len < index and tree:              # обход/подсчет узлов
            len, tree = len+1, tree[1]
        if tree:
            return tree[0]                       # IndexError, при выходе за границы
        else:
            raise IndexError()                   # остановка для 'in' и 'for'
        
    def __repr__(self):
        return '[FastStack:' + repr(self.stack) + ']'
