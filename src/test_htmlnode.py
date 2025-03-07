import unittest
from htmlnode import HTMLNode

class Test_HTMLNode(unittest.TestCase):
    def test_props_tohtml_withdata(self):
        node = HTMLNode("p", "Some test to print", None, {"class": "d-flex", "z-index": "1"})
        expected = " class=\"d-flex\" z-index=\"1\""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_tohtml_none(self):
        node = HTMLNode("p", "Some test to print")
        expected = ""
        self.assertEqual(node.props_to_html(), expected)


if __name__ == "__main__":
    unittest.main()
