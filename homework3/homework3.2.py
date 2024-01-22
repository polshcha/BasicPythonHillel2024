# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

def last_to_first_element(my_list):
    list_copy = my_list.copy()
    if len(list_copy) >= 2 and list_copy != "":
        temp = list_copy[-1]
        list_copy.pop(-1)
        list_copy.insert(0, temp)
    return list_copy


list_one = [12, 3, 4, 10]
list_one_transformed = last_to_first_element(list_one)
print(f"{list_one} => {list_one_transformed}", end="\n")

list_two = [1]
list_two_transformed = last_to_first_element(list_two)
print(f"{list_two} => {list_two_transformed}", end="\n")

list_three = []
list_three_transformed = last_to_first_element(list_three)
print(f"{list_three} => {list_three_transformed}", end="\n")

list_four = [12, 3, 4, 10, 8]
list_four_transformed = last_to_first_element(list_four)
print(f"{list_four} => {list_four_transformed}", end="\n")


