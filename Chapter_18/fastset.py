"оптимизация за счет применения линейного алгоритма сканирования по словарям"

import set

class Set(set.Set):
    def __init__(self, value=[]):
        self.data = {}
        self.concat(value)

    def intersect(self, other):
        res = {}
        for x in other:
            if x in self.data:
                res[x] = None
        return Set(res.keys())

    def union(self, other):
        res = {}
        for x in other:
            res[x] = None
        for x in self.data.keys():
            res[x] = None
        return Set(res.keys())

    def concat(self, value):
        for x in value: self.data[x] = None

    # inherit and, or, len
    def __getitem__(self, ix):
        return list(self.data.keys())[ix] # 3.X: вызов list() необходим
    
    def __repr__(self):
        return '<Set:%r>' % list(self.data.keys()) # то же самое
    