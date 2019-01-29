import json
from random import randrange

with open('critter_names.json') as f:
    critter_names = json.load(f)
with open('character.json') as f:
    character = json.load(f)

size = int(input("How big do you want the map? (recomended between 10 and 20): "))
char_xy = [0,0]
critter_list = {}
door = [randrange(0, size), randrange(0, size)]
new_level = True
player_in_range = False
level = 0

def attack(name):
    critter_list[name][2] = critter_list[name][2] - character["weapon_rating"]

def defend(name):
    character["hp"] = character["hp"] - (critter_list[name][3]/character["armour_rating"])

def critter_gen():
    for i in critter_names:
        if randrange(1, 6) == 3:
            #[xpos, ypos, hp, attack]
            critter_list[i] = [randrange(0, size), randrange(0, size), randrange(1, 100), randrange(1, 25)]

def player_input():
    move = input("It's your move! ")
    if move in "wasd":
        index, increment = {
            "w": (0, -1),
            "a": (1, -1),
            "s": (0, 1),
            "d": (1, 1)
            }(move)
        try:
            char_xy[index] += increment
        except IndexError:
            print("That is not a valid move")
    elif move == "e":
        if door[0] == char_xy[0] and door[1] == char_xy[1]:
            new_level = True
    elif move == "f":
        attack_pos = [
            (char_xy[0] + x, char_xy[1] + y)
            for x in range(-1, 2)
            for y in range(-1, 2)
        ]
        for critter_name, critter_info in critter_list.items():
            if critter_info[:2] in attack_pos:
                attack(critter_name)
                if critter_info[:2] == char_xy[:2]:
                    defend(critter_name)
    else:
        print("That is not a valid move")

def map_gen():
    asc = '-'
    gen = [size * [asc] for i in range(size)]
    gen[char_xy[0]][char_xy[1]] = '@'
    for critter in critter_list.values():
        gen[critter[0]][critter[1]] = "M" if critter[2] > 0 else "X"
    gen[door[0]][door[1]] = "D"
    print('\n'.join(' '.join(row) for row in gen))

def ai():
    attack_pos = [
        (char_xy[0] + x, char_xy[1] + y)
        for x in range(-1, 2)
        for y in range(-1, 2)
    ]
    for critter_name, critter_info in critter_list.items():
        if critter_info[2] > 0:
            if critter_info[:2] in attack_pos:
                defend(critter_name)
                if critter_info[:2] == char_xy[:2]:
                    attack(critter_name)
            else:
                index, increment = [
                    (0, -1),
                    (1, -1),
                    (0, 0),
                    (0, 1),
                    (1, 1)
                ](random.randrange(0, 5))
                try:
                    critter_info[index] += increment
                except IndexError:
                    pass

while character["hp"] > 0:
    if new_level == True:
        door = [randrange(0, int(size)), randrange(0, int(size))]
        critter_list = {}
        critter_gen()
        map_gen()
        level += 1
        new_level = False
    elif new_level == False:
        print("N A M E:  " + character["name"])
        print("H E A L T H:  " + str(character["hp"]))
        print("W E A P O N:  " + str(character["weapon_rating"]) + "     " + character["weapon_name"])
        print("A R M O U R:  " + str(character["armour_rating"]) + "     " + character["armour_name"])
        for i in critter_list:
            print("E N E M Y:  " + str(i) + "     " + "H P: " + str(critter_list[i][2]) + "     " + "A T K: " + str(critter_list[i][3]))
        player_input()
        ai()
        map_gen()
        if door[0] == char_xy[0] and door[1] == char_xy[1]:
            new_level = True

print()
print()
print(" ________________________________________________")
print("|    G    A    M    E        O    V    E    R    |")
print(" IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
print()
print("            You Reached L E V E L: " + str(level))
