ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    if not str_:
        return False
    for simbol in str_:
        if simbol not in ALLOW_SYMBOLS:
            return False
    return True


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
