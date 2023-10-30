import pygame
import sys

import pygame.event

pygame.init()



main_screen = pygame.display.set_mode((1024, 700))

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()



