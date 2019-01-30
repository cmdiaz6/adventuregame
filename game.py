import os
import time
import world
from player import Player

def play():
    os.system('clear')
    world.load_tiles()
    player = Player()

    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text(player))

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            time.sleep(0.25)
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                if action.hotkey is not "g":
                    print(action)
            action_input = input('Action: ')
            print('')
            os.system('clear')
            time.sleep(0.25)
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break

if __name__ == "__main__":
    play()
