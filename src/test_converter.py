import unittest
from converter import *
from textnode import *


class Test_Converter(unittest.TestCase):
    
    def test_convert_normal(self):
        text = TextNode("Normal text", TextType.NORMAL)
        expected = "Normal text"

        sut = text_node_to_html_node(text)
        self.assertEqual(sut.to_html(), expected)

    def test_convert_bold(self):
        text = TextNode("Bold text", TextType.BOLD)
        expected = "<b>Bold text</b>"

        sut = text_node_to_html_node(text)
        self.assertEqual(sut.to_html(), expected)

    def test_convert_italics(self):
        text = TextNode("Italic text", TextType.ITALIC)
        expected = "<i>Italic text</i>"
        
        sut = text_node_to_html_node(text)
        self.assertEqual(sut.to_html(), expected)

    def test_convert_code(self):
        text = TextNode("x = 1", TextType.CODE)
        expected = "<code>x = 1</code>"
        
        sut = text_node_to_html_node(text)
        self.assertEqual(sut.to_html(), expected)

    def test_convert_img(self):
        text = TextNode("alt text", TextType.IMAGE, "path/to/image.jpg")
        expected = "<img src=\"path/to/image.jpg\" alt=\"alt text\"> </img>"
        
        sut = text_node_to_html_node(text)
        self.assertEqual(sut.to_html(), expected)

    def test_convert_anchor(self):
        text = TextNode("Boots", TextType.URL, "https://boot.dev")
        expected = "<a href=\"https://boot.dev\">Boots</a>"
        
        sut = text_node_to_html_node(text)
        self.assertEqual(sut.to_html(), expected)

    




if __name__ == "__main__":
    unittest.main()
