from htmlnode import HTMLNode

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
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props}"