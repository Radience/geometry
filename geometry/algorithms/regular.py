from geometry.core import Point, Segment
from geometry.shapes import Polygon
from ..constants import EPSILON

def convex_regular_validation(polygon: Polygon):
    points = polygon.points
    segments = polygon.segments
    if len(points) % 2 != 0:
        for n in range(len(points)):
            p_n = points[n]
            p2 = points[(n + len(points)//2) % len(points)]
            p3 = points[(n + len(points)//2 + 1) % len(points)]
            dx1 = (p_n.x - p2.x)
            dx2 = (p_n.x - p3.x)
            dy1 = (p_n.y - p2.y)
            dy2 = (p_n.y - p3.y)
            l1 = (dx1**2 + dy1**2)
            l2 = (dx2**2 + dy2**2)
            if abs(l1 - l2) / max(abs(l1), abs(l2), 1.0) > EPSILON:
                print(f"P{n}, P{(n + len(points)//2) % len(points)}, P{(n + len(points)//2 + 1) % len(points)}, L1={l1}, L2={l2}")
                return False
    else:
        for n in range(len(points)):
            p_n = points[n]
            m_n_x = (p_n.x + points[(n+1) % len(points)].x) / 2
            m_n_y = (p_n.y + points[(n+1) % len(points)].y) / 2
            m_n = Point(m_n_x, m_n_y)
            p2 = points[(n + len(points)//2 + 1) % len(points)]
            p3 = points[(n + len(points)//2) % len(points)]
            p4 = points[(n + len(points)//2 - 1) % len(points)]
            
            dm_x1 = (m_n.x - p2.x)
            dm_x2 = (m_n.x - p3.x)
            dm_y1 = (m_n.y - p2.y)
            dm_y2 = (m_n.y - p3.y)
            lm1 = (dm_x1**2 + dm_y1**2)
            lm2 = (dm_x2**2 + dm_y2**2)

            dx1 = (p_n.x - p2.x)
            dx2 = (p_n.x - p4.x)
            dy1 = (p_n.y - p2.y)
            dy2 = (p_n.y - p4.y)
            l1 = (dx1**2 + dy1**2)
            l2 = (dx2**2 + dy2**2)

            if abs(l1 - l2) / max(abs(l1), abs(l2), 1.0) > EPSILON:
                print(f"P{n}, P{(n + len(points)//2 + 1) % len(points)}, P{(n + len(points)//2 - 1) % len(points)}, L1={l1}, L2={l2}")
                return False
            
            if abs(lm1 - lm2) / max(abs(lm1), abs(lm2), 1.0) > EPSILON:
                print(f"P{n}, M{m_n}, P{(n + len(points)//2 + 1) % len(points)}, P{(n + len(points)//2) % len(points)}, Lm1={lm1}, Lm2={lm2}")
                return False
    return True