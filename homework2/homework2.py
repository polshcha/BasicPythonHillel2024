user_input = input().replace(" ", "")

if len(user_input) == 4 and user_input.isdigit():
    for i in user_input:
        print(i, end="\n")