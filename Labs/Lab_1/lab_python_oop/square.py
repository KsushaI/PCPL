from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
  name = "Квадрат"
  def __init__(self, side, color):
      self.side = side
      super().__init__(self.side, self.side, color)
  def area(self):
      return self.side**2
  def __repr__(self):
    return '{} {} цвета со стороной {} и площадью {}.'.format(
      self.Get_name(),
      self.color.Get_color(),
      self.side,
      self.area()
  )
