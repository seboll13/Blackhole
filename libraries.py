import pygame
import sys

# COLORS
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
GRAY   = (192, 192, 192)
ORANGE = (255, 128, 0)
RED    = (255, 0, 0)

# GAME CONSTANTS
WIDTH = 800
HEIGHT = 600
FPS = 60

# REAL PHYSICS CONSTANTS
scaling_factor = 1e-7
G = scaling_factor*6.67408e-11  # gravitational constant
c = scaling_factor*299792458    # speed of light
M = scaling_factor*26*1e-3*1.989e30 # mass of the blackhole
rs = 2*G*M/c**2