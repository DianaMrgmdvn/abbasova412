#1
import random

def random_element(lst):
    return random.choice(lst)

a = [1, 23, 45, 6, 2566, 66]
result = random_element(a)
print(result)


#2
import os

def random_file(dir):
    files = os.listdir(dir)
    random_file = random.choice(files)
    return random_file


dir = "images/Math"
random_image = random_file(dir)
print(random_image)