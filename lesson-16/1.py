class CashRegister:
  def __init__(self, money):
    self.money = money

  def top_up(self, X):
    self.money+=X
    print(self.money)

  def count_1000(self):
    thousands = self.money // 1000
    print(thousands)
  

  def take_away(self, X):
    if self.money < X:
      print('Недостаточно денег')
    else:
      self.money-=X
      print(self.money)

cash = CashRegister(20000)

up = int(input("Введите сумму пополнения: "))
away = int(input("Введите сумма снятия: "))

cash.top_up(up)
cash.count_1000()
cash.take_away(away)

    
      
