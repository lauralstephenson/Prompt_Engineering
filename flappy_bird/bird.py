import math
import pygame as pg
from math import sin, cos

class Bird(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('bird.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.acceleration = 2
        self.velocity = 0
        self.angle = 0

    def apply_gravity(self):
        # Gravity pulls the bird downwards
        self.velocity += self.acceleration
        self.rect.y += self.velocity

    def jump(self):
        # Bird jumps when the user clicks or presses spacebar
        self.velocity = -10
        self.angle = math.pi / 4

    def update(self, ground_height):
        # Update bird's position and apply physics
        self.apply_gravity()

        # Prevent the bird from going out of screen boundaries
        if self.rect.bottom > ground_height:
            self.rect.bottom = ground_height
        elif self.rect.top <= 0:
            self.rect.top = 0

        # Rotate the bird image based on its angle
        rotated_image = pg.transform.rotate(self.image, -self.angle)
        self.image = rotated_image