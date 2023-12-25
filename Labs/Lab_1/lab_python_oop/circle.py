from math import *
from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.Color import Color

class Circle(GeometricFigure):
  name = "Круг"
  def __init__(self, radius, color):
      self.radius = radius
      self.color = Color(color)
  def area(self):
      return round(self.radius**2 * pi, 3)
  def Get_name(self):
    return self.name
  def __repr__(self):
    return '{} {} цвета радиусом {} и площадью {}.'.format(
      self.Get_name(),
      self.color.Get_color(),
      self.radius,
      self.area()
  )