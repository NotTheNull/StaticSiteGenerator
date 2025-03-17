import unittest
from doc_to_nodes import markdown_to_html_nodes

class Test_DocToHtml(unittest.TestCase):

    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div id=\"idDocument\"><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div id=\"idDocument\"><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
