import random
import items, world

class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

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

        print('')
        print(f"You attack {enemy.name} with your {best_weapon.name}!")
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print(f"You have murdered {enemy.name}.")
        else:
            print(f"{enemy.name}'s wellness deteriorates to {enemy.hp} vitality units.")
        print('')

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

################### ################### ###################
    def determine_ability_scores(self, method):
        #Sets ability scores by either 4d6 drop lowest method or by the standard array in random order
        self.abilities = {
        "Strength" :     0,
        "Dexterity" :    0,
        "Constitution" : 0,
        "Charisma" :     0,
        "Intelligence" : 0,
        "Wisdom" :       0
        }
        if method == "roll":
            for i in self.abilities:
                scores = functions.die(4, 6)
                scores.sort()
                scores = scores[1::]
                self.abilities[i] = sum(scores)
        elif method == "array":
            scores = [8, 10, 12, 13, 14, 15]
            for i in self.abilities:
                rand_index = randint(0, len(scores) - 1)
                self.abilities[i] = scores[rand_index]
                scores.pop(rand_index)
        #Add racial modifier
#        for i in self.abilities:
#            self.abilities[i] += self.race.abilities[i]

    def ability_scores_modifiers(self):
        self.str_mod = (self.abilities["Strength"] - 10) // 2
        self.dex_mod = (self.abilities["Dexterity"] - 10) // 2
        self.con_mod = (self.abilities["Constitution"] - 10) // 2
