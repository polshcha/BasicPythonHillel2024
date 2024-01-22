def calc(first_num, second_num, operation):
    if operation == "+":
        result = first_num + second_num
    elif operation == "-":
        result = first_num - second_num
    elif operation == "*":
        result = first_num * second_num
    elif operation == "/" and second_num != 0:
        result = first_num / second_num
    else:
        result = None
    return result


num_one = int(input("~Please, input the first number: ").replace(" ", ""))
math_operation = input("~Math operation? \"+\", \"-\", \"/\" or \"*\": ").replace(" ", "")
num_two = int(input("~Please, input the second number: ").replace(" ", ""))

calc_result = calc(num_one, num_two, math_operation)
if calc_result is None:
    print("Sorry, cannot complete your calculation :( \n Check your input and try again.")
else:
    print(f"{num_one} {math_operation} {num_two} = {calc_result}")
