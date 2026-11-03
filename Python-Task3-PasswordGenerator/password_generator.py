import random
import string


def get_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Length must be at least 8.")
            else:
                return length
        except ValueError:
            print("Please enter a whole number.")


def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please type y or n.")


def get_character_types():
    while True:
        pools = []
        if ask_yes_no("Include uppercase letters?"):
            pools.append(string.ascii_uppercase)
        if ask_yes_no("Include lowercase letters?"):
            pools.append(string.ascii_lowercase)
        if ask_yes_no("Include numbers?"):
            pools.append(string.digits)
        if ask_yes_no("Include symbols?"):
            pools.append(string.punctuation)
        if len(pools) >= 2:
            return pools
        print("Please select at least 2 character types.\n")


def generate_password(length, pools):
    # one character from each chosen type, so every type is guaranteed
    password = [random.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    while len(password) < length:
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return "".join(password)


print("=== Random Password Generator ===")
while True:
    length = get_length()
    pools = get_character_types()
    print("Your password:", generate_password(length, pools))
    if not ask_yes_no("Generate another password?"):
        print("Goodbye!")
        break
