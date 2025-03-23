import random
import string

def generate_unique_random_string(length, existing_strings=None):
    if existing_strings is None:
        existing_strings = set()
    
    while True:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if random_string not in existing_strings:
            existing_strings.add(random_string)
            return random_string
