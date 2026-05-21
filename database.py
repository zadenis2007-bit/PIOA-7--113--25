from memory_table import MemoryTable
from file_table import FileTable


class Database:
    def __init__(self, mode="memory"):
        if mode == "file":
            self.table = FileTable()
        else:
            self.table = MemoryTable()