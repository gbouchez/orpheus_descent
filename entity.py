import tcod


class Entity:
    def __init__(self, x, y):
        self.char = 'o'
        self.color = tcod.yellow
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
