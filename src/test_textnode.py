import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_notequal_differenttext(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is NOT a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_notequal_differenttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_notequal_differenturl(self):
        node = TextNode("This is a text node", TextType.URL, "https://boot.dev")
        node2 = TextNode("This is a text node", TextType.URL, "https://www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
