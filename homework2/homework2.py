# user_input = input().replace(" ", "")
#
# if len(user_input) == 4 and user_input.isdigit():
#     for i in user_input:
#         print(i, end="\n")

NUMBER_OF_DIGITS = 4

user_input = input().replace(" ", "")

if user_input.isdigit():
    quotient, remainder = divmod(len(user_input), NUMBER_OF_DIGITS)

    if quotient == 1 and remainder == 0:
        for i in user_input:
            print(i, end="\n")

