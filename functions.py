from random import randint
import time

def roll(num_dice,sides):
    """Rolls Dice"""
    return [randint(1,sides) for i in range(num_dice)]

def slowprint(string,rate):
    for s in string:
        print(s, end="", flush=True)
        time.sleep(rate)
