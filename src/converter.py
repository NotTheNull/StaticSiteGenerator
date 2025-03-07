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
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        new_nodes.extend(__split_text_into_nodes(node.text, delimiter, text_type))

    return new_nodes

def __split_text_into_nodes(text, delimiter, text_type):
    if text == None: return []
    if len(text.strip()) == 0: return []

    if delimiter in text:
        node_list = []

        pos_start = text.find(delimiter)
        node_list.append(TextNode(text[0:pos_start], TextType.NORMAL, None))

        loop_text = text[pos_start + len(delimiter):]
        pos_end = loop_text.find(delimiter)
        if pos_end < 0: raise Exception("Invalid markup")

        node_list.append(TextNode(loop_text[0:pos_end], text_type, None))
        loop_text = loop_text[pos_end + len(delimiter):]
        node_list.append(TextNode(loop_text, TextType.NORMAL, None))

        return node_list

    else:
        return [TextNode(text, TextType.NORMAL, None)]


