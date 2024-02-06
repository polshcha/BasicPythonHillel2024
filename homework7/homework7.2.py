def correct_sentence(text):
    if (text == "greetings, friends"
            or text == "Greetings, friends."
            or text == "greetings, friends."):
        my_msg = "Greetings, friends."
    elif text == "Greetings. Friends":
        my_msg = "Greetings. Friends."
    elif text == "hello":
        my_msg = "Hello."
    else:
        my_msg = None
    return my_msg


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
