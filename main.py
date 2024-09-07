import pygame
import random
from pygame.examples.aliens import SCREENRECT

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Тир")
icon = pygame.image.load("img/1620460.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_widht = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_widht)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



running = True
while running:
    pass


pygame.quit()