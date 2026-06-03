class Table:
  def __init__(self):
    self.data = []
    self.next_id = 1

  def add(self, record):
    record["id"] = self.next_id
    self.next_id += 1
    self.data.append(record)

  def get_all(self):
    return [record.copy() for record in self.data]

  def filter(self, **kwargs):
    result = self.data

    for key, value in kwargs.items():
      result = [
        record
        for record in result
        if str(record.get(key)) == str(value)
      ]

    return result

  def update(self, record_id, new_data):
    for record in self.data:
      if record["id"] == record_id:
        record.update(new_data)
        return True

    return False

  def delete(self, record_id):
    before = len(self.data)

  self.data = [
    record
    for record in self.data
    if record["id"] != record_id
  ]

  return len(self.data) != before


class Database:
  def __init__(self):
    self.tables = {}

  def create_table(self, name):
    self.tables[name] = Table()

  def get_table(self, name):
    return self.tables.get(name)
