src = not False and True or False and not True # Исходное выражение


# result = True and True or False and False # Убираем отрицание
# result = True or False # Убираем логическое и
# result = True # Убираем логическое или

result = True

print(src == result)
