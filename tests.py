import os
import unittest
from database import FileTable


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

  def test_insert(self):
    self.table.insert({"name": "Denis", "age": 18})

    self.assertEqual(len(self.table.data), 1)
    self.assertEqual(self.table.data[0]["name"], "Denis")
    self.assertEqual(self.table.data[0]["id"], 1)

  def test_select_all(self):
    self.table.insert({"name": "A"})
    self.table.insert({"name": "B"})

    result = self.table.select_all()

    self.assertEqual(len(result), 2)

  def test_select_by_id(self):
    self.table.insert({"name": "Test"})

    result = self.table.select_by_id(1)

    self.assertIsNotNone(result)
    self.assertEqual(result["name"], "Test")

  def test_select_by_invalid_id(self):
    result = self.table.select_by_id(999)

    self.assertIsNone(result)

  def test_update(self):
    self.table.insert({"name": "Old"})

    updated = self.table.update(1, {"name": "New"})

    self.assertTrue(updated)

    result = self.table.select_by_id(1)
    self.assertEqual(result["name"], "New")

  def test_update_invalid_id(self):
    updated = self.table.update(999, {"name": "Ghost"})

    self.assertFalse(updated)

  def test_delete(self):
    self.table.insert({"name": "DeleteMe"})

    deleted = self.table.delete(1)

    self.assertTrue(deleted)
    self.assertEqual(len(self.table.data), 0)

  def test_delete_invalid_id(self):
    deleted = self.table.delete(999)

    self.assertFalse(deleted)

  def test_save_and_load(self):
    self.table.insert({"name": "Saved"})

    new_table = FileTable(self.TEST_FILE)

    self.assertEqual(len(new_table.data), 1)
    self.assertEqual(new_table.data[0]["name"], "Saved")

  def test_next_id_increment(self):
    self.table.insert({"name": "A"})
    self.table.insert({"name": "B"})

    self.assertEqual(self.table.next_id, 3)

  def test_empty_table(self):
    result = self.table.select_all()

    self.assertEqual(result, [])

  def test_load_nonexistent_file(self):
    if os.path.exists("temp.json"):
      os.remove("temp.json")

    table = FileTable("temp.json")

    self.assertEqual(table.data, [])
    self.assertEqual(table.next_id, 1)

    if os.path.exists("temp.json"):
      os.remove("temp.json")

  def test_delete_then_select(self):
    self.table.insert({"name": "Test"})
    self.table.delete(1)

    result = self.table.select_by_id(1)

    self.assertIsNone(result)

  def test_update_persists_after_reload(self):
    self.table.insert({"name": "Old"})
    self.table.update(1, {"name": "New"})

    new_table = FileTable(self.TEST_FILE)

    result = new_table.select_by_id(1)

    self.assertEqual(result["name"], "New")

  def test_delete_persists_after_reload(self):
    self.table.insert({"name": "Delete"})
    self.table.delete(1)

    new_table = FileTable(self.TEST_FILE)

    self.assertEqual(len(new_table.data), 0)

  def test_multiple_inserts_ids(self):
    self.table.insert({"name": "A"})
    self.table.insert({"name": "B"})
    self.table.insert({"name": "C"})

    self.assertEqual(self.table.data[0]["id"], 1)
    self.assertEqual(self.table.data[1]["id"], 2)
    self.assertEqual(self.table.data[2]["id"], 3)

  def test_insert_empty_data(self):
    self.table.insert({})

    result = self.table.select_by_id(1)

    self.assertEqual(result["id"], 1)

  def test_load_invalid_json(self):
    with open(self.TEST_FILE, "w", encoding="utf-8") as f:
      f.write("INVALID JSON")

    table = FileTable(self.TEST_FILE)

    self.assertEqual(table.data, [])

  def test_save_creates_file(self):
    self.table.insert({"name": "FileTest"})

    self.assertTrue(os.path.exists(self.TEST_FILE))


if __name__ == "__main__":
  unittest.main()
