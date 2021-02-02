import pygame
pygame.init()

pygame.display.init()
screen = pygame.display.set_mode(size=(1280, 720))
pygame.display.set_caption("Game_Project")
running = True

while running:

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False