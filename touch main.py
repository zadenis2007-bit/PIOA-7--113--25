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

def filter(self, **kwargs):
    result = self.data
    for key, value in kwargs.items():
        result = [r for r in result if str(r.get(key)) == str(value)]
    return result

def update(self, record_id, new_data):
    for r in self.data:
        if r["id"] == record_id:
            r.update(new_data)
            return True
    return False

def delete(self, record_id):
    before = len(self.data)
    self.data = [r for r in self.data if r["id"] != record_id]
    return len(self.data) != before


class Database:
    def __init__(self):
        self.tables = {}

def create_table(self, name):
    self.tables[name] = Table()

def get_table(self, name):
    return self.tables.get(name)


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
            name = input("Name: ")
            age = input("Age: ")
            table.add({"name": name, "age": age})
            print("Added")

        elif choice == "2":
            print(table.get_all())

        elif choice == "3":
            name = input("Name: ")
            print(table.filter(name=name))

        elif choice == "4":
            id_ = int(input("ID: "))
            name = input("New name: ")
            age = input("New age: ")
            ok = table.update(id_, {"name": name, "age": age})
            print("Updated" if ok else "Not found")

        elif choice == "5":
            id_ = int(input("ID: "))
            ok = table.delete(id_)
            print("Deleted" if ok else "Not found")

        elif choice == "0":
            break

        else:
            print("Wrong input")


if __name__ == "__main__":
    main()
    