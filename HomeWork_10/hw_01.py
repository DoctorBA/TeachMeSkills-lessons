'''Задача 1.
1) Реализовать функцию longest_words, которая выводит слово, содержимого файла
"article.txt", имеющее максимальную длину (или список слов, если таковых несколько). 
'''
#include modul
from typing import Union

#initialization function
def longest_words(file: str) -> Union[str, list]:

    #read file
    with open(file, 'r', encoding='utf-8') as file:
        file = file.read()

    #maximum word length in the list
    max_len_word =  max([len(len_word) for len_word in file.split()])

    #maximum word or words length
    result = [word for word in file.split() if len(word) == max_len_word]
    return ''.join(result) if len(result) < 2 else result

#output result
print(longest_words('HomeWork_10/article.txt'))    