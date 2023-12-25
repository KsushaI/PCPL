from pprint import pp
def field(items, *args):
    assert len(args) > 0
    for c in items:
      if len(args) == 1:
        if c.get(args[0]) != None:
          print(c[args[0]], end=', ')
        else:
          continue
      else:
        new_dict = {}
        for arg in args:
          if c.get(arg) is not None:
            new_dict[arg] = c[arg]
        pp(new_dict)
        

goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'color': 'black'}
]
field(goods, 'title', 'price')
