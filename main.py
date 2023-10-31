import string
import random

import string

def is_valid_password(password):
    valid_punctuation = string.punctuation + "@#"
    return (len(password) >= 12 and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in valid_punctuation for c in password))

def check_passwords(passwords):
    for i, password in enumerate(passwords, 1):
        if is_valid_password(password):
            print(f"Password {i}: '{password}' - Valid")
        else:
            print(f"Password {i}: '{password}' - Invalid")

if __name__ == "__main__":
    password_list = [
        "AbC",
        "Pssw0rdLongerThanCharacters12",
        "AllsffesfLowercasepass3",
        "StrongdfgdfgdfgdgdfgdfgdPssW22",
        "NoUppgdfgdgdfgdgdg@fer2",
        "NfesfsefsefeoNumbe3r",
        "Pssw0fgdsfrdL.ongerThanCharacters4",
        "NoPunffdgdgdfg34ctuationPass",
        "NoNu4mber",
        "Short3Pwe",
        "GoodfsfsdPs6sword",
        "Validscbshcbshbdhvbsdvbsd.fl#0Pss",
        "Secure,Pw8d",
        "Safgfsdnvgjndrjvgfnfrndfklvn;dfklnvl;dfkvnd;fkl.e7Pwd"
    ]
    check_passwords(password_list)


def generate_password(length):
    if length < 12:
        return "Password length should be at least 12 characters."

    # Define character sets for each category
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(symbols)

    # Generate the rest of the password
    remaining_length = length - 4
    all_characters = lowercase_letters + uppercase_letters + digits
    password += ''.join(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the characters in the password
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

def program_1():

    while True:
        user_password = input("Enter a password: ")
        if is_valid_password(user_password):
            print("Welcome.")
            break
        else:
            print("Password does not adhere to complexity rules.")
            print("Please make sure the password has 12 characters, at least one uppercase letter, one number, and one punctuation mark.")

def program_2():
    while True:
        try:
            print("\nThis program generates 50 passwords of a specified length and saves them to a .txt file")
            print("The passwords will include upper case and lower case letters, numbers, and one symbol")

            length = int(input("Enter the desired password length: "))
            if length < 12:
                print("\nPassword length should be at least 12 characters.")
            else:
                num_passwords = 50

                with open("passwords.txt", "w") as file:
                    for _ in range(num_passwords):
                        password = generate_password(length)
                        file.write(password + "\n")

                print(f"{num_passwords} passwords generated and saved to 'passwords.txt'")
                break  # Exit the loop when the operation is successful

        except ValueError:
            print("Invalid input. Please enter a valid password length.")

def program_3():
    while True:
        try:
            print("\nThis program generates 50 passwords of a specified length and saves them to a .txt file")
            print("The passwords will include upper case and lower case letters, numbers, and one symbol")
            print("Additionally, every generated password will include a reversed version")

            length = int(input("Enter the desired password length: "))
            if length < 12:
                print("\nPassword length should be at least 12 characters.")
                continue  # Continue to the beginning of the loop

            num_passwords = 50

            with open("reverse-passwords.txt", "w") as file:
                for _ in range(num_passwords):
                    password = generate_password(length)
                    reverse_password = password[::-1]  # Create the reverse of the password
                    combined_passwords = f"{password} {reverse_password}"  # Combine both passwords with a space
                    file.write(combined_passwords + "\n")

            print(f"{num_passwords} pairs of passwords generated and saved to 'reverse-passwords.txt'")
            break  # Exit the loop when the operation is successful

        except ValueError:
            print("Invalid input. Please enter a valid password length.")

def program_4():
    # Add your code for the fourth program here
    pass

def main():
    while True:
        print("\n Select a program:")
        print("1: Password Checker")
        print("2: Password Generator")
        print("3. Reversed Password Generator")
        print("4. Program 4")
        print("0. Exit")

        choice = input("Enter the program number (1-4) or 0 to exit: ")

        if choice == '1':
            program_1()
        elif choice == '2':
            program_2()
        elif choice == '3':
            program_3()
        elif choice == '4':
            program_4()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid program number or 0 to exit.")

if __name__ == "__main__":
    main()
