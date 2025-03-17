from textnode import *
from parentnode import ParentNode
from leafnode import LeafNode


def main():
    node = TextNode("Some text", TextType.URL, "https://boot.dev")
    print(node)

main()
