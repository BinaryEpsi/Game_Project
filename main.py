import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode(size=(1280, 720))
pygame.display.set_caption("Game_Project")
running = True

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False


	pygame.display.flip()