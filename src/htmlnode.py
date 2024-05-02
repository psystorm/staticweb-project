from textnode import TextNode

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    def __eq__(self, other):
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_str = ""
        if len(self.props) == 0:
            return ""
        for k,v in self.props.items():
            html_str += f'{k}="{v}" '
        return html_str[:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None")
        if self.tag and (len(self.props) > 0):
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        elif self.tag:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return self.value
        
class ParentNode(HTMLNode):
    def __init__(self, tag=None,children=None, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None")
        if self.children is None:
            raise ValueError("Children cannot be None")
        return self.get_nodes()

    def get_nodes(self):
        html_str = ""
        if self.children is None:
            return self.to_html()
        if len(self.props) > 0:
                html_str += f'<{self.tag} {self.props_to_html()}>'
        else:
            html_str += f'<{self.tag}>'
        for child in self.children:
            if len(child.children) == 0:
                html_str += child.to_html()
            else:
                html_str += child.get_nodes()
        html_str += f'</{self.tag}>'
        return html_str

