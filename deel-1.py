import string
from tkinter import W

def is_valid_password(password):
    return (len(password) == 12 and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password))

def main():
    while True:
        user_password = input("Enter a password: ")
        if is_valid_password(user_password):
            print("Welcome.")
            break
        else:
            print("Password does not adhere to complexity rules.")
            print("Please make sure the password has 12 characters, at least one uppercase letter, one number, and one punctuation mark.")

if __name__ == "__main__":
    main()
W