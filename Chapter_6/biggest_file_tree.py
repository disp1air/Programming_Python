"""
Отыскивает наибольший файл с исходным программным кодом в дереве каталогов.
"""
import os, sys, pprint

dirname = r'***'           # path to the directory
file_extension = '.js'

all_files = []

def lister(root_dir):
    for(thisdir, dirnames, filenames) in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                fullname = os.path.join(thisdir, filename)
                filesize = os.stat(fullname).st_size
                all_files.append((filesize, fullname))

    all_files.sort()
    pprint.pprint(all_files)
    pprint.pprint(all_files[-1])

lister(dirname)