from textnode import *
from parentnode import ParentNode
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextType.NORMAL:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        case TextType.IMAGE:
            return LeafNode("img", " ", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
        case TextType.URL:
            return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
        case _:
            raise Exception(f"Text Type {text_node.text_type} is not supported")
    

# def __text_to_anchor_tag(text_node):
#     # sample text:  [Boots](https://boot.dev)
#     if text_node.text_type != TextType.URL: raise ValueError("This conversion is for Anchor tags only")

#     link_text_pos_end = text_node.text.index("]")
#     link_text = text_node.text[1:link_text_pos_end]

#     src_pos_start = text_node.text.index("(")
#     src_pos_end = text_node.text.index(")")
#     src = text_node.text[src_pos_start:src_pos_end]

#     return LeafNode("a", link_text, {"href": f"{src}"})

# def __text_to_img_tag(text_node):
#     # sample text:  ![alt text for image](url/of/image.jpg)
#     if text_node.text_type != TextType.IMAGE: raise ValueError("This conversion is for Image tags only")

#     alt_pos_end = text_node.text.index("]")
#     alt = text_node.text[2:alt_pos_end]

#     src_pos_start = text_node.text.index("(")
#     src_pos_end = text_node.text.index(")")
#     src = text_node.text[src_pos_start:src_pos_end]

#     return LeafNode("img", " ", {"src": f"{src}", "alt": f"{alt}"})

