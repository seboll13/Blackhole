from vector import Vector
from libraries import pygame, RED, G, c

class Particles():
    def __init__(self, pos: Vector):
        self.pos = pos
        self.radius = 3
        self.velocity = Vector(-c, 0)
    
    def update(self, a, dt):
        # update position
        self.pos.x += self.velocity.x*dt + 0.5*a.x*dt**2
        self.pos.y += self.velocity.y*dt + 0.5*a.y*dt**2
        # update velocity from acceleration
        self.velocity += a*dt
    
    def get_acceleration(self, blackhole):
        # compute acceleration of particle
        a = Vector(blackhole.v.x - self.pos.x, blackhole.v.y - self.pos.y)
        r = a.get_magnitude()
        fg = G*blackhole.mass/r**2
        # add velocity to object
        a.set_magnitude(fg)
        return a
    
    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.pos.x, self.pos.y), self.radius)