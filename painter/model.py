# TODO: Add code here
import math

import matplotlib.pyplot as plt

class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

class Circle:
    def __init__(self, center: Point, radius:float):
        self.radius: float= radius
        self.center: Point= center


    def area_circle(self)->float:
        Area = math.pi*(self.radius)**2
        return Area
    def Draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()
    def __str__(self):
        Circle
        return  f"with center at {self.x}, {self.y} and {self.radius} r:"
class triangle:
    def __init__(self, point1:Point, point2:Point, point3: Point):
        self.point1: Point= point1
        self.point2: Point= point2
        self.point3: Point= point3

    def area_triangle(self):


