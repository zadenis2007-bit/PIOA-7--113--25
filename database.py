from memory_table import MemoryTable
from file_table import FileTable


class Database:
    def __init__(self, mode="memory"):
        if mode == "memory":
            self.table = MemoryTable()

        elif mode == "file":
            self.table = FileTable()

        else:
            raise ValueError(
                f"Unknown database mode: {mode}"
            )
