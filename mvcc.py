class MVCCKVStore(KVStore):
    def __init__(self):
        super().__init__()
        self.version_chain = {}  # {key: [(timestamp, value)]}
    
    def put(self, key, value):
        self.wal.log(f"PUT {key} {value}")
        self.version_chain.setdefault(key, []).append((time.time(), value))
