import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = updatable, drawable
  Asteroid.containers = updatable, drawable, asteroids
  AsteroidField.containers = updatable
  Shot.containers = updatable, drawable, shots

  clock = pygame.time.Clock()
  dt = 0
  player = Player(SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)
  AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print("Exiting asteroids!")
        pygame.quit()
        return

    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.collides_with(player):
        print("Game over!")
        pygame.quit()
        return
      for asteroid2 in asteroids:
        if asteroid != asteroid2 and asteroid.collides_with(asteroid2):
          # Rotate velocities to simulate a bounce
          asteroid.velocity = asteroid.velocity.rotate(45)
          asteroid2.velocity = asteroid2.velocity.rotate(45)

          # Move asteroids apart to prevent overlap
          move_distance = (asteroid.radius + asteroid2.radius) - (asteroid.position - asteroid2.position).length()

          asteroid.position += asteroid.velocity.normalize() * move_distance
          asteroid2.position += asteroid2.velocity.normalize() * move_distance
      for shot in shots:
        if asteroid.collides_with(shot):
          asteroid.split()
          shot.kill()

    screen.fill("black")

    for sprite in drawable:
      sprite.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
