import os

class WriteAheadLog:
    def __init__(self, log_file="wal.log"):
        self.log_file = open(log_file, "a+")
    
    def log(self, operation: str):
        self.log_file.write(f"{operation}\n")
        self.log_file.flush()  # Force OS to write to disk
    
    def recover(self):
        self.log_file.seek(0)
        return [line.strip() for line in self.log_file.readlines()]
