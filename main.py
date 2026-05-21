from database import Database


class App:
    def __init__(self):
        self.db = Database(mode="file") # или memory

    def run(self):
        while True:
            print("\n1 - Add")
            print("2 - Show all")
            print("3 - Find")
            print("4 - Update")
            print("5 - Delete")
            print("6 - Sort")
            print("0 - Exit")

            choice = input("Choice: ")

            if choice == "1":
                name = input("Name: ")
                age = input("Age: ")
                self.db.table.add({"name": name, "age": age})

            elif choice == "2":
                print(self.db.table.get_all())

            elif choice == "3":
                name = input("Name: ")
                print(self.db.table.filter(name))

            elif choice == "4":
                try:
                    rid = int(input("ID: "))
                    name = input("Name: ")
                    age = input("Age: ")
                    print(self.db.table.update(rid, name, age))
                except:
                    print("Error")

            elif choice == "5":
                rid = int(input("ID: "))
                print(self.db.table.delete(rid))

            elif choice == "6":
                field = input("Field: ")
                order = input("asc/desc: ")
                print(self.db.table.sort_by(field, order == "desc"))

            elif choice == "0":
                break


if __name__ == "__main__":
    App().run()