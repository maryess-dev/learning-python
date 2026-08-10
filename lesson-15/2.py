class Transport:
  def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

  def seating_capacity(self, capacity):
    return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):
  def seating_capacity(self, capacity=50):
    return super().seating_capacity(capacity)

  def __str__(self):
   return self.seating_capacity()

  def info(self):
    print(f"Название атомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

bus = Autobus("Renault Logan", 180, 12)

bus.info()
print(bus.seating_capacity()) 
