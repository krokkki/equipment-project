equipment = [
  "Видеокамера",
  "Датчик движения",
  "Охранная сигнализация",
  "Контроллер доступа"
]


def show_equipment():
  print("\nСписок оборудования:")
  for i, item in enumerate(equipment, 1):
    print(f"{i}. {item}")


def add_equipment():
  item = input("Введите название оборудования: ")
  equipment.append(item)
  print("Оборудование добавлено.")


def find_equipment():
  search = input("Введите название для поиска: ").lower()

  found = []

  for item in equipment:
    if search in item.lower():
      found.append(item)

  if found:
    print("\nНайденное оборудование:")
    for item in found:
      print(f"- {item}")
  else:
    print("Оборудование не найдено.")


while True:
  print("\n=== Учет оборудования ООО «СИГНАЛ СБ» ===")
  print("1. Показать оборудование")
  print("2. Добавить оборудование")
  print("3. Найти оборудование")
  print("4. Выход")

  choice = input("Выберите действие: ")

  if choice == "1":
    show_equipment()
  elif choice == "2":
    add_equipment()
  elif choice == "3":
    find_equipment()
  elif choice == "4":
    break
  else:
    print("Неверный выбор.")
