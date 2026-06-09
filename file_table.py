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
                
            if not isinstance(content, dict):
                raise ValueError("Invalid file structure")

            if "data" not in content or "next_id" not in content:
                raise ValueError("Missing required fields")

            if not isinstance(content["data"], list):
                raise ValueError("'data' must be a list")

            if not isinstance(content["next_id"], int):
                raise ValueError("'next_id' must be an integer")

            if content["next_id"] < 1:
                raise ValueError("'next_id' must be positive")

            for record in content["data"]:
                if not isinstance(record, dict):
                    raise ValueError("Invalid record format")

                required_fields = ["id", "name", "age"]

                for field in required_fields:
                    if field not in record:
                        raise ValueError(f"Missing field: {field}")

                if not isinstance(record["id"], int):
                    raise ValueError("Invalid id")

                if not isinstance(record["name"], str):
                    raise ValueError("Invalid name")

                if not record["name"].strip():
                    raise ValueError("Name cannot be empty")

                if not isinstance(record["age"], int):
                    raise ValueError("Invalid age")

                if record["age"] < 0:
                    raise ValueError("Age must be positive")
           
            self.data = content["data"]
            self.next_id = content["next_id"]
                    
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
        if "name" not in record:
            raise ValueError("Missing field: name")

        if "age" not in record:
            raise ValueError("Missing field: age")

        if not isinstance(record["name"], str):
            raise ValueError("Name must be string")

        if not record["name"].strip():
            raise ValueError("Name connot be empty")

        if not isinstance(record["age"], int):
            raise ValueError("Age must be integer")

        if record["age"] < 0:
            raise ValueError("Age must be positive")

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

        if not isinstance(name, str):
            raise ValueError("Name must be string")

        if not name.strip():
            raise ValueError("Name cannot be empty")

        if not isinstance(age, int):
            raise ValueError("Age must be integer")

        if age < 0:
            raise ValueError("Age must be positive")

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
