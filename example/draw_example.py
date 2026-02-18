from core import Point, Segment
from shapes import Polygon
from viz.plt_draw import draw_segment, setup_plot, show_plot, draw_polygon

p1 = Point(1.5,1)
p2 = Point(1,2)
p3 = Point(1.5,3)
p4 = Point(2.5,3)
p5 = Point(3,2)
p6 = Point(2.5,1)
p_s_1 = Point(1,1)
p_s_2 = Point(4,4)

setup_plot()

#segment
sgm = Segment(p_s_1, p_s_2)
draw_segment(sgm, color='red')

#polygon
plg = Polygon([p1,p2,p3,p4,p5,p6])
draw_polygon(plg)

show_plot()