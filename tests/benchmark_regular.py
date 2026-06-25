import time
import math
from geometry.core import Point
from geometry.shapes import Polygon
from geometry.algorithms.regular import convex_regular_validation

# --- Метод из интернета (Эталон) ---
def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def angle(a, b, c):
    ab = distance(a, b)
    bc = distance(b, c)
    ac = distance(a, c)
    if ab == 0 or bc == 0: return 0
    cos_val = (ab**2 + bc**2 - ac**2) / (2 * ab * bc)
    cos_val = max(-1, min(1, cos_val))
    return math.degrees(math.acos(cos_val))

def is_regular_polygon_classic(polygon: Polygon, tol=1e-6) -> bool:
    pts = [(p.x, p.y) for p in polygon.points]
    n = len(pts)
    side_lengths = [distance(pts[i], pts[(i + 1) % n]) for i in range(n)]
    if max(side_lengths) - min(side_lengths) > tol: return False
    angles = [angle(pts[i - 1], pts[i], pts[(i + 1) % n]) for i in range(n)]
    if max(angles) - min(angles) > tol: return False
    return True

# Генерация полигона для теста
N = 1000
radius = 10.0
test_points = [Point(radius * math.cos(2 * math.pi * i / N), 
                     radius * math.sin(2 * math.pi * i / N)) for i in range(N)]
poly = Polygon(test_points)

# Замер твоего метода
start = time.perf_counter()
res1 = convex_regular_validation(poly)
end1 = time.perf_counter() - start

# Замер классического метода
start = time.perf_counter()
res2 = is_regular_polygon_classic(poly)
end2 = time.perf_counter() - start

print(f"Результаты для N={N} вершин:")
print(f"1. Твой метод (дистанции): {end1:.6f} сек.")
print(f"2. Классический метод (углы): {end2:.6f} сек.")
print(f"Ускорение твоего метода: {end2/end1:.2f} раз.")