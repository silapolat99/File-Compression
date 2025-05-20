class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf
        self.next = None  # for leaf-to-leaf traversal

class BPlusTree:
    def __init__(self, t=3):  # t: max t-1 keys per node
        self.root = BPlusTreeNode(True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.t - 1:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            idx = self._find_index(node.keys, key)
            child = node.children[idx]
            if len(child.keys) == self.t - 1:
                self._split_child(node, idx)
                if key > node.keys[idx]:
                    idx += 1
            self._insert_non_full(node.children[idx], key)

    def _split_child(self, parent, idx):
        t = self.t
        node = parent.children[idx]
        new_node = BPlusTreeNode(node.is_leaf)
        mid = t // 2
        parent.keys.insert(idx, node.keys[mid])

        new_node.keys = node.keys[mid+1:]
        node.keys = node.keys[:mid]

        if not node.is_leaf:
            new_node.children = node.children[mid+1:]
            node.children = node.children[:mid+1]
        else:
            new_node.next = node.next
            node.next = new_node

        parent.children.insert(idx+1, new_node)

    def _find_index(self, keys, key):
        for i, item in enumerate(keys):
            if key < item:
                return i
        return len(keys)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node.is_leaf:
            return key in node.keys
        else:
            idx = self._find_index(node.keys, key)
            return self._search(node.children[idx], key)

    def print_tree(self):
        self._print_node(self.root)

    def _print_node(self, node, level=0):
        print("  " * level + str(node.keys))
        if not node.is_leaf:
            for child in node.children:
                self._print_node(child, level + 1)

