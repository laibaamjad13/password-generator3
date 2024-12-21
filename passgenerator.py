import random
import string

print("Name: Laiba Amjad")
print("Registration Number: 065258")

def generate_password(length=12):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_chars = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

try:
    length = int(input("Enter password length (minimum 8): "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")

print("Name: John Doe")
print("Registration Number: 123456")
