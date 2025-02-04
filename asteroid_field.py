import pygame
import random
from asteroids import Asteroid
from constants import *
from ball import Ball
import random


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * (SCREEN_HEIGHT / 3)),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * (SCREEN_HEIGHT / 3)
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, (SCREEN_HEIGHT / 3) + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity, image):
        asteroid = Ball(position.x, position.y, random.randint(8,20))
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            if kind == 3:
                image = pygame.image.load('sprites/asteroid_160.png').convert_alpha()
            if kind == 2:
                image = pygame.image.load('sprites/asteroid_90.png').convert_alpha()
            if kind == 1:
                image = pygame.image.load('sprites/asteroid_60.png').convert_alpha()
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity, image)