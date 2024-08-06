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


    def area(self)->float:
        Area = math.pi*(self.radius)**2
        return Area
    def Draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()
    def __str__(self):
        Circle
        with center at (x, y) and radius r
        return  (f"{x}, {y}, {r}")

