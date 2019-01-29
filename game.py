import os
import time
import world
from player import Player

def play():
    os.system('clear')
    world.load_tiles()
    player = Player()

    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            time.sleep(0.5)
            for action in available_actions:
                if action.hotkey is not "g":
                    print(action)
            action_input = input('Action: ')
            print('')
            os.system('clear')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break

if __name__ == "__main__":
    play()
