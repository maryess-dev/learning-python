animal_type = input("Введите вид питомца: ")
animal_age = int(input("Введите возраст питомца: "))
animal_name = input("Введите кличку питомца: ")
client_name = input("Введите ваше имя: ")
pets = dict()

if animal_name:
  pets[animal_name] = {
    "Вид питомца": animal_type,
    "Возраст питомца": animal_age,
    "Имя владельца": client_name 
  }

suffix = ""

if animal_age%10==0 or animal_age%10>4 or animal_age%100>10 and animal_age%100<20 :
  suffix = "лет"
if animal_age%10==1:
  suffix = "год"
if animal_age%10>1 and animal_age%10<5:
  suffix="года"

print(f'Это {pets.get(animal_name, {}).get("Вид питомца")} по кличке "{animal_name}". Возраст питомца: {pets.get(animal_name, {}).get("Возраст питомца")} {suffix}. Имя владельца: {pets.get(animal_name, {}).get("Имя владельца")}')
