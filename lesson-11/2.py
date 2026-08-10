import collections

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}

def create():
  last = collections.deque(pets, maxlen=1)[0]
  animal_type = input("Введите вид питомца: ")
  animal_age = int(input("Введите возраст питомца: "))
  animal_name = input("Введите кличку питомца: ")
  client_name = input("Введите ваше имя: ")
  pets[last + 1] = {
    animal_name: {
    "Вид питомца": animal_type,
    "Возраст питомца": animal_age,
    "Имя владельца": client_name 
  }
}

def get_pet(ID):
  return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
  if age%10==0 or age%10>4 or age%100>10 and age%100<20 :
    return "лет"
  if age%10==1:
    return "год"
  if age%10>1 and age%10<5:
    return "года" 

def pets_list():
  for pet_id, pet_info in pets.items():
    for name, details in pet_info.items():
      age = details["Возраст питомца"]
      suffix = get_suffix(age)
      print(
        f'ID: {pet_id} | Это {details["Вид питомца"]} по кличке "{name}". '
        f'Возраст питомца: {age} {suffix}. Владелец: {details["Имя владельца"]}'
      )


command = "start"

while command != "stop":
  command = input(
  "\nВведите команду (create - создать, get - получить по ID, list - список, stop - выйти): ").strip().lower()

  if command == 'create': 
    { create()}
  elif command == "get":
    pet_id = int(input("Введите ID питомца: "))
    pet = get_pet(pet_id)
    if pet:
      for name, details in pet.items():
        age = details["Возраст питомца"]
        print(
          f'Это {details["Вид питомца"]} по кличке "{name}". '
          f'Возраст питомца: {age} {get_suffix(age)}. Владелец: {details["Имя владельца"]}'
        )
    else:
      print("Питомец с таким ID не найден.")
  if command == "list": 
    pets_list()


