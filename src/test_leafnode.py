import unittest
from leafnode import LeafNode

class Test_LeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Boot Dev URL", {"href": "https://boot.dev", "target": "_blank"})
        expected = "<a href=\"https://boot.dev\" target=\"_blank\">Boot Dev URL</a>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_no_value(self):
        self.assertRaises(ValueError, LeafNode, None, None, None)

if __name__ == "__main__":
    unittest.main()
