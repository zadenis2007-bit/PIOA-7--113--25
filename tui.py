from database import Database


db = Database()
db.create_table("students")


def main():
  table = db.get_table("students")

  while True:
    print("\n=== MENU ===")
    print("1 - Add student")
    print("2 - Show all")
    print("3 - Filter by name")
    print("4 - Update by ID")
    print("5 - Delete by ID")
    print("0 - Exit")

    choice = input("Choice: ")

    if choice == "1":
      name = input("Name: ").strip()

      if not name:
        print("Name cannot be empty")
        continue

      try:
        age = int(input("Age: "))

        if age <= 0:
          print("Age must be positive")
          continue

      except ValueError:
        print("Age must be a number")
        continue

      table.add({
          "name": name,
          "age": age
      })

      print("Added")

  elif choice == "2":
    print(table.get_all())

  elif choice == "3":
    name = input("Name: ")
    print(table.filter(name=name))

  elif choice == "4":
    try:
      id_ = int(input("ID: "))
    except ValueError:
      print("ID must be a number")
      continue

    name = input("New name: ")
    age = input("New age: ")

    ok = table.update(
      id_,
      {
        "name": name,
        "age": age
      }
    )

    print("Updated" if ok else "Not found")

  elif choice == "5":
    try:
      id_ = int(input("ID: "))
    except ValueError:
      print("ID must be a number")
      continue

    ok = table.delete(id_)

    print("Deleted" if ok else "Not found")

  elif choice == "0":
    break

  else:
    print("Wrong input")
