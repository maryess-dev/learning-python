number = int(input('Введите число: '))

if number < 0 and number % 2 == 0:
  print('отрицательное четное число')
if( number > 0 and number % 2 == 0):
  print('положительное четное число')
if( number == 0):
  print('нулевое число')
if(number % 2 != 0 ):
  print('число не является четным')