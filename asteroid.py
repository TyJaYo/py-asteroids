import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius < ASTEROID_MIN_RADIUS:
      return
    angle = random.uniform(85, 95)
    new_velocity_1 = self.velocity.rotate(angle) * ASTEROID_BREAKOFF_SPEED
    new_velocity_2 = self.velocity.rotate(-angle) * ASTEROID_BREAKOFF_SPEED
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    new_position_1 = self.position + new_velocity_1.normalize() * new_radius
    new_position_2 = self.position + new_velocity_2.normalize() * new_radius
    asteroid_1 = Asteroid(new_position_1.x, new_position_1.y, new_radius)
    asteroid_2 = Asteroid(new_position_2.x, new_position_2.y, new_radius)
    asteroid_1.velocity = new_velocity_1
    asteroid_2.velocity = new_velocity_2

