import matplotlib.pyplot as plt
from geometry.core import Segment
from geometry.shapes import Polygon

def draw_segment(segment: Segment, color='blue', linewidth=2, label=None):
    x_coords = [segment.start.x, segment.end.x]
    y_coords = [segment.start.y, segment.end.y]
    plt.plot(x_coords, y_coords, 
             color=color, 
             linewidth=linewidth,
             label=label)
    plt.plot(segment.start.x, segment.start.y, 'ro', markersize=4)
    plt.plot(segment.end.x, segment.end.y, 'ro', markersize=4)

def draw_polygon(plg: Polygon):
    for sgm in plg.segments:
        draw_segment(sgm)

def setup_plot():
    plt.figure(figsize=(8,8))
    plt.title('Geometry')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)

def show_plot():
    plt.legend()
    plt.show()