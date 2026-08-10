import random

matrix_1 = []
matrix_2 = []
matrix_3=[]
rows = int(input("Кол-во строк: "))
cols = int(input("Кол-во колонок: "))


for i in range(rows):
  row_1 = []
  row_2 = []
  for j in range(cols):
    row_1.append(random.randint(-100, 100))
    row_2.append(random.randint(-100, 100))
  matrix_1.append(row_1)
  matrix_2.append(row_2)

for i in range(rows):
  sum = []
  for j in range(cols):
    sum.append(matrix_1[i][j]+matrix_2[i][j])
  matrix_3.append(sum)

for row in matrix_3:
  print(row)
