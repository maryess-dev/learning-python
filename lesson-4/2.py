number = int(input())

str = str(number)

last_num = str[len(str) - 1]
pre_last_num = str[len(str) - 2]
middle_num = str[len(str) - 3]
second_num = str[len(str) - 4]
first_num = str[len(str) - 5]

step_1 = int(pre_last_num) ** int(last_num)
step_2 = step_1* int(middle_num)
step_3 = int(first_num) - int(second_num)
result = step_2/step_3

print(str)
print(result)