 #? Задание
 # В первой строке вводится число N. 
 # Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. 
 # Все числа по модулю не превышают 10e5. 
 # Переверните массив чисел. 
 # Выведите N чисел - перевернутый массив. 

num = int(input())

numbers = []

for _ in range(num):
  new_number = int(input())
  numbers.append(new_number)

numbers.reverse()

result = ",".join(map(str, numbers))
print(result)

