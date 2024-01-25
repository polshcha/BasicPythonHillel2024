# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

def zeros_to_end(my_list):
    my_list_copy = my_list.copy()
    if my_list_copy != "" and len(my_list_copy) > 1:
        for index in range(len(my_list_copy)):
            if my_list_copy[index] == 0:
                temp = my_list_copy.pop(index)
                my_list_copy.append(temp)
    return my_list_copy


list_1 = [0, 1, 0, 12, 3]
list_2 = [0]
list_3 = [1, 0, 13, 0, 0, 0, 5]
list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

list_1_changed = zeros_to_end(list_1)
list_2_changed = zeros_to_end(list_2)
list_3_changed = zeros_to_end(list_3)
list_4_changed = zeros_to_end(list_4)

print(f"{list_1} => {list_1_changed}")
print(f"{list_2} => {list_2_changed}")
print(f"{list_3} => {list_3_changed}")
print(f"{list_4} => {list_4_changed}")
