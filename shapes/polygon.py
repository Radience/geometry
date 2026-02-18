from core import Point, Segment

class Polygon:
    def __init__(self, points: List[Point]):
        self.points = points
        self.segments = self.get_segments(points)

    @staticmethod
    def get_segments(points: List[Point]) -> List[Segment]:
        segments = []
        n = len(points)
        for i in range(n): # 0,1,2,...
            segments.append(Segment(points[i], points[(i+1) % n])) # i={0,1,2,...} i+1={1,2,3,...} if i+1=n: i+1%n = 0 
        return segments