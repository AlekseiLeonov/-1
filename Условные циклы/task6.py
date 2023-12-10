list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

num_max = 0 # Значение максимального числа
index_max = 0 # Индекс максимального числа
num_last = list_numbers[-1] # Значение последнего числа

for i in range(len(list_numbers)):
    if num_max <= list_numbers[i]:
        num_max = list_numbers[i]
        index_max = i
list_numbers[index_max] = num_last
list_numbers[-1] = num_max

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
