word = input('Введите слово: ')
vowels = ['a', 'e', 'i', 'o', 'u']


count = 0
for v in vowels:
    count_v = word.count(v)
    if count_v > 0:
        print(f"Буква '{v}': {count_v}")
        count += count_v 
    else:
        print(f"Буква '{v}': False")
print('Количество гласных:', count)
 