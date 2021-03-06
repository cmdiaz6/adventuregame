"""Describes the items in the game."""

class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.count = 0
        self.taken = False

    def __str__(self):
        return "{}: {}\nValue: {}".format(self.name,self.description,self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}: {}\nValue: {}\tDamage: {}".format(self.name,self.description,self.value,self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="It's a rock. It's pretty old.",
                         value=0,
                         damage=5)
                         
class FineRock(Weapon):
    def __init__(self):
        super().__init__(name="Fine Rock",
                         description="It's a fine rock, indeed! It's quite a bit older than most rocks.",
                         value=0,
                         damage=4)

class Glove(Weapon):
    def __init__(self):
        super().__init__(name="Glove",
                        description="A velvet ceremonial glove used to demand satisfaction with a forceful slap.",
                        value=1,
                        damage=1)

class Healing(Item):
    def __init__(self, name, description, value, heal):
        self.heal = heal
        super().__init__(name, description, value)

    def __str__(self):
        return "{}: {}\nValue: {}\tRestorative Power: {}".format(self.name,self.description,self.value,self.heal)

class Poultice(Healing):
    def __init__(self):
        super().__init__(name="Fig Poultice",
                         description="A poultice made of fig to mend your afflictions.",
                         value=10,
                         heal=10)
