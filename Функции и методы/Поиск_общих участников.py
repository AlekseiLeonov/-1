def find_common_participants(str1, str2, divider=","):
    split_str_1 = str1.split(divider)
    split_str_2 = str2.split(divider)
    common_name = set(split_str_1).intersection(split_str_2)
    return sorted(list(common_name))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(f'общий список участников {find_common_participants(participants_first_group, participants_second_group)}')




