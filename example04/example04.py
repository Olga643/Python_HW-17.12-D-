#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

import random


number = int(input('Введите число: '))

my_list = []

for i in range(1, number + 1):
    my_list.append(random.randint(-number, number))

print(f'Оригинальный список {my_list}')

new_list = [my_list[3], my_list[1]]
print(new_list)
mult = 1

for i in new_list:
    mult = mult * i

print(mult)