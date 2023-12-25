from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.Color import Color

class Rectangle(GeometricFigure):
  name = "Прямоугольник"
  def __init__(self, width, height, color):
      self.width = width
      self.height = height
      self.color = Color(color)
  def area(self):
    return self.width * self.height
  def Get_name(self):
    return self.name
  def __repr__(self):
    return '{} {} цвета шириной {}, высотой {} и площадью {}.'.format(
        self.Get_name(),
        self.color.Get_color(),
        self.width,
        self.height,
        self.area()
    )