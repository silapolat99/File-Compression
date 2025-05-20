import unittest
from redblacktree import RedBlackTree
from b_plus_tree import BPlusTree

class TestTrees(unittest.TestCase):
    def test_red_black_tree_insert_search(self):
        tree = RedBlackTree()
        tree.insert("file1.txt")
        self.assertTrue(tree.search("file1.txt"))
        self.assertFalse(tree.search("file2.txt"))

    def test_b_plus_tree_insert_search(self):
        tree = BPlusTree(t=3)
        tree.insert("fileA.txt")
        self.assertTrue(tree.search("fileA.txt"))
        self.assertFalse(tree.search("fileB.txt"))

if __name__ == '__main__':
    unittest.main()
