import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    characters = lowercase_letters + uppercase_letters + digits + symbols

    password = ''.join(random.choices(characters, k=length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password =generate_password(password_length)
    print(f"Generated password: {password}")