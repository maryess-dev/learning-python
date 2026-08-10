class Turtles:
  def __init__(self, x,y,s):
    self.x = x
    self.y = y
    self.s = s 

  def go_up(self):
    self.y += self.s
    print(self.y)

  def do_down(self):
    self.y-=self.s
    print(self.y)

  def go_left(self):
    self.x-=self.s

  def go_right(self):
    self.x+=self.s

  def evolve(self):
    self.s += 1

  def degrade(self):
    if self.s <= 0:
      print('Ошибка')
    else: 
      self.x -=1

  def count_moves(self, x2, y2):
    start_x=self.x
    start_y=self.y
    count=0
    while self.y != y2 or self.x != x2:
      if self.x < x2:
        self.x= min(self.x + self.s, x2)
        count+=1
      elif self.x > x2:
        self.x = max(self.x - self.s, x2) 
        count += 1
      if self.y < y2:
        self.y = min(self.y + self.s, y2)
        count += 1
      elif self.y > y2:
        self.y = max(self.y - self.s, y2)
        count += 1
    print(f"Старт: ({start_x}, {start_y}) -> Финиш: ({x2}, {y2}) | Кол-во: {count}")


turtle = Turtles(2,2,4)

turtle.count_moves(5,5)
  