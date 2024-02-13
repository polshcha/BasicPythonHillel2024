def find_unique_value(my_list):
    unique_value = 0
    for val in range(len(my_list)):
        val_count = 0
        for elem in range(len(my_list)):
            if my_list[val] == my_list[elem]:
                val_count += 1
        if val_count == 1:
            unique_value = my_list[val]
            break
        else:
            continue

    return unique_value


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")