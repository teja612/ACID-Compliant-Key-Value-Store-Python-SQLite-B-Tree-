# ACID-Compliant-Key-Value-Store-Python-SQLite-B-Tree-
1. Initialize the Store
python
kv = KVStore()
kv.put("name", "Alice")
print(kv.get("name"))  # Output: "Alice"
2. Simulate Crash Recovery
python
# Simulate a crash
kv = KVStore()
kv.wal.recover()  # Replay uncommitted operations
3. Benchmark Performance
python
import time
start = time.time()
for i in range(1000):
    kv.put(f"key_{i}", f"value_{i}")
print(f"Ops/sec: {1000 / (time.time() - start)}")
