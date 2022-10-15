class Vector:
    """Simplified vector class for getting the position of particles"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    
    def get_magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def set_magnitude(self, magnitude):
        self.x *= magnitude / self.get_magnitude()
        self.y *= magnitude / self.get_magnitude()