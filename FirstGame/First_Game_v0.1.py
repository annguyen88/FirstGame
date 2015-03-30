import pygame, sys
from pygame.locals import *
import random
import spritesheet

pygame.init()

display_width = 800
display_height = 600

# background color
white = (0, 0, 0)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Title of Game
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()

# back = pygame.Surface((640,480))

gameDisplay.fill(white)


print "hello"


# Creating the bars
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))

pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))


def event_key_press(self, key, char):
            if key == 'f8':
                print "hello"
                #sge.Sprite.from_screenshot().save('screenshot.jpg')
            elif key == 'f11':
                self.fullscreen = not self.fullscreen
            elif key == 'escape':
                self.event_close()
            elif key in ('p', 'enter'):
                self.pause()


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    gameExit = False

    while not gameExit:
        # Exit when ESC is pressed
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        # for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        pygame.quit()
        #        quit()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
