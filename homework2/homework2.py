user_input = int(input("~Please, input a number (4 digits only): "))

thousands, remainder = divmod(user_input, 1000)
hundreds, remainder = divmod(remainder, 100)
tens, ones = divmod(remainder, 10)

print(f"{thousands}\n{hundreds}\n{tens}\n{ones}")


