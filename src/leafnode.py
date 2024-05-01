from htmlnode import HTMLNode


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

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"