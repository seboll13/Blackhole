from libraries import pygame, GRAY, rs
from blackhole import Blackhole
from vector import Vector

class AccretionDisk():
    def __init__(self, v: Vector, blackhole: Blackhole):
        self.v = v
        self.radius = 3*rs
    
    def draw(self, screen):
        pygame.draw.circle(screen, GRAY, (self.v.x, self.v.y), self.radius+10, width=20)