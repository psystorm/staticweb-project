
class TextNode:
    def __init__(self, text, text_style, url=None):
        self.text = text
        self.text_style = text_style
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and
                self.text_style == other.text_style and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_style}, {self.url})"