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

        return  f"with center at {self.center.x}, {self.center.y} and {self.radius} r:"
class triangle:
    def __init__(self, point_1:Point, point_2:Point, point_3: Point):
        self.point_1: Point= point_1
        self.point_2: Point= point_2
        self.point_3: Point= point_3

    def area(self):
        area= 0.5 * abs((self.point_1.x * self.point_2.y - self.point_1.x * self.point_3.y) +
                        (self.point_2.x * self.point_3.y - self.point_2.x * self.point_1.y) +
                        (self.point_3.x * self.point_1.y - self.point_3.x * self.point_2.y))


    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()
    def __str__(self):
        return f"with vertices at {self.point_1.x}, {self.point_1.y}, {self.point_2.x}, {self.point_2.y} and {self.point_3.x}, {self.point_3.y}"


