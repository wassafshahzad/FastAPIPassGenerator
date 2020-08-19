import random
from constant import ALLOWED_CHARACTERS, MIN_LENGTH


def generate_pass(length):
    return {
        "password": "".join(random.choice(ALLOWED_CHARACTERS)
                            for x in range(length))}
