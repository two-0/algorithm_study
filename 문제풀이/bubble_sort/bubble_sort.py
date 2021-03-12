import random


# 버블 정렬 파이썬 구현


def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - 2):
            if data[index2 + 1] < data[index2]:
                data[index2],data[index2 + 1] = data[index2 + 1],data[index2]
                swap = True
    return data


data_list = random.sample(range(100), 50)

print(bubble_sort(data_list))
