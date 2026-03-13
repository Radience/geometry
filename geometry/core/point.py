from ..constants import EPSILON

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, point: Point) -> float:
        dx = self.x - point.x
        dy = self.y - point.y
        return (dx**2 + dy**2)**0.5
    
    def __eq__(self, point: Point):
        if not isinstance(point, Point):
            return NotImplemented
        return (abs(self.x - point.x) < EPSILON and
                abs(self.y - point.y) < EPSILON)
    
    def __str__(self):
        return f'({self.x:.3f}, {self.y:.3f})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'