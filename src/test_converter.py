import unittest
import re
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

    TEST_MARKDOWN_IMAGE = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(Test_Converter.TEST_MARKDOWN_IMAGE)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    TEST_MARKDOWN_LINK = "This is text with a link [Boot Dev](https://boot.dev)"
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(Test_Converter.TEST_MARKDOWN_LINK)
        self.assertListEqual([("Boot Dev", "https://boot.dev")], matches)


    TEST_MULTIPLE_IMAGES =  "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
    def test_split_images(self):
        node = TextNode(Test_Converter.TEST_MULTIPLE_IMAGES, TextType.NORMAL, None)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    TEST_MULTIPLE_LINKS = "The videos from [Boot Dev](https://boot.dev) should be viewable on [YouTube](https://www.youtube.com)"
    def test_split_links(self):
        node = TextNode(Test_Converter.TEST_MULTIPLE_LINKS, TextType.NORMAL, None)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("The videos from ", TextType.NORMAL),
                TextNode("Boot Dev", TextType.URL, "https://boot.dev"),
                TextNode(" should be viewable on ", TextType.NORMAL),
                TextNode("YouTube", TextType.URL, "https://www.youtube.com")
            ],
            new_nodes
        )

    def test_split_links_withoutlinks(self):
        test_node = [TextNode("This is a normal string", TextType.NORMAL, None)]
        sut = split_nodes_links(test_node)
        self.assertListEqual(
            test_node,
            sut
        )


    TEST_FULL_MARKDOWN = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    def test_full_markdown_to_text(self):
        sut = text_to_text_nodes(Test_Converter.TEST_FULL_MARKDOWN)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.URL, "https://boot.dev"),
            ],
            sut
        )

if __name__ == "__main__":
    unittest.main()
