import pygame, sys
from pygame.locals import *

pygame.init()

size = width, height = 1920, 1080
speed = [2,2]
black = 0, 0, 0
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

ball = pygame.image.load('intro_ball.gif')
ballrect = ball.get_rect()

square = pygame.Surface(size=(20, 20), flags=0)
squarerect = square.fill((250, 0, 0))

while 1:
    dirty_rect = []
    clock.tick(150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            sys.exit()

    dirty_rect.append(ballrect)
    dirty_rect.append(squarerect)
    squarerect = squarerect.move(speed)
    ballrect = ballrect.move(speed)
    dirty_rect.append(ballrect)
    dirty_rect.append(squarerect)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(square, squarerect)
    screen.blit(ball, ballrect)
    pygame.display.update(dirty_rect)