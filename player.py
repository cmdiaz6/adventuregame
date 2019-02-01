import random
import items, world
from functions import roll, slowprint
import time, sys

class Player():
    def __init__(self):
        self.level = 1
        self.xp = 1
        self.inventory = [items.Glove()]
        self.hp = 100
        self.gold = 0
        self.location_x, self.location_y = world.starting_position
        self.godmode = False
        self.victory = False

        print("Character creation screen")
        stattype = input("Determine stats with arrays (a) or roll (r)? \n>")
        time.sleep(0.1)
        if stattype == "a":
            self.determine_ability_scores("array")
        elif stattype == "r":
            slowprint("Calculating rolls",0.1)
            slowprint(" . . . .\n",0.5)
            self.determine_ability_scores("roll")
        else:
            print("\nyou apparently cannot handle this decision so it will be handled for you.\n")
            time.sleep(0.5)
            self.determine_ability_scores("roll")
        self.ability_scores_modifiers()

    def is_alive(self):
        return self.hp > 0 or self.godmode

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        print(' {} Gold'.format(self.gold))
        for item in self.inventory:
            print(item, '\n')

    def print_stats(self):
        print("\nVitality Units:",self.hp,"/100\n")
        print("level: ",self.level,"\t XP:",self.xp)
        for a in self.abilities:
            print(a,"\t",self.abilities[a])
        if self.godmode:
            print("God Mode active")
        print("")

    def toggle_god_mode(self):
        """toggles God mode"""
        self.godmode = not self.godmode
        print("God mode set to: ",self.godmode)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text(self))

    def move_north(self):
        self.move(dx=0, dy=-1)
    def move_south(self):
        self.move(dx=0, dy=1)
    def move_east(self):
        self.move(dx=1, dy=0)
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        attack_roll = sum(roll(1,20)) + self.str_mod
        attack_roll = attack_roll + 5 if self.godmode else attack_roll
        print('')
        print(f"You attack {enemy.name} with your {best_weapon.name}.")
        if attack_roll > 10:
            damage = best_weapon.damage + self.str_mod
            print(f"You inflict {damage} units of drainage upon the creature!")
            enemy.hp -= best_weapon.damage
            if not enemy.is_alive():
                if not self.godmode:
                    print(f"You have murdered {enemy.name}.")
                    self.level += random.randint(1,40)
                    xp = random.randint(1,1000)
                    print("gained {}XP".format(xp))
                    self.xp += xp
                    print("LEVEL UP!")
                else:
                    print(f"You have freed {enemy.name} from its mortal coil.")
            else:
                print(f"{enemy.name}'s wellness deteriorates to {enemy.hp} vitality units.")
        else:
            print("You missed!")
        print('')

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def look(self, tile):
        print(tile.intro_text(self))

################### ################### ###################
    def determine_ability_scores(self, method):
        #Sets ability scores by either 4d6 drop lowest method or by the standard array in random order
        self.abilities = {
        "Strength" :     0,
        "Dexterity" :    0,
        "Constitution" : 0,
        "Charisma" :     0,
        "Intelligence" : 0,
        "Wisdom  " :     0
        }
        if method == "roll":
            for i in self.abilities:
                scores = roll(4,6)
                scores.sort()
                scores = scores[1::]
                self.abilities[i] = sum(scores)
        elif method == "array":
            scores = [8, 10, 12, 13, 14, 15]
            for i in self.abilities:
                rand_index = random.randint(0, len(scores) - 1)
                self.abilities[i] = scores[rand_index]
                scores.pop(rand_index)
            
        #Add racial modifier
#        for i in self.abilities:
#            self.abilities[i] += self.race.abilities[i]

        for a in self.abilities:
            print(a,"\t",self.abilities[a], flush=True)
            time.sleep(0.05)

    def ability_scores_modifiers(self):
        self.str_mod = (self.abilities["Strength"] - 10) // 2
        self.dex_mod = (self.abilities["Dexterity"] - 10) // 2
        self.con_mod = (self.abilities["Constitution"] - 10) // 2
