class MapObject:
    def __init__(self, sprite, cords, wall, block):
        self.sprite = sprite
        self.cords = cords
        self.wall = wall
        self.block = block

    def is_wall(self):
        return self.wall

    def is_block(self):
        return self.block

    def get_cords(self):
        return self.cords

    def get_sprite(self):
        return self.sprite

    def get_position(self):
        x, y = self.cords
        size = self.sprite.get_size()[0]
        return (x*size, y*size)