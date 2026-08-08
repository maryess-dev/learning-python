n = int(input('Введите длительность цикла:'))
zero_counter = 0

for i in range(n):
  number = int(input())
  if number == 0: 
    zero_counter+= 1

print('Количество нулей:',zero_counter)
