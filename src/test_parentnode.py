import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class Test_ParentNode(unittest.TestCase):
    def test_tohtml_withleafs(self):
        sut = ParentNode("div", [LeafNode(None, "Standard line ", None), LeafNode("b", "for me", None)], {"class": "row", "id": "idDiv"})
        expected = "<div class=\"row\" id=\"idDiv\">Standard line <b>for me</b></div>"
        self.assertEqual(sut.to_html(), expected)

    def test_tohtml_withparents(self):
        sut = ParentNode("div", [ParentNode("p", [LeafNode(None, "Standard line ", None), LeafNode("b", "for me", None)], None), LeafNode("i", "And more!!", None)], {"class": "row", "id": "idDiv"})
        expected = "<div class=\"row\" id=\"idDiv\"><p>Standard line <b>for me</b></p><i>And more!!</i></div>"
        self.assertEqual(sut.to_html(), expected)

    def test_init_nochildren_raiseerror(self):
        self.assertRaises(ValueError, ParentNode, "p", None, None)

    def test_init_notag_raiseerror(self):
        self.assertRaises(ValueError, ParentNode, None, [LeafNode(None, "Stuff")], None)


if __name__ == "__main__":
    unittest.main()
