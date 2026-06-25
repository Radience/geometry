from geometry.core import Point, Segment
from geometry.shapes import Polygon
from ..constants import EPSILON

def convex_regular_validation(polygon: Polygon):
    points = polygon.points
    segments = polygon.segments
    len_p = len(points)
    if len_p % 2 != 0:
        for n in range(len_p):
            p_n = points[n]
            p2 = points[(n + len_p//2) % len_p]
            p3 = points[(n + len_p//2 + 1) % len_p]
            dx1 = (p_n.x - p2.x)
            dx2 = (p_n.x - p3.x)
            dy1 = (p_n.y - p2.y)
            dy2 = (p_n.y - p3.y)
            l1 = (dx1**2 + dy1**2)
            l2 = (dx2**2 + dy2**2)
            if abs(l1 - l2) / max(abs(l1), abs(l2), 1.0) > EPSILON:
                #print(f"P{n}, P{(n + len_p//2) % len_p}, P{(n + len_p//2 + 1) % len_p}, L1={l1}, L2={l2}")
                return False
    else:
        for n in range(len_p):
            p_n = points[n]
            m_n_x = (p_n.x + points[(n+1) % len_p].x) / 2
            m_n_y = (p_n.y + points[(n+1) % len_p].y) / 2
            p2 = points[(n + len_p//2 + 1) % len_p]
            p3 = points[(n + len_p//2) % len_p]
            p4 = points[(n + len_p//2 - 1) % len_p]
            
            dm_x1 = (m_n_x - p2.x)
            dm_x2 = (m_n_x - p3.x)
            dm_y1 = (m_n_y - p2.y)
            dm_y2 = (m_n_y - p3.y)
            lm1 = (dm_x1**2 + dm_y1**2)
            lm2 = (dm_x2**2 + dm_y2**2)

            dx1 = (p_n.x - p2.x)
            dx2 = (p_n.x - p4.x)
            dy1 = (p_n.y - p2.y)
            dy2 = (p_n.y - p4.y)
            l1 = (dx1**2 + dy1**2)
            l2 = (dx2**2 + dy2**2)

            if abs(l1 - l2) / max(abs(l1), abs(l2), 1.0) > EPSILON:
                #print(f"P{n}, P{(n + len_p//2 + 1) % len_p}, P{(n + len_p//2 - 1) % len_p}, L1={l1}, L2={l2}")
                return False
            
            if abs(lm1 - lm2) / max(abs(lm1), abs(lm2), 1.0) > EPSILON:
                #print(f"P{n}, M{m_n}, P{(n + len_p//2 + 1) % len_p}, P{(n + len_p//2) % len_p}, Lm1={lm1}, Lm2={lm2}")
                return False
    return True