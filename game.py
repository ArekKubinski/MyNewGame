from character import Character
import levelparser, mapobject, pygame, sys, character
from pygame.locals import *


def mouse():
    pos = pygame.mouse.get_pos()
    cords = pos[0] - (pos[0]-8) % 16, pos[1] - (pos[1]-8) % 16
    return cords

def mousetocords():
    pos = mouse()
    pos = int(pos[0] / 16), int(pos[1] / 16)
    return pos

size = width, height = 800, 800
level = levelparser.Level('level.map', size, (16, 16))
mapp = level.mapobj()
mappdic = {}
for m in mapp:
    mappdic[m.get_cords()] = m

red = pygame.image.load('red.png').convert_alpha()
charsprite = pygame.image.load('chara16.png').convert_alpha()
char = character.Character('Pej', 'Pej', (26,26), 'backpackobject', level.get_gsize(), level.get_screen(), charsprite)

screen = level.get_screen()


clock = pygame.time.Clock()


while 1:
    clock.tick(150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('boom', char.get_AbsoluteCordOfMouse())
        if event.type == pygame.KEYDOWN:           
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_w:
                if not mappdic[char.get_fcords((0, -1))].is_block():
                    char.changecord((0, -1))
                    char.rotate(0)
            elif event.key == pygame.K_a:
                if not mappdic[char.get_fcords((-1, 0))].is_block():
                    char.changecord((-1, 0))
                    char.rotate(3)
            elif event.key == pygame.K_d:
                if not mappdic[char.get_fcords((1, 0))].is_block():
                    char.changecord((1, 0))
                    char.rotate(1)
            elif event.key == pygame.K_s:
                if not mappdic[char.get_fcords((0, 1))].is_block():
                    char.changecord((0, 1))
                    char.rotate(2)
    screen.fill((0, 0, 0))
    for obj in mapp:
        tempcords = obj.get_cords()
        temptuple = char.poscalc(tempcords)
        tempsprite = obj.get_sprite()
        screen.blit(tempsprite, (temptuple[0], temptuple[1]))
    screen.blit(char.get_sprite(), char.chposcalc())
    screen.blit(red, mouse())
    pygame.display.flip()