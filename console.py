import tcod

import variables

field = None


def init():
    global field
    tcod.console_set_custom_font('assets/arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(variables.screen_width, variables.screen_height, 'Orpheus\' Descent', False)
    field = tcod.console_new(variables.screen_width, variables.screen_height)
    return None


def update(player, game_map):
    global field
    for y in range(game_map.height):
        for x in range(game_map.width):
            tcod.console_set_char_background(field, x, y, game_map.tiles[y][x].color, tcod.BKGND_SET)

    print_entity(player)
    tcod.console_blit(field, 0, 0, variables.screen_width, variables.screen_height, 0, 0, 0)
    tcod.console_flush()
    clear_entity(player)
    return None


def print_entity(entity):
    global field
    tcod.console_set_default_foreground(field, entity.color)
    tcod.console_put_char(field, entity.x, entity.y, entity.char, tcod.BKGND_NONE)


def clear_entity(entity):
    global field
    tcod.console_put_char(field, entity.x, entity.y, ' ', tcod.BKGND_NONE)
