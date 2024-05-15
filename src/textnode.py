from htmlnode import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"



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
    
def text_node_to_html(text_node):
    if text_node.text_style is text_type_text:
        return LeafNode(None, text_node.text)
    elif text_node.text_style is text_type_bold:
        return LeafNode('b', text_node.text)
    elif text_node.text_style is text_type_italic:
        return LeafNode('i', text_node.text)
    elif text_node.text_style is text_type_code:
        return LeafNode('code', text_node.text)
    elif text_node.text_style is text_type_link:
        return LeafNode('a', text_node.text, {"href": text_node.url})
    elif text_node.text_style is text_type_image:
        return LeafNode('img', text_node.text, {"src": text_node.url})
    else:
        raise ValueError("Invalid text style")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if (node.text.count(delimiter) % 2 == 0) and (node.text.count(delimiter) > 0):
            text_var = node.text
            old_node_type = node.text_style
            for i in range(node.text.count(delimiter)):
                text_parts = text_var.partition(delimiter)
                if text_parts[0] == "":
                    text_var = text_parts[2]
                elif text_parts[2] == "":
                    new_nodes.append(TextNode(text_parts[0], text_type))
                else:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(text_parts[0], old_node_type))
                        text_var = text_parts[2]
                    else:
                        new_nodes.append(TextNode(text_parts[0], text_type))
                        text_var = text_parts[2]
                        if i == node.text.count(delimiter) - 1:
                            new_nodes.append(TextNode(text_var, old_node_type))
        elif node.text.count(delimiter) == 0:
            new_nodes.append(TextNode(node.text, node.text_style))
        else:
            raise ValueError("Invalid markdown syntax")
    return new_nodes

def split_nodes_delimiter_mkII(old_nodes, delimiter,text_type):
    new_nodes = []
    for node in old_nodes:
        temp = node.text.split(delimiter)
        if len(temp) > 1:
            for i in range(len(temp)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(temp[i], text_type_text))
                else:
                    new_nodes.append(TextNode(temp[i], text_type))
        else:
            raise ValueError("Invalid markdown syntax")
    return new_nodes