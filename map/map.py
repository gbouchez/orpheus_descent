import tcod


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.init_tiles()

    def init_tiles(self):
        tiles = [[Tile() for x in range(self.width)] for y in range(self.height)]

        for x in range(35, 45):
            for y in range(20, 30):
                tiles[y][x].blocked = False
                tiles[y][x].block_sight = False
                tiles[y][x].color = tcod.Color(50, 50, 150)

        return tiles

    def is_blocked(self, x, y):
        if self.tiles[y][x].blocked:
            return True

        return False


class Tile:
    def __init__(self):
        self.blocked = True
        self.block_sight = True
        self.color = tcod.Color(0, 0, 100)
