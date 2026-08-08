min_invest_value = int(input('Введите минимальную сумму инвестиций: '))
mike_sum = int(input("Сколько долларов у Майкла: "))
ivan_sum = int(input('Соклько долларов у Ивана: '))

if(mike_sum >= min_invest_value and ivan_sum >= min_invest_value):
  print(2)
elif(mike_sum >= min_invest_value):
  print('Mike')
elif(ivan_sum >= min_invest_value):
  print('Ivan')
elif(mike_sum + ivan_sum >= min_invest_value):
  print(1)
elif(mike_sum <= min_invest_value and ivan_sum <= min_invest_value):
  print(0)

