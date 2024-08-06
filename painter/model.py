# TODO: Add code here
import math
class Point:
    def __init__(self, x: float, y: float):
        self.x: float = 0
        self.y: float = 0

class Circulo:
    def __init__(self, center: Point, radius:float):
        self.radius: float= 0

    def area(self)->float:
        Area = math.pi*self.radius

