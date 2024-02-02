my_dict_1 = {1: 1, 2: 2}
dict_1_keys = list(my_dict_1.keys())
first_dict_only_keys = []

my_dict_2 = {11: 11, 2: 22}
dict_2_keys = list(my_dict_2.keys())
second_dict_only_keys = []

both_dict_keys = []
new_dict_first_keys = []
new_dict = {}
new_dict_rule = {}

for i in range(len(dict_1_keys)):
    if dict_1_keys[i] in dict_2_keys:
        both_dict_keys.append(dict_1_keys[i])
    else:
        first_dict_only_keys.append(dict_1_keys[i])

for i in range(len(dict_2_keys)):
    if dict_2_keys[i] not in dict_1_keys:
        second_dict_only_keys.append(dict_2_keys[i])

print(f'key(s) {both_dict_keys} is in both dictionaries', end="\n")
print(f'key(s) {first_dict_only_keys} is in first dictionary  only', end="\n")

for i, j in my_dict_1.items():
    temp_dict = {}
    if my_dict_1[i] in first_dict_only_keys:
        temp_dict[i] = j
        new_dict.update(temp_dict)

print(f'new dictionary for key(s) that are 1st dictionary only [{new_dict}]')

new_dict_rule.update(new_dict)
for i in range(len(second_dict_only_keys)):
    temp_dict = {}
    temp_val = my_dict_2.get(second_dict_only_keys[i])
    temp_dict[second_dict_only_keys[i]] = temp_val
    new_dict_rule.update(temp_dict)

for i in range(len(both_dict_keys)):
    temp_dict = {}
    temp_list = []

    temp_val = my_dict_1.get(both_dict_keys[i])
    temp_list.append(temp_val)
    temp_val = my_dict_2.get(both_dict_keys[i])
    temp_list.append(temp_val)

    temp_dict[both_dict_keys[i]] = temp_list
    new_dict_rule.update(temp_dict)

print('~dictionary, created with the rule is:', end="\n")
print(f'\t{new_dict_rule}')



