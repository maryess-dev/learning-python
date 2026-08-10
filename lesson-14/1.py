my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def recursion(list):
  # my_list.reverse()

  if not list:
    return;
  print(list[0])

  recursion(list[1:])

  if len(list) == 1:
    print('Конец списка')

recursion(my_list)

#! [0] -> вызов  с урезанием -> [1] -> [2] ...