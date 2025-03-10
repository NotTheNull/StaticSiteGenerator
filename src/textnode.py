
from enum import Enum

class TextType(Enum):
    NORMAL = "Normal"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Codeblock"
    URL = "Link"
    IMAGE = "Image"


class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, test):
        if not isinstance(test, TextNode): return False

        if self.text_type != test.text_type: return False
        if self.text != test.text: return False
        return self.url == test.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
