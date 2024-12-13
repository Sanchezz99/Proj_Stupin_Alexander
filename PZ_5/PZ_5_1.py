#Составить функцию, которая напечатает сорок любых символов.
import random
def generate_random_characters(length=40):
    random_characters = ""
    while len(random_characters) < length:
        random_char = chr(random.randint(32, 126))
        random_characters += random_char
    return random_characters
random_characters = generate_random_characters()
print(random_characters)