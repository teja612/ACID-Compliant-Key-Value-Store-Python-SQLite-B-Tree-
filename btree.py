class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf
        self.next_leaf = None  # Linked list for range scans

class BPlusTree:
    def __init__(self, order=3):
        self.root = BPlusTreeNode(is_leaf=True)
        self.order = order
    
    def insert(self, key, value):
        # Simplified insertion logic
        if len(self.root.keys) >= self.order:
            self._split_root()
        self._insert_non_full(self.root, key, value)
