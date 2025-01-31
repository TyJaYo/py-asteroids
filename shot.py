from asteroid import Asteroid
from constants import *

class Shot(Asteroid):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIUS)
