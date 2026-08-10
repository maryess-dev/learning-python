class Transport:
   def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

class Autobus(Transport):
  def info(self):
    print(f"Название атомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

bus = Autobus("Renault Logan", 180, 12)
bus.info()