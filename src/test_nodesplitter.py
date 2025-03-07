import unittest
from converter import split_nodes_delimiter
from textnode import *

class Test_NodeSplitter(unittest.TestCase):
    def test_nodesplit(self):
        text = "This is a **bold statement** but _this has emphasis_"
        node = TextNode(text, TextType.NORMAL, None)

        sut = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(sut), 3, "The nodes were not split correctly")
        self.assertEqual(sut[0].text, "This is a ")
        self.assertEqual(sut[1].text_type, TextType.BOLD)
        self.assertEqual(sut[1].text, "bold statement")
        self.assertEqual(sut[2].text, " but _this has emphasis_")



if __name__ == "__main__":
    unittest.main()

