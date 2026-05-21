from database import Database


class App:
    def __init__(self):
        self.db = Database()

    def run(self):
        while True:
            print("\n1 - Add")
            print("2 - Show all")
            print("3 - Find by name")
            print("4 - Update")
            print("5 - Delete")
            print("0 - Exit")
            print("6 - Sort")

            choice = input("Choice: ")

            if choice == "1":
                name = input("Name: ")
                age = input("Age: ")

                self.db.table.add({
                "name": name,
                "age": age
                })

                print("Added")

            elif choice == "2":
                print(self.db.table.get_all())

            elif choice == "3":
                name = input("Name: ")
                print(self.db.table.filter(name))

            elif choice == "4":
                record_id = int(input("ID: "))
                name = input("New name: ")
                age = input("New age: ")

                ok = self.db.table.update(record_id, name, age)
                print("Updated" if ok else "Not found")

            elif choice == "5":
                record_id = int(input("ID: "))
                ok = self.db.table.delete(record_id)
                print("Deleted" if ok else "Not found")

            elif choice == "6":
                field = input("Field (id/name/age): ")
                order = input("Order (asc/desc): ")

                reverse = order == "desc" 

                result = self.db.table.sort_by(field, reverse)
                print(result)       

            elif choice == "0":
                break

            else:
                print("Wrong input")


if __name__ == "__main__":
    App().run()