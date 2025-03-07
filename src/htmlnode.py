from textnode import *

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        #all fields CAN be NONE
        self.tag = tag #string for the HTML tag e.g. p, a, h1, etc
        self.value = value #the string content between start & end tag
        self.children = children #the HTMLNode content betwen the start & end tag
        self.props = props #dictionary of the tag's attributes

    #expected to be overriden by child nodes
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None: return ""
        if len(self.props.items()) == 0: return ""

        return "".join(list(map(lambda k: f" {k}=\"{self.props[k]}\"", self.props.keys())))

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
