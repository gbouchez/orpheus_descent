import tcod

import console
import input
import variables
from map.bounded_map import BoundedMap
from player import Player


def run():
    console.init()

    key = tcod.Key()
    mouse = tcod.Mouse()

    player = Player(int(variables.screen_width / 2), int(variables.screen_height / 2))
    game_map = BoundedMap(80, 50)

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)
        console.update(player, game_map)

        action = input.handle_keys(key)

        move = action.get('move')
        quit_game = action.get('exit')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        if quit_game:
            return True

        if key.vk == tcod.KEY_ESCAPE:
            return True
