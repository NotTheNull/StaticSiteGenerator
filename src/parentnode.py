from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        if tag == None: raise ValueError("Tag MUST be provided for Parent Nodes")
        if children == None: raise ValueError("Children MUST be defined for Parent Nodes")

        super().__init__(tag, None, children, props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.children_to_html(self.children)}</{self.tag}>"
    
    def children_to_html(self, child_list):
        if len(child_list) == 0: return ""
        return child_list[0].to_html() + self.children_to_html(child_list[1:])