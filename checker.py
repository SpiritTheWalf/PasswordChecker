import re
print("Hello there! I am a password checker!")
print("How many characters does your password need to contain?")
chars_needed = int(input())
print(f"Got it! Your password needs to contain {chars_needed} characters!")

print("How many special characters does your password need to contain?")
special_chars = int(input())
print(f"Ok! {special_chars} special characters it is!")

print("How many numbers does your password need to contain?")
no_num = int(input())
print(f"Ok! {no_num} numbers!")

print("Now then! Please enter the password you plan on using and I will check it for you")
password = input()
print("Give me a moment, testing your password...")

def length_check():
    if len(password) > chars_needed:
        print("You password has the required number of characters")
    else:
        print(f"Test failed! Your password needs {chars_needed} and you only have {len(password)}!")


def contains_special_chars():
    contains_special_char = False
    for letter in password:
        if (not letter.isnumeric() and not letter.isdigit()):
            contains_special_char = True
            break



        


