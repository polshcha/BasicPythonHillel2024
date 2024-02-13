def add_one(my_list):
    my_list_copy = my_list.copy()
    my_list_num = "".join(str(num) for num in my_list_copy)
    my_list_num = int(my_list_num) + 1
    my_list_copy = [int(num) for num in str(my_list_num)]
    return my_list_copy


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
