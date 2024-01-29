def get_data():
    num_one = input("~Please, input the first number: ").replace(" ", "")
    math_operation = input("~Math operation? \"+\", \"-\", \"/\" or \"*\": ").replace(" ", "")
    num_two = input("~Please, input the second number: ").replace(" ", "")
    return num_one, math_operation, num_two


def calc(num_1, operation, num_2):
    try:  # перевірка чи данні є числами (float щоб не обрізати після точки)
        num_1 = float(num_1)
        num_2 = float(num_2)
        if operation == "+":
            result = num_1 + num_2
        elif operation == "-":
            result = num_1 - num_2
        elif operation == "*":
            result = num_1 * num_2
        elif operation == "/" and num_2 != 0:
            result = num_1 / num_2
        else:  # num_2 нуль при діленні або operation не з перерахованих
            result = None
    except:  # num_1 або num_2 не числа
        result = None
    return result


counter = 0  # підраховуємо обчислення
while True:
    numb_1, mth_operation, numb_2 = get_data()
    calc_result = calc(numb_1, mth_operation, numb_2)
    if calc_result is None:
        print("Sorry, cannot complete your calculation :( \n Check your input and try again.")
        counter = counter + 1
        print(f"Do you want any more calculations?", end="\n")
        more_calc = input("[y/Y/Yes] ~ [n/N/No]:").replace(" ", "")
        if more_calc == "y" or more_calc == "Y" or more_calc == "yes" or more_calc == "Yes":
            continue
        else:
            print(f"Thanks for using the calculator!  \n\tCalculations count: {counter}")
            break
    else:
        print(f"\t{numb_1} {mth_operation} {numb_2} = {calc_result}")
        counter = counter + 1
        print(f"Do you want any more calculations?", end="\n")
        more_calc = input("\t[y/Y/Yes] ~ [n/N/No]:").replace(" ", "")
        if more_calc == "y" or more_calc == "Y" or more_calc == "yes" or more_calc == "Yes":
            continue
        else:
            print(f"Thanks for using the calculator!  \n\tCalculations count: {counter}")
            break

