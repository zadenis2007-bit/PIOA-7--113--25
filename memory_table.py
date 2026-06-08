from storage import BaseTable


class MemoryTable(BaseTable):
    def __init__(self):
        self.data = []
        self.next_id = 1

    def add(self, record):
        if "name" not in record:
            raise ValueError("Missing field: name")

        if not record["name"].strip():
            raise ValueError("Name connot be empty")

        if "age" not in record:
            raise ValueError("Missing field: age")

        if not isinstance(record["name"], str):
            raise ValueError("Name must be string")

        if not isinstance(record["age"], int):
            raise ValueError("Age must be integer")

        if record["age"] < 0:
            raise ValueError("Age must be positive")
            
        record["id"] = self.next_id
        self.next_id += 1
        self.data.append(record)

    def get_all(self):
        return [r.copy() for r in self.data]

    def filter(self, **filters):
        result = []

        for record in self.data:
            if all(record.get(key) == value
                   for key, value in filters.items()):
                result.append(record.copy())

        return result

    def update(self, record_id, name, age):
        for r in self.data:
            if r["id"] == record_id:
                r["name"] = name
                r["age"] = age
                return True

        return False

    def delete(self, record_id):
        for r in self.data:
            if r["id"] == record_id:
                self.data.remove(r)
                return True

        return False

    def sort_by(self, field, reverse=False):
        if not self.data:
            return []

        if field not in self.data[0]:
            return []

        return sorted(
            self.data,
            key=lambda x: x[field],
            reverse=reverse
        )
