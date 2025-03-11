import re
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
    if not isinstance(old_nodes, list): raise ValueError("1st Argument must be a list of TextNodes")

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



def split_nodes_images(old_nodes):
    if not isinstance(old_nodes, list): raise ValueError("Argument must be a list of TextNodes")

    return [img for lst in list(map(__split_markdown_images, old_nodes)) for img in lst]
    

def __split_markdown_images(node):
    if not isinstance(node, TextNode): raise ValueError("Argument MUST be a TextNode")
    if node.text_type != TextType.NORMAL: return [node]

    images = extract_markdown_images(node.text)
    if len(images) == 0: return [node]

    node_list = []
    pos_start = 0
    pos_end = 1
    for img in images:
        pos_end = node.text.index(img[0]) - 2
        node_list.append(TextNode(node.text[pos_start:pos_end], TextType.NORMAL, None))

        pos_start = node.text.index(img[1]) + len(img[1]) + 1 # the +1 covers the closing parenthesis
        node_list.append(TextNode(img[0], TextType.IMAGE, img[1]))

    if len(node.text.strip()) > pos_start:
        node_list.append(TextNode(node.text[pos_start:], TextType.NORMAL, None))

    return node_list


def split_nodes_links(old_nodes):
    if not isinstance(old_nodes, list): raise ValueError("Argument must be a list of TextNodes")

    return [link for lst in list(map(__split_markdown_links, old_nodes)) for link in lst]

def __split_markdown_links(node):
    if not isinstance(node, TextNode): raise ValueError("Argument MUST be a TextNode")
    if node.text_type != TextType.NORMAL: return [node]

    links = extract_markdown_links(node.text)
    if len(links) == 0: return [node]

    node_list = []
    pos_start = 0
    pos_end = 1
    for link in links:
        pos_end = node.text.index(link[0]) - 1
        node_list.append(TextNode(node.text[pos_start:pos_end], TextType.NORMAL, None))

        pos_start = node.text.index(link[1]) + len(link[1]) + 1
        node_list.append(TextNode(link[0], TextType.URL, link[1]))

    if len(node.text.strip()) > pos_start:
        node_list.append(TextNode(node.text[pos_start:], TextType.NORMAL, None))

    return node_list



#![rick roll](https://i.imgur.com/aKaOqIh.gif)
markdown_img_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
def extract_markdown_images(text):
    return re.findall(markdown_img_regex, text)
    

#[boot dev](https://boot.dev)
markdown_link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
def extract_markdown_links(text):
    return re.findall(markdown_link_regex, text)
    

def text_to_text_nodes(text):
    return split_nodes_delimiter(
        split_nodes_delimiter(
            split_nodes_delimiter(
                split_nodes_links(
                    split_nodes_images(
                        [TextNode(text, TextType.NORMAL, None)]
                    )
                ),
                "`",
                TextType.CODE
            ),
            "_",
            TextType.ITALIC
        ), 
        "**", 
        TextType.BOLD)


def markdown_to_blocks(markdown):
    if markdown is None: return []
    if len(markdown.strip()) == 0: return []

    blocks = []
    for txt in markdown.split("\n\n"):
        if len(txt.strip()) == 0: continue
        blocks.append(txt.strip())

    return blocks
