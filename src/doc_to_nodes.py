from converter import *
from blocktype import *
from textnode import *
from parentnode import ParentNode


def markdown_to_html_nodes(doc_text):
    if doc_text == None: raise Exception("Document not set")
    if len(doc_text.strip()) == 0: raise Exception("Document cannot be empty")

    children = []
    block_list = markdown_to_blocks(doc_text)
    for blk in block_list:
        btype = block_to_block_type(blk)
        btext = get_block_text(blk, btype)

        match(btype):
            case BlockType.CODE:
                children.append(ParentNode("pre", [text_node_to_html_node(TextNode(btext[0], TextType.CODE, None))]))
            case BlockType.QUOTE:
                children.append(ParentNode("quote", __list_text_nodes_to_html_nodes(text_to_text_nodes(btext[0]))))
            case BlockType.HEADING:
                children.append(ParentNode(f"h{len(btext[0].strip())}", __list_text_nodes_to_html_nodes(text_to_text_nodes(btext[1]))))
            case BlockType.UNORDERED_LIST:
                lists = []
                for text in btext:
                    lists.append(ParentNode("li", __list_text_nodes_to_html_nodes(text_to_text_nodes(text))))

                children.append(ParentNode("ul", lists, None))
            case BlockType.ORDERED_LIST:
                lists = []
                for text in btext:
                    lists.append(ParentNode("li", __list_text_nodes_to_html_nodes(text_to_text_nodes(text))))

                children.append(ParentNode("ol", lists, None))
            case BlockType.PARAGRAPH:
                children.append(ParentNode("p", __list_text_nodes_to_html_nodes(text_to_text_nodes(btext[0]))))
            case _:
                raise Exception(f"Block type {btype} unsupported")
            
    return ParentNode("div", children, {"id": "idDocument"})
    



def __list_text_nodes_to_html_nodes(nodes):
    if not isinstance(nodes, list): raise ValueError("Nodes MUST be a list")

    new_list = []
    for node in nodes:
        new_list.append(text_node_to_html_node(node))

    return new_list
    #return [html for node in nodes for html in text_node_to_html_node(node)]
