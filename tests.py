import unittest
from database import Table


class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = Table()

    def test_add(self):
        self.table.add({"name": "Ivan", "age": 20})
        self.assertEqual(len(self.table.get_all()), 1)

    def test_filter(self):
        self.table.add({"name": "Ivan", "age": 20})
        self.table.add({"name": "Petr", "age": 25})

        result = self.table.filter("Ivan")
        self.assertEqual(len(result), 1)

    def test_update(self):
        self.table.add({"name": "Ivan", "age": 20})
        result = self.table.update(1, "Alex", 30)
        self.assertTrue(result)

    def test_delete(self):
        self.table.add({"name": "Ivan", "age": 20})
        result = self.table.delete(1)
        self.assertTrue(result)

    def test_sort(self):
        self.table.add({"name": "A", "age": 30})
        self.table.add({"name": "B", "age": 20})

        result = self.table.sort_by("age")
        self.assertEqual(result[0]["age"], 20)


if __name__ == "__main__":
    unittest.main()