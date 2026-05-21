class Table:
    def __init__(self):
        self.data = []
        self.next_id = 1

    def add(self, record):
        record["id"] = self.next_id
        self.next_id += 1
        self.data.append(record)

    def get_all(self):
        return self.data

    def filter(self, name):
        result = []

        for record in self.data:
            if record["name"] == name:
                result.append(record)

        return result

    def update(self, record_id, name, age):
        for record in self.data:
            if record["id"] == record_id:
                record["name"] = name
                record["age"] = age
                return True

        return False

    def delete(self, record_id):
        for record in self.data:
            if record["id"] == record_id:
                self.data.remove(record)
                return True

        return False


class Database:
    def __init__(self):
        self.table = Table()


db = Database()


while True:
    print("\n1 - Add")
    print("2 - Show all")
    print("3 - Find by name")
    print("4 - Update")
    print("5 - Delete")
    print("0 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")

        db.table.add({
            "name": name,
            "age": age
        })

        print("Added")

    elif choice == "2":
        print(db.table.get_all())

    elif choice == "3":
        name = input("Name: ")
        print(db.table.filter(name))

    elif choice == "4":
        record_id = int(input("ID: "))
        name = input("New name: ")
        age = input("New age: ")

        ok = db.table.update(record_id, name, age)

        if ok:
            print("Updated")
        else:
            print("Not found")

    elif choice == "5":
        record_id = int(input("ID: "))

        ok = db.table.delete(record_id)

        if ok:
            print("Deleted")
        else:
            print("Not found")

    elif choice == "0":
        break

    else:
        print("Wrong input")  
         