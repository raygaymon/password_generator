from random import choice
import string

def generate_password(min_length, number = True, special = True):
    alphabets = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # create pool of characters to choose from - default is only alphabets
    choose_from = alphabets

    # include digits into the pool if indicated
    if number:
        choose_from += digits
    # include special characters into the pool if indicated
    if special:
        choose_from += special_chars

    # final password to be returned
    pwd = ""
    # booleans to check if the user's criteria for their desired password is met
    meet_criteria = False
    have_num = False
    have_special = False

    # to continue loop of getting characters while the password is shorter than the required length and while the criteria for password is not met
    while not meet_criteria or len(pwd) < min_length:
        char_to_add = choice(choose_from)
        pwd += char_to_add

        # checking if number and special character criteria are fulfilled - checking by character is more efficient than checking entire pwd
        if char_to_add in digits:
            have_num = True
        elif char_to_add in special_chars:
            have_special = True

        meet_criteria = True

        # if user wants to include digits - then meet_criteria is set to whether the current pwd contains digits
        if number:
            meet_criteria = have_num
        
        # if user wants to include special characters - then meet_criteria is set to whether the current pwd contains special characters
        if special:
            meet_criteria = have_special
    
    return pwd

def get_length():

    # to get the desired legnth of password from user and to make sure users only type in digits
    while True:
        try:
            desired_length = int(input("Please indicate the length of password you desire: "))
        except ValueError:
            print("Please only enter digits.")
        else:
            return desired_length


desired_length = get_length()
# get whether users want to include numbers and/or special characters
number = input("Do you want to include numbers (y/n): ").lower() == 'y'
special = input("Do you want to include special characters (y/n): ").lower() == 'y'

pwd = generate_password(desired_length, number, special)
print(f"Your newly generated password is {pwd}. Have fun")