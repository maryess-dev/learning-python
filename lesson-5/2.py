word = input('Введите слово: ')
vowels = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]
count = 0
for w in vowels:
  if w in word:
    count+=1
 
print('Количество гласных:', count)
 