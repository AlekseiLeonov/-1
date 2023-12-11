def count_letters(text): # Должна вернуть словарь с ключами из букв нижнего регистра
    text = text.lower()
    dict_ = {}
    for char in text:
        if char.isalpha():
            count = text.count(char)
            dict_[char] = count
    return dict_


def calculate_frequency(dict_):
    len_text = sum(dict_.values()) #701
    frequencies = {}
    for letter, count in dict_.items():
        frequency = count / len_text
        frequencies[letter] = format(frequency, '.2f')
    return frequencies


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

dictionary = count_letters(main_str)
frequency = (calculate_frequency(dictionary))
for letter, frequency in frequency.items():
    print(f"{letter}: {frequency}")
