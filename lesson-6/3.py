a = int(input('Введите a:'))
b = int(input('Введите b:'))

for i in range(a, b + 1):
  if i % 2 == 0:
    print(i, end=" ")
