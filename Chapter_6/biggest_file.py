"""
Отыскивает наибольший файл с исходным программным кодом на языке Python
в единственном каталоге.
"""
import os, sys, glob, pprint

dirname = r'***'          # path to the directory
file_extension = '*.js'

list_of_files = glob.glob(dirname + os.sep + file_extension)
all_sizes = []

for filename in list_of_files:
    filesize = os.path.getsize(filename)
    all_sizes.append((filesize, filename))

all_sizes.sort()
pprint.pprint(all_sizes)
pprint.pprint(all_sizes[-1])

