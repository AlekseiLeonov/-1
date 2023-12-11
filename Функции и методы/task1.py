def remove_whitespace(str_):
    words_list = str_.split(" ")

    words_list_without_empty_spase = []
    for word in words_list:
        if word:
            words_list_without_empty_spase.append(word)

    return " ".join(words_list_without_empty_spase)


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
