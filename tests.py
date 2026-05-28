import os
import unittest
from file_table import FileTable


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
    self.table.add({
      "name": "Denis",
      "age": 18
    })

    self.assertEqual(len(self.table.data), 1)
    self.assertEqual(self.table.data[0]["name"], "Denis")
    self.assertEqual(self.table.data[0]["id"], 1)

  def test_get_all(self):
    self.table.add({"name": "A", "age": 10})
    self.table.add({"name": "B", "age": 20})

    result = self.table.get_all()

    self.assertEqual(len(result), 2)

  def test_filter_found(self):
    self.table.add({"name": "Denis", "age": 18})
    self.table.add({"name": "Alex", "age": 20})

    result = self.table.filter("Denis")

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0]["name"], "Denis")

  def test_filter_not_found(self):
    self.table.add({"name": "Alex", "age": 20})

    result = self.table.filter("Denis")

    self.assertEqual(result, [])

  def test_update_success(self):
    self.table.add({"name": "Old", "age": 10})

    updated = self.table.update(1, "New", 20)

    self.assertTrue(updated)

    result = self.table.get_all()

    self.assertEqual(result[0]["name"], "New")
    self.assertEqual(result[0]["age"], 20)

  def test_update_fail(self):
    updated = self.table.update(999, "Ghost", 99)

    self.assertFalse(updated)

  def test_delete_success(self):
    self.table.add({"name": "Delete", "age": 10})

    deleted = self.table.delete(1)

    self.assertTrue(deleted)
    self.assertEqual(len(self.table.data), 0)

  def test_delete_fail(self):
    deleted = self.table.delete(999)

    self.assertFalse(deleted)

  def test_save_and_load(self):
    self.table.add({"name": "Saved", "age": 30})

    new_table = FileTable(self.TEST_FILE)

    self.assertEqual(len(new_table.data), 1)
    self.assertEqual(new_table.data[0]["name"], "Saved")

  def test_next_id_increment(self):
    self.table.add({"name": "A", "age": 1})
    self.table.add({"name": "B", "age": 2})

    self.assertEqual(self.table.next_id, 3)

  def test_sort_by_age(self):
    self.table.add({"name": "A", "age": 30})
    self.table.add({"name": "B", "age": 20})

    result = self.table.sort_by("age")

    self.assertEqual(result[0]["age"], 20)

  def test_sort_by_age_reverse(self):
    self.table.add({"name": "A", "age": 30})
    self.table.add({"name": "B", "age": 20})

    result = self.table.sort_by("age", reverse=True)

    self.assertEqual(result[0]["age"], 30)

  def test_empty_table(self):
    result = self.table.get_all()

    self.assertEqual(result, [])

  def test_load_invalid_json(self):
    with open(self.TEST_FILE, "w", encoding="utf-8") as f:
      f.write("INVALID JSON")

    table = FileTable(self.TEST_FILE)

    self.assertEqual(table.data, [])
    self.assertEqual(table.next_id, 1)

  def test_file_created(self):
    self.table.add({"name": "File", "age": 1})

    self.assertTrue(os.path.exists(self.TEST_FILE))


if __name__ == "__main__":
  unittest.main()
