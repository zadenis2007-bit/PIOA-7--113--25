from database import Database


class App:
    def __init__(self):
        print("1 - Memory database")
        print("2 - File database")

        choice = input("Choice: ")

        if choice == "1":
            self.db = Database(mode="memory")
            
        elif choice == "2":
            self.db = Database(mode="file")

        else:
            raise ValueError("Invalid database type")


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
                name = input("Name: ").strip()

                if not name:
                    print("Name cannot be empty")
                    continue

                try:
                    age = int(input("Age: "))

                    if age < 0:
                        print("Age must be positive")
                        continue

                except ValueError:
                    print("Age must be a number")
                    continue
                    
                self.db.table.add({
                    "name": name, 
                    "age": age
                })

            elif choice == "2":
                print(self.db.table.get_all())

            elif choice == "3":
                name = input("Name: ").strip()

                if not name:
                    print("Name cannot be empty")
                    continue
                    
                print(
                    self.db.table.filter(
                        name=name
                    )
                )
                
            elif choice == "4":

                try:
                    rid = int(input("ID: "))
                except ValueError:
                    print("ID must be a number")
                    continue

                name = input("Name: ").strip()

                if not name:
                    print("Name cannot be empty")
                    continue

                try:
                    age = int(input("Age: "))
                except ValueError:
                    print("Age must be a number")
                    continue

                if age < 0:
                    print("Age must be positive")
                    continue

                print(self.db.table.update(rid, name, age))
                
            elif choice == "5":
                try:
                    rid = int(input("ID: "))
                    print(self.db.table.delete(rid))
                    
                except ValueError:
                    print("ID must be a number")

            elif choice == "6":
                field = input("Field: ")
                order = input("asc/desc: ")

                reverse = (order == "desc")
                
                print(self.db.table.sort_by(field, reverse))

            elif choice == "0":
                break
                
            else:
                print("Wrong input")

if __name__ == "__main__":
    App().run()
