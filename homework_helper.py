import os
import shutil

from helper import make_dirs

#1. проверка существует ли директория
    #1.1. если существует, то ничего не делать
    #1.2. если не существует, то создать
#2. ищем файлы, которые будем переносить
    #2.1. ищем файлы с форматом .txt
    #2.2. ищем файлы, название которых содержит слово "homework"  
#3. перемещение
    #3.1. выбор файла
    #3.2. копирование
    #3.3. переходим в директорию
    #3.4. добавляем файл
        #3.4.1. проверка исходного и скопированного файлов
    #3.5. удаляем исходный файл

#1
homework_dir = 'homeworks'
make_dirs(homework_dir)

#2
files = os.listdir()
new_files_list = []

for file in files:
#2.1 и 2.2
    if '.txt' in file and 'homework' in file:
        new_files_list.append(file)

# print(new_files_list)
        
for file in new_files_list:
    shutil.copy(file, f'{homework_dir}/{file}')
    
for file in new_files_list:
    os.remove(file)