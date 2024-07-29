import secrets
import string
import pyperclip

def generate_password(length, has_uppercase, has_lowercase, has_digits, has_symbols):
    characters = ''
    if has_uppercase:
        characters += string.ascii_uppercase
    if has_lowercase:
        characters += string.ascii_lowercase
    if has_digits:
        characters += string.digits
    if has_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Password must include at least one character type")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("Password copied to clipboard.")

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 1:
                raise ValueError
        except ValueError:
            print("Invalid input. Password length must be a positive integer.")
            continue

        has_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        has_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        has_digits = input("Include digits? (y/n): ").lower() == 'y'
        has_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, has_uppercase, has_lowercase, has_digits, has_symbols)
        print(f"Generated password: {password}")

        copy = input("Copy password to clipboard? (y/n): ").lower() == 'y'
        if copy:
            copy_to_clipboard(password)

        again = input("Generate another password? (y/n): ").lower() == 'y'
        if not again:
            print("Farewell! Thanks for using the Password Generator.")
            break

if __name__ == "__main__":
    main()