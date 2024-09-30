import pygame
from constants import *
from circleshape2 import CircleShape2
import random

class Border(CircleShape2):
    def __init__(self, x, y, radius = BORDER_RADIUS, containers = ()):
        super().__init__(x, y, radius)
        self.width = 2
        self.timer = 0
        self.bordercolor = 'white'
        self.grow_radius = radius

    def update(self, dt):
        pass

    def draw(self, screen):
        pass

    def effect(self):
        self.bordercolor = COLORS[random.randint(0,len(COLORS)-1)]
        #self.bordercolor = COLORS[6]