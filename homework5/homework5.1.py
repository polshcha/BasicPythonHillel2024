import keyword


def if_variable_ok(var):
    punc = "!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~"  # змінена пунктуація не включаємо _ та робимо єкранування

    if keyword.iskeyword(var):
        is_keyword = True
    else:
        is_keyword = False
    is_punc = False
# двійний цикл перевіряємо кожний символ var чи є він пунктуацією, без цього шукає тільк. на початку (?):
    for i in range(len(var)):
        for j in punc:
            if var[i] in punc:
                is_punc = True
                break
        if is_punc is True:
            break

    if var[0].isdigit() or " " in var.strip():  # чи 1 симв. змінної число та чи пробіли (крім поч. та кін)
        is_first_digit_or_space = True
    else:
        is_first_digit_or_space = False

    if var == "_":  # тому що _ при перевірці на регістр повертає .islower FALSE оброблюємо окремо
        is_upper = False
    elif var != "_" and var.islower():  # якщо var НЕ Є _ і при цьому нижній регістр
        is_upper = False
    else:
        is_upper = True

    if is_keyword or is_punc or is_first_digit_or_space or is_upper:  # якщо хоч десь тригернуло True
        var_ok = False  # змінна не ок
    else:  # все норм по всім пунктам
        var_ok = True  # змінна ОК

    return var_ok


users_var = input("~ input variable name: ")
print(if_variable_ok(users_var))
