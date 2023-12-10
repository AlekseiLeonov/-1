list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

counter_pos = 0 # Счетчик четных
counter_neg = 0 # Счетчик нечетный

for i, j in enumerate(list_):
    number = int(j % 2)
    if number == 0:
        counter_pos += 1
    elif number != 0:
        counter_neg += 1

if counter_neg > counter_pos:
    print("Нечетных чисел больше")
elif counter_neg == counter_pos:
    print("Четных и нечетных одинаковое количество")
elif counter_neg < counter_pos:
    print("Четных чисел больше")
