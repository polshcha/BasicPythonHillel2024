# Пояснення:
# [0, 1, 7, 2, 4, 8] -> (0 + 7 + 4) * 8 = 88
#
# [1, 3, 5] -> 30
# [6] -> 36
# [] -> 0

def my_func(my_list):
    my_list_copy = my_list.copy()
    even_elements_sum = 0
    result = 0

    for index in range(len(my_list_copy)):
        if index % 2 == 0:
            temp = my_list_copy[index]
            even_elements_sum = temp + even_elements_sum
        if my_list_copy != "":
            result = even_elements_sum * my_list_copy[-1]
        else:
            result = 0
    return result


list_1 = [1, 3, 5]
list_2 = [6]
list_3 = []

print(f"{list_1} -> {my_func(list_1)}")
print(f"{list_2} -> {my_func(list_2)}")
print(f"{list_3} -> {my_func(list_3)}")