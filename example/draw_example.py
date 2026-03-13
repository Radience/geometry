from geometry.core import Point, Segment
from geometry.shapes import Polygon
from .plt_draw import draw_segment, setup_plot, show_plot, draw_polygon

p1 = Point(1.3,1)
p2 = Point(1.3,3.7)
p3 = Point(4.5,2.7)

setup_plot()

#polygon
plg = Polygon([p1,p2,p3])
draw_polygon(plg)

print(p1.distance_to(p3))
show_plot()