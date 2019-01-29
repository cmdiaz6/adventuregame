import items, enemies, actions, world
import time

class MapTile:
    """The base class for a tile within the world space"""
    def __init__(self, x, y):
        """Creates a new tile.

        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        """
        self.x = x
        self.y = y

    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.GodMode())
        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find YOURSELF in a room.
        1 SELF added to inventory!

        there is a door to the North, you should get your bearings and figure out which way is North"""

    def modify_player(self, player):
        #Room has no action on player
        pass

class LeaveCaveRoom(MapTile):
    def intro_text(self):
#        return """
        print("""
        You see an exit sign up ahead... sirens are in the distance and the walls flash red and blue...
        You squint against the brightness and exit clutching your FINE ROCK.
        
        The officers force you to the ground while medics rush past, too late, to the spiders who had called them.
        Your FINE ROCK tumbles from your hand and lands among a pile of COMMON ROCKs, where it will wait for your return...
       
        In ROCK SEARCH III, coming SPRING 1996!
        """)
        time.sleep(3)
        return """
        . . . ?
        """
        time.sleep(1)

    def modify_player(self, player):
        player.victory = True

class LootRoom(MapTile):
    """A room that adds something to the player's inventory"""
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class FindRockRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Rock())
 
    def intro_text(self):
        return """
        Your notice something sitting in the corner.
        It's a ROCK! You are drawn to it. You pick it up and place it among your impressive collection.
        """

class FindFineRockRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.FineRock())
 
    def intro_text(self):
        return """
        Your notice another rock. Something about this rock fills you with dread.
        It's a FINE ROCK! This rock is much older than most rocks and full of the wisdom that age brings.
        The rock may not be as functional as the more pragmatic rocks in your collection, but it makes a fine travelling partner 
        """


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print(f"The enemy hurls {self.enemy.damage} damager orbs at you. You have {the_player.hp} vitality units remaining.")
            print('')

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class BigOlSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BigOlSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A big ol' spider spooks the hell out of you!
            """
        else:
            return """
            A large spider lays dead here, mourned by its children
            """

class LilSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.LilSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A lil' spider waits for its mother to return.
            """
        else:
            return """
            A small smudge is on the floor. All that is left of the proud Spider race
            """


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
