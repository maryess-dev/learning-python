num = int(input())
result = []
def find_factorial(number):
  if number < 0:
      print('Число должно быть положительным')
  factorial = 1
  for i in range(1,number + 1,1):
    factorial*= i
    result.append(factorial)

  result.sort(reverse=True)
  print(result)
find_factorial(num)