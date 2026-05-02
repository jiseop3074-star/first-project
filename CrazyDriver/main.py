import pygame
import sys
from pygame.locals import *
import os

print(__file__)
print(os.path.dirname(__file__))

GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER =  os.path.join(GAME_ROOT_FOLDER,"Images")

print("게임 루트:",GAME_ROOT_FOLDER)
print("이미지 폴더:",IMAGE_FOLDER)
Black = (0, 0, 0)
White = (255,255,255)
Red = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

pygame.display.set_caption("Crazy Driver")

screen = pygame.display.set_mode((500, 800))
screen.fill(White)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        

