# 1. функция выбора случайного элемента из списка
import random

def random_element(lst):
    return random.choice(lst)

a=[1, 23, 45, 6, 2566, 66]
result = random_elemant(a)
print('Element:', result)

# 2. получить спислк файлов в директории и выбрать случайный  файл

import os

folder = 'images\Gauss'
name = []

for files in os.scandir(folder):
    if files.is_file():
        name.append(files.name)

random = random.choice(name)
print('File:', random)