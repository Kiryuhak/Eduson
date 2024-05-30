import string
from random import randrange, choice

def generate() -> str:
    return ''.join(choice(string.ascii_lowercase) for i in range(3)) + str(randrange(1000000))