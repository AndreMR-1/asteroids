# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	asteroidfield = AsteroidField()
	
	center_x = SCREEN_WIDTH / 2
	center_y = SCREEN_HEIGHT / 2
	player = Player(center_x, center_y)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()
			
			for shot in shots:
				if shot.collides_with(asteroid):
					asteroid.kill()


		screen.fill(SCREEN_FILL)
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		#limit the framerate to 60 FPS
		dt = clock.tick(60) /1000


if __name__ == "__main__":
    main()


