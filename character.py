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
        #returns relative coords when given absolute coords
        scords =  acords[0] - self.coordinates[0], acords[1] - self.coordinates[1]
        return scords

    def chposcalc(self):
        #returns position of the character (middle of the screen)
        size = self.screen.get_size()
        chpos = size[0]/2 - self.gsize[0]/2, size[1]/2 - self.gsize[1]/2
        return chpos

    def poscalc(self, cords):
        #returns relative positon based on absolute coords
        scords = self.cordcalc(cords)
        middle = self.chposcalc()
        spos = (scords[0] * self.gsize[0]) + middle[0], (scords[1] * self.gsize[1]) + middle[1]
        return spos

    def changecord(self, cord):
        #changes absolute coordintes of an character
        self.coordinates = self.coordinates[0] + cord[0], self.coordinates[1] + cord[1]

    def get_cords(self):
        #gives absolute coordinates of an character
        return self.coordinates

    def get_fcords(self, cords):
        #gives future cords of an character based on given change in coords
        return self.coordinates[0] + cords[0], self.coordinates[1] + cords[1]

    def get_sprite(self):
        #gives sprite of an character
        return self.sprite

    def rotate(self, way):
        #rotates sprite of an carater (0=north, 1=east, 2=south, 3=west)
        if way != 0 and way != self.way:
            self.sprite = pygame.transform.rotate(self.sprite, (self.way - way) * 90)
            self.way = way
        elif way != self.way:
            self.sprite = pygame.transform.rotate(self.sprite, self.way * 90)
            self.way = way

    #mouse section

    def mouse(self):
        #returns position of the mouse acording to the tiles on the screen
        pos = pygame.mouse.get_pos()
        cords = pos[0] - (pos[0]-8) % self.gsize[0], pos[1] - (pos[1]-8) % self.gsize[1]
        return cords

    def mousetocords(self):
        #returns relative coordinats of the mouse pointer
        apos = self.mouse()
        apos = int(apos[0] / self.gsize[0]), int(apos[1] / self.gsize[1])
        return apos

    def mouseRch(self):
        #returns the relative change in coords of the mouse to character
        cord = self.mousetocords()
        screen = self.screen.get_size()
        midoff = cord[0] - int((((screen[0] - self.gsize[0]/2) / self.gsize[0])) / 2), cord[1] - int((((screen[1] - self.gsize[1]/2) / self.gsize[1])) / 2)
        return midoff

    def get_AbsoluteCordOfMouse(self):
        #returns absolute cords of the mouse
        midoff = self.mouseRch()
        acord = self.get_fcords(midoff)
        return acord