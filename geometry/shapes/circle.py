from ..core import Point

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = abs(radius)