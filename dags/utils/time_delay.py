import random

max_delay_seconds = 425
min_delay_seconds = 360

def get_random_delay() -> int:
    return random.randint(min_delay_seconds, max_delay_seconds) 