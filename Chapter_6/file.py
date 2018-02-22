"""
Возвращает все имена файлов, соответствующие шаблону в дереве каталогов;
find() - функция-генератор, использующая функцию-генератор os.walk(),
возвращающая только имена файлов, соответствующие шаблону: чтобы получить весь
список результатов сразу, используйте функцию findlist();
"""
import os, fnmatch

# dirname = r'D:\REACT\react_redux\src\doc\pp'

def find(pattern, startdir=os.curdir):
    for (thisdir, dirnames, filenames) in os.walk(startdir):
       for name in dirnames + filenames:
           if fnmatch.fnmatch(name, pattern):
               fullpath = os.path.join(thisdir, name)
               yield fullpath

def findlist(pattern, startdir=os.curdir, dosort=False):
    matches = list(find(pattern, startdir))
    if dosort: matches.sort()
    return matches

if __name__ == '__main__':
    import sys
    # namepattern, startdir = sys.argv[1], sys.argv[2]
    namepattern, startdir = '*.py', '.\src'
    for name in find(namepattern, startdir): print(name)