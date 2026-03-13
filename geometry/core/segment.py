from .point import Point

class Segment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def length(self):
        return self.start.distance_to(self.end)