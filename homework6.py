def grouped(array, num=3):
    array1 = [array[i:i+num] for i in range(0, len(array), num)]
    return array1

array = [
    "Курс 1",
    "Курс 2",
    "Курс 3",
    "Курс 4",
    "Курс 5",
    "Курс 6",
    "Курс 7",
    "Курс 8",
    "Курс 9",
    "Курс 10",
]

array2 = grouped(array, 2)
for sublist in array2:
    print(sublist)