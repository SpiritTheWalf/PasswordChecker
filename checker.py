"""
Just a simple password checker
"""
import re
print("Hello there! I am a password checker!")
print("How many characters does your password need to contain?")
chars_needed = int(input())
print(f"Got it! Your password needs to contain at least {chars_needed} characters!")

print("How many special characters does your password need to contain?")
special_chars_needed = int(input())
print(f"Ok! At least {special_chars_needed} special characters it is!")

print("How many numbers does your password need to contain?")
no_num_needed = int(input())
print(f"Ok! At least {no_num_needed} numbers!")

print("Now then! Please enter the password you plan on using and I will check it for you:")
password = input()
print("Give me a moment, testing your password...")


def length_check(password, chars_needed):
    """Checks the length of the password"""
    return len(password) >= chars_needed

def count_chars(password):
    """returns the number of chars in the password"""
    numbers = re.findall(r"\d", password)
    special_chars = re.findall(r"[^\w\s]", password)

    return {
        "num": len(numbers),
        "special_chars": len(special_chars)
    }

def number_check(password, no_num_needed):
    """checks if the amount of numbers passes"""
    char_count = count_chars(password)
    num = char_count["num"]
    return num >= no_num_needed

def special_check(password, special_chars_needed):
        """checks if the amount of special characters passes"""
    char_count = count_chars(password)
    special_char_count = char_count["special_chars"]
    return special_char_count >= special_chars_needed

def run_checks(password, chars_needed, no_num_needed, special_chars_needed):
        """Method to run all the checks"""
    checks = [
        ("length check", length_check(password, chars_needed)),
        ("number check", number_check(password, no_num_needed)),
        ("special character check", special_check(password, special_chars_needed))
    ]

    all_passed = True
    for check_name, result in checks:
        if not result:
            print(f"Your password failed the {check_name}.")
            all_passed = False

    if all_passed:
        print("Your password passed all checks!")
    else:
        print("Please update your password to meet the requirements.")

run_checks(password, chars_needed, no_num_needed, special_chars_needed)
