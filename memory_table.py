from storage import BaseTable


class MemoryTable(BaseTable):
    def __init__(self):
        self.data = []
        self.next_id = 1

    def add(self, record):
        record["id"] = self.next_id
        self.next_id += 1
        self.data.append(record)

    def get_all(self):
        return [r.copy() for r in self.data]

    def filter(self, name):
        return [r for r in self.data if r["name"] == name]

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
        return sorted(self.data, key=lambda x: x[field], reverse=reverse)
