class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class BigOlSpider(Enemy):
    def __init__(self):
        super().__init__(name="a big ol' spider", hp=10, damage=2)

class LilSpider(Enemy):
    def __init__(self):
        super().__init__(name="just a lil' Spider", hp=2, damage=0)
    
