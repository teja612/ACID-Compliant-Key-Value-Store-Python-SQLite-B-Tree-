class KVStore:
    def __init__(self):
        self.wal = WriteAheadLog()
        self.index = BPlusTree()
    
    def put(self, key, value):
        self.wal.log(f"PUT {key} {value}")
        self.index.insert(key, value)
    
    def get(self, key):
        return self.index.search(key)
