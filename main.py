from libraries import pygame
from vector import Vector
from libraries import pygame, sys, WIDTH, HEIGHT, FPS, BLACK, M, rs
from blackhole import Blackhole
from photonsphere import PhotonSphere
from accretiondisk import AccretionDisk
from particles import Particles

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blackhole Animation")
    clock = pygame.time.Clock()
    
    # fixed objects
    blackhole = Blackhole(Vector(WIDTH/2, HEIGHT/2), M)
    photon_beam = PhotonSphere(Vector(WIDTH/2, HEIGHT/2), blackhole)
    accretion_disk = AccretionDisk(Vector(WIDTH/2, HEIGHT/2), blackhole)
    
    # moving objects
    particles = []
    start, end = int(HEIGHT/2 - rs*2.6), int(HEIGHT/2)
    for y in range(start, end, 10):
        particles.append(Particles(Vector(WIDTH-20, y)))
    
    running = True
    while running:
        dt = clock.tick(FPS)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #screen.fill(BLACK)
        
        # draw fixed objects
        blackhole.draw(screen)
        photon_beam.draw(screen)
        accretion_disk.draw(screen)

        # update position of particles according to physics
        for particle in particles:
            # compute acceleration of particle
            a = particle.get_acceleration(blackhole)
            #blackhole.pull(particle)
            particle.update(a, dt)
            particle.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
