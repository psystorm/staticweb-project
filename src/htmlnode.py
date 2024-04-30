

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