import pygame

class Character:
    def __init__(self, nick, player, coordinates, backpack, gsize, screen, sprite):
        self.nick = nick
        self.player = player
        self.coordinates = coordinates
        self.backpack = backpack
        self.gsize = gsize
        self.screen = screen
        self.sprite = sprite
        self.way = 0
    
    def cordcalc(self, acords):
        scords =  acords[0] - self.coordinates[0], acords[1] - self.coordinates[1]
        return scords

    def chposcalc(self):
        size = self.screen.get_size()
        chpos = size[0]/2 - self.gsize[0]/2, size[1]/2 - self.gsize[1]/2
        return chpos

    def poscalc(self, cords):
        scords = self.cordcalc(cords)
        middle = self.chposcalc()
        spos = (scords[0] * self.gsize[0]) + middle[0], (scords[1] * self.gsize[1]) + middle[1]
        return spos

    def changecord(self, cord):
        self.coordinates = self.coordinates[0] + cord[0], self.coordinates[1] + cord[1]

    def get_cords(self):
        return self.coordinates

    def get_fcords(self, cords):
        return self.coordinates[0] + cords[0], self.coordinates[1] + cords[1]

    def get_sprite(self):
        return self.sprite

    def rotate(self, way):
        if way != 0 and way != self.way:
            self.sprite = pygame.transform.rotate(self.sprite, (self.way - way) * 90)
            self.way = way
        elif way != self.way:
            self.sprite = pygame.transform.rotate(self.sprite, self.way * 90)
            self.way = way