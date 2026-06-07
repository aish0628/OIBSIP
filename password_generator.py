import random
import string

def generate_password(length,use_letters , use_numbers , use_symbols):

    char =""
    if use_letters:
        char += string.ascii_letters
    if use_numbers:
        char += string.digits
    if use_symbols:
        char += string.punctuation
    if char =="":
        print("ERROR : Select at least one character")
        return None
    password = ""
    for i in range(length):
        password += random.choice(char)
    return password

print("="*40)
print("RANDOM PASSWORD GENERATOR")
print("="*40)

while True :
    try :
        length = int(input("Enter the length of the password(4-32): "))
        if 4<=length<=32 :
            break
        else:
            print("Please enter a number between 4 and 32")
    except ValueError:
        print("Invalid ! Enter a number")

print("Choose character type(y/n) : ")
letters_choice =input("Add letters in password (y/n): ").lower()
numbers_choice =input("Add numbers in password (y/n): ").lower()
symbols_choice = input("Add symbols in password (y/n)").lower()

use_letters = letters_choice == "y"
use_numbers = numbers_choice == "y"
use_symbols = symbols_choice == "y"

password = generate_password(length,use_letters,use_numbers,use_symbols)
print("="*40)
print("PASSWORD GENERATOR",password)
print("="*40)

while True :
    again = input("Do you want to generate another password (y/n): ").lower()
    if again == "y" :
        password = generate_password(length,use_letters,use_numbers,use_symbols)
        print("New Password : ", password)
    else :
       print("THANK YOU FOR USING THIS PASSWORD GENERATOR")
       break

