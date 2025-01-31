import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x, y, radius):
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()

    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)
    self.radius = radius

  def draw(self, _screen):
    # sub-classes must override
    pass

  def update(self, _dt):
    # sub-classes must override
    pass

  def collides_with(self, other):
    return (self.position - other.position).length() < self.radius + other.radius
