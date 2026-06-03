def add(self, record):
    record["id"] = self.next_id
    self.next_id += 1
    self.data.append(record)

def get_all(self):
    return [record.copy() for record in self.data]

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
