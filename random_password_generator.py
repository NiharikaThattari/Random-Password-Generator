import string
import random

# characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password(length_of_pass):
    length = length_of_pass

    # shuffling the characters
    random.shuffle(characters)

    # picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    # printing the list
    generated_password = "".join(password)
    return generated_password


if __name__ == "__main__":
    length = int(input("Enter password length: "))
    resultant_password = generate_random_password(length)
    print(resultant_password)