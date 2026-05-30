import random
import string

def generate_strong_password(length):

    if length < 4:
        return "Password length should be at least 4"

    password = []

    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    all_characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(length - 4):
        random_char = random.choice(all_characters)
        password.append(random_char)

    random.shuffle(password)

    final_password = ""

    for char in password:
        final_password += char

    return final_password


length = int(input("Enter Password Length: "))

result = generate_strong_password(length)

print("Generated Password:", result)