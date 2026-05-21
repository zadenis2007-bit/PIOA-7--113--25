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
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    content = json.load(f)
                    self.data = content.get("data", [])
                    self.next_id = content.get("next_id", 1)
            except Exception:
                self.data = []
                self.next_id = 1

    def save(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump({
                    "data": self.data,
                    "next_id": self.next_id
                }, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print("File error:", e)

    def add(self, record):
        record["id"] = self.next_id
        self.next_id += 1
        self.data.append(record)
        self.save()

    def get_all(self):
        return self.data

    def filter(self, name):
        return [r for r in self.data if r["name"] == name]

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
        return sorted(self.data, key=lambda x: x[field], reverse=reverse)