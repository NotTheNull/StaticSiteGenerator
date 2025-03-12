import unittest
from blocktype import *

class Test_BlockType(unittest.TestCase):


    TEST_FULL_MARKDOWN = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    def test_markdown_to_blocks(self):
        blocks = markdown_to_blocks(Test_BlockType.TEST_FULL_MARKDOWN)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    
    def test_block_type_heading(self):
        block = "### This is a heading"
        btype = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, btype)


    def test_block_type_code(self):
        block = """
```
x = 1
x++
print(x)
```
"""
        
        btype = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, btype)

    def text_block_type_quote(self):
        block = """
>Quote me on that
>Dude, where's my car?
>...but I carry a BIIIIIIIIIIIG stick!
"""
        btype = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, btype)

    def text_block_type_unorderedlist(self):
        block = """
- one item
- two item
- red item
- blue item
"""
        btype = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, btype)

    def text_block_type_orderedlist(self):
        block = """
1. one item
2. two item
3. red item
4. blue item
"""
        btype = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, btype)

    def text_block_type_everythingelse(self):
        block = "A normal sentence"
        btype = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, btype)

    



if __name__ == "__main__":
    unittest.main()
