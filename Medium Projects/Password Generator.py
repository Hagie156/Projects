# Here are all the things I have imported

import random
import string #This is a module that collects all letters (a-z & A-Z), numbers and special characters


# Here we will prompt the user questions for how they want their password to be set up

min_length = int(input("What is the minimum amount of characters you require for your password? "))
contain_digit = input('Do you require numbers in your password? Please type "y" if yes: ').lower() == "y"
contain_special = input('Do you require special characters in your password? Please type "y" if yes: ' ).lower() == "y"



# Here we will define our own generate password function

def gen_password(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters # Only letters (a-z & A-Z)
    digits = string.digits # Only numbers (0-9)
    special = string.punctuation # Only special characters 



# Here we will establish the potential characters that will in the password

    characters = letters # By defaul
    if numbers: 
        characters += digits # if numbers is needed, add numbers to the randomised characters 
    if special_char:
        characters += special # if special_char is needed, add special_char to the randomised characters



#Here we establish the initial parameters of the password that will alter as the password generates 
    password = ""
    requirement = False
    contain_digit = False
    contain_special = False



# Here we have created a loop until the user gets a password that meets their expectation
    while not requirement or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char


        # Here we will check for required characters
    
        if new_char in digits:
            contain_digit = True 
        if new_char in special:
            contain_special = True



        # This ensures that the requirements are met 

        requirement = True
        if numbers:
            requirement = contain_digit
        if special_char:
            requirement = requirement + contain_special
    

    return password



password = gen_password(min_length, contain_digit, contain_special)
print('Here is your new password: ' + password)







