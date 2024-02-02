my_dict_1 = {1: 1, 2: 2}
dict_1_keys = list(my_dict_1.keys())  # зразу створюємо list з ключів бо знадобиться потім
first_dict_only_keys = []  # поки порожній list куди будемо складати ключі що є тільки в перш. dict

my_dict_2 = {11: 11, 2: 22}
dict_2_keys = list(my_dict_2.keys())
second_dict_only_keys = []

both_dict_keys = []  # порожній list де будуть ключі спільні для обох словників
new_dict = {}  # словник що створюється за умовою завдання 2.в
new_dict_rule = {}  # словник  створений за правилом, відповідно завдання 2.г

for i in range(len(dict_1_keys)):
    if dict_1_keys[i] in dict_2_keys:  # шукаємо елементи що є в обох словниках
        both_dict_keys.append(dict_1_keys[i])
    else:  # якщо елемент є лише в першому словнику та його немає у другому
        first_dict_only_keys.append(dict_1_keys[i])  # елементи, що є лише в першому словнику

for i in range(len(dict_2_keys)):  # додатковий цикл щоб знайти елементи що тільки в другому словнику
    if dict_2_keys[i] not in dict_1_keys:  # перереробити цикл for вище додавши цю умову туди (?)
        second_dict_only_keys.append(dict_2_keys[i])

print(f'key(s) {both_dict_keys} is in both dictionaries', end="\n")
print(f'key(s) {first_dict_only_keys} is in first dictionary  only', end="\n")

for i, j in my_dict_1.items():  # проходимося по всьому словнику №1 з його keys та values
    temp_dict = {}  # тимчасовий словник щоб запхнути його у новий (прибрати та переробити(?))
    if my_dict_1[i] in first_dict_only_keys:  # нас цікавлять лише елементи унікальні для 1 словника
        temp_dict[i] = j  # забираємо з словника 1 лише унікальні елементи, заносимо в temp (key та value)
        new_dict.update(temp_dict)  # пхаємо тимчасовий словник з потрібними данними в новий

print(f'new dictionary for key(s) that are 1st dictionary only [{new_dict}]')

new_dict_rule.update(new_dict)  # пхаємо в словник-правило той, що створений вище, відповідно завдання
for i in range(len(second_dict_only_keys)):  # аналог циклу, написаного вище (?) для унікальних 2го сл.
    temp_dict = {}
    temp_val = my_dict_2.get(second_dict_only_keys[i])  # забираємо value унікальних для 2 сл. елем.
    temp_dict[second_dict_only_keys[i]] = temp_val  # наповнюємо тимчасовий словник
    new_dict_rule.update(temp_dict)  # пхаємо у словник-правило

for i in range(len(both_dict_keys)):  #  ключі що в обох словниках
    temp_dict = {}  # тимчасовий словник який запхаємо в словник-правило
    temp_list = []  # тимчасовий list для значень з 1 та 2 словника

    temp_val = my_dict_1.get(both_dict_keys[i])  # забираємо value унік. елем. для 1 словника
    temp_list.append(temp_val)  # додаємо value в тимчасовий list
    temp_val = my_dict_2.get(both_dict_keys[i])  # забрали value унік. елем. для 2го словника
    temp_list.append(temp_val)  # value в тимчасовий list в купу до того що додали вище

    temp_dict[both_dict_keys[i]] = temp_list  # тимчасовий словник для спільного ключа та list of values
    new_dict_rule.update(temp_dict)  # кладемо створений словник у словник-правило

print('~dictionary, created with the rule is:', end="\n")
print(f'\t{new_dict_rule}')



