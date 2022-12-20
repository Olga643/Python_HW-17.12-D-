# Реализуйте алгоритм перемешивания списка

import random


my_list = []
for i in range(10):
    my_list.append(random.randint(0, 100))
print(f'Оригинальный список {my_list}')

mix_list = my_list [:]    

for i in range(len(mix_list)):
        
        new_index = random.randint(0, len(mix_list) - 1)
       
        temp = mix_list[i]
        mix_list[i] = mix_list[new_index]
        mix_list[new_index] = temp
    
 

print(f'Перемешанный список {mix_list}')