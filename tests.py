import os
import unittest
import json
from file_table import FileTable
from memory_table import MemoryTable
from database import Database


class TestFileTable(unittest.TestCase):

  TEST_FILE = "test_data.json"

  def setUp(self):
    self.table = FileTable(self.TEST_FILE)
    self.table.data = []
    self.table.next_id = 1
    self.table.save()

  def tearDown(self):
    if os.path.exists(self.TEST_FILE):
      os.remove(self.TEST_FILE)

  def test_add(self):
    self.table.add({"name": "Denis", "age": 18})
    self.assertEqual(len(self.table.data), 1)

  def test_get_all(self):
    self.table.add({"name": "A", "age": 10})
    self.table.add({"name": "B", "age": 20})
    self.assertEqual(len(self.table.get_all()), 2)

  def test_load_saved_file(self):
    self.table.add({"name": "Denis", "age": 18})

    new_table = FileTable(self.TEST_FILE)

    self.assertEqual(len(new_table.data), 1)
    self.assertEqual(new_table.data[0]["name"], "Denis")

  def test_invalid_json(self):
    with open(self.TEST_FILE, "w", encoding="utf-8") as f:
      f.write("invalid json")

    with self.assertRaises(ValueError):
      FileTable(self.TEST_FILE)

  def test_invalid_structure(self):
    with open(self.TEST_FILE, "w", encoding="utf-8") as f:
      json.dump({"wrong": "data"}, f)

    with self.assertRaises(ValueError):
      FileTable(self.TEST_FILE)

  def test_filter(self):
    self.table.add({"name": "Denis", "age": 18})
    result = self.table.filter(name="Denis")
    self.assertEqual(len(result), 1)

  def test_filter_multiple_fields(self):
    self.table.add({"name": "Denis", "age": 18})
    self.table.add({"name": "Denis", "age": 20})

    result = self.table.filter(
      name="Denis",
      age=18
    )

    self.assertEqual(len(result), 1)

  def test_update(self):
    self.table.add({"name": "Old", "age": 10})
    self.assertTrue(self.table.update(1, "New", 20))

  def test_delete(self):
    self.table.add({"name": "Del", "age": 10})
    self.assertTrue(self.table.delete(1))

  def test_sort(self):
    self.table.add({"name": "A", "age": 30})
    self.table.add({"name": "B", "age": 20})

    result = self.table.sort_by("age")
    self.assertEqual(result[0]["age"], 20)

  def test_sort_invalid_field(self):
    self.table.add({"name": "Denis", "age": 18})

    result = self.table.sort_by("salary")

    self.assertEqual(result, [])

class TestMemoryTable(unittest.TestCase):

  def setUp(self):
    self.table = MemoryTable()

  def test_add(self):
    self.table.add({"name": "A", "age": 1})
    self.assertEqual(len(self.table.get_all()), 1)

  def test_filter(self):
    self.table.add({"name": "Denis", "age": 18})
    self.assertEqual(len(self.table.filter(name="Denis")), 1)

  def test_update_success(self):
    self.table.add({"name": "Old", "age": 10})
    self.assertTrue(self.table.update(1, "New", 20))

  def test_update_fail(self):
    self.assertFalse(self.table.update(999, "X", 1))

  def test_delete_success(self):
    self.table.add({"name": "A", "age": 10})
    self.assertTrue(self.table.delete(1))

  def test_delete_fail(self):
    self.assertFalse(self.table.delete(999))

  def test_sort(self):
    self.table.add({"name": "A", "age": 30})
    self.table.add({"name": "B", "age": 20})

    result = self.table.sort_by("age")
    self.assertEqual(result[0]["age"], 20)

  def test_sort_invalid_field(self):
    self.table.add({"name": "Denis", "age": 18})

    result = self.table.sort_by("salary")

    self.assertEqual(result, [])


class TestDatabase(unittest.TestCase):

  def test_memory_mode(self):
    db = Database(mode="memory")
    self.assertEqual(type(db.table).__name__, "MemoryTable")

  def test_file_mode(self):
    db = Database(mode="file")
    self.assertEqual(type(db.table).__name__, "FileTable")
    
  def test_invalid_mode(self):
    with self.assertRaises(ValueError):
      Database(mode="invalid")

if __name__ == "__main__":
  unittest.main()
