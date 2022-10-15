from libraries import pygame, WHITE, G, c, rs, scaling_factor
from vector import Vector

class Blackhole():
    def __init__(self, v: Vector, mass):
        self.v = v
        self.mass = mass
        print("Schwarzschild radius: ", rs)
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.v.x, self.v.y), rs)

    def pull(self, photon):
        force = Vector(self.v.x - photon.pos.x, self.v.y - photon.pos.y)
        r = force.get_magnitude()
        fg = G*self.mass/r**2
        # add velocity to object
        force.set_magnitude(fg)
        photon.pos += force
        # limit photon to light speed
        if photon.velocity.get_magnitude() > c:
            photon.velocity.set_magnitude(c)