'''Задача 2.
1) Выберите любую папку на своем компьютере, имеющую вложенные директории.
2) Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи
функции "print_docs(directory)" 
'''

#include modul
import os

#initialization function
def print_docs(directory: str) -> None:

    #walk of directory and files
    data = list(os.walk(directory))
    
    #show result
    if len(data):
        for files in data:
            print()
            print(f'Folder {files[0]} contains:')
            print(f'Directories: {",".join([folder for folder in files[1]])}')
            print(f'Files: {", ".join([file for file in files[2]])}')
            print()
    else:
        print(f'\nPath not found\n')    

print_docs("HomeWork_10")    