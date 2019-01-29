from random import randint

def roll(num_dice,sides):
    """Rolls Dice"""
    return [randint(1,sides) for i in range(num_dice)]


