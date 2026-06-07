import json
import os
from storage import BaseTable


class FileTable(BaseTable):
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = []
        self.next_id = 1
        self.load()

    def load(self):
        if not os.path.exists(self.filename):
            return
            
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = json.load(f)
                    
            self.data = content.get("data", [])
            self.next_id = content.get("next_id", 1)
                    
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Invalid JSON format in file '{self.filename}'"
            ) from e

        except OSError as e:
            raise OSError(
                f"Cannot open file '{self.filename}'"
            ) from e    


    def save(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump({
                    "data": self.data,
                    "next_id": self.next_id
                }, f, indent=4, ensure_ascii=False)
        except OSError as e:
            raise OSError(
                f"Cannot save file '{self.filename}'"
            ) from e

    def add(self, record):
        record["id"] = self.next_id
        self.next_id += 1
        self.data.append(record)
        self.save()

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
                self.save()
                return True
        return False

    def delete(self, record_id):
        for r in self.data:
            if r["id"] == record_id:
                self.data.remove(r)
                self.save()
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
