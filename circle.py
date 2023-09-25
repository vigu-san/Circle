import math


class Circle():

    def __init__(self, r):
        self.radius = r

    def area(self):
        area = self.radius**2*math.pi
    
    def circumference(self):
        circumference = 2*math.pi*self.radius

