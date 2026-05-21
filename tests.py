import unittest
import os
from file_table import FileTable


class TestFileTable(unittest.TestCase):

    def setUp(self):
        self.file = "test.json"
        if os.path.exists(self.file):
            os.remove(self.file)
        self.table = FileTable(self.file)

    def test_add(self):
        self.table.add({"name": "A", "age": 20})
        self.assertEqual(len(self.table.get_all()), 1)

    def test_update(self):
        self.table.add({"name": "A", "age": 20})
        self.assertTrue(self.table.update(1, "B", 30))

    def test_delete(self):
        self.table.add({"name": "A", "age": 20})
        self.assertTrue(self.table.delete(1))

    def test_filter(self):
        self.table.add({"name": "A", "age": 20})
        self.assertEqual(len(self.table.filter("A")), 1)

    def test_sort(self):
        self.table.add({"name": "A", "age": 30})
        self.table.add({"name": "B", "age": 10})
        res = self.table.sort_by("age")
        self.assertEqual(res[0]["age"], 10)


if __name__ == "__main__":
    unittest.main()