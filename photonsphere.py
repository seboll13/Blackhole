from vector import Vector
from blackhole import Blackhole
from libraries import pygame, ORANGE, rs

class PhotonSphere():
    def __init__(self, v: Vector, blackhole: Blackhole):
        self.v = v
        self.radius = 1.5*rs
    
    def draw(self, screen):
        pygame.draw.circle(screen, ORANGE, (self.v.x, self.v.y), self.radius+5, width=10)