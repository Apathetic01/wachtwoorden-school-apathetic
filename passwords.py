import string

def is_valid_password(password):
    return (
        len(password) >= 12 and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)
    )

def main():
    while True:
        user_password = input("Enter a password: ")

        if is_valid_password(user_password):
            print("Welcome")
            break
        else:
            print("Invalid password. Please make sure your password has the following:")
            print("- At least 12 characters")
            print("- At least one uppercase letter")
            print("- At least one number")
            print("- At least one punctuation mark")

if __name__ == "__main__":
    main()
