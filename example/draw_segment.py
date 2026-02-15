from core import Point, Segment
from viz.plt_draw import draw_segment, setup_plot, show_plot

p1 = Point(1,2)
p2 = Point(3,3)
p3 = Point(2,1)

s = Segment(p1, p2)

setup_plot()

draw_segment(s, color='green', linewidth=3, label=f'AB = {s.length()}')

show_plot()