import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a text node", None, {"class":"bold"})
        node2 = HTMLNode("p", "This is a text node", None, {"class":"bold"})
        self.assertEqual(node, node2, f'{node} should be equal to {node2}')

    def test_props_to_html(self):
        node = HTMLNode("p", "This is a text node", None, {"class":"bold"})
        self.assertEqual(node.props_to_html(), 'class="bold"')

        node2 = HTMLNode("p", "This is a text node", (['h1','p','div']), {"class":"bold", "id":"1", "style":"color:red"})
        self.assertEqual(node2.props_to_html(), 'class="bold" id="1" style="color:red"')

    def test_render(self):
        node = LeafNode("p", "This is a text node")
        self.assertEqual(node.to_html(), '<p>This is a text node</p>')
        
        node2 = LeafNode("p","This is a text node",{"class":"bold"})
        self.assertEqual(node2.to_html(), '<p class="bold">This is a text node</p>')

        node3 = LeafNode("p","This is a text node",{"class":"bold", "id":"1", "style":"color:red"})
        self.assertEqual(node3.to_html(), '<p class="bold" id="1" style="color:red">This is a text node</p>')

        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node4.to_html(), '<a href="https://www.google.com">Click me!</a>')

        node5 = LeafNode("img", None, {"src": "https://www.google.com/logo.png"})
        self.assertRaises(ValueError, node5.to_html)

    def test_nest_html(self):
        p_node = ParentNode("p", [
            LeafNode("strong", "This is a bold text"),
            LeafNode("em", "This is an italic text"),
            ParentNode("div", [
                LeafNode("span", "This is a span text"),
                LeafNode("td", "This is a table")
                ], {"class":"container"}),
            LeafNode("img", "This is a division text", {"src":"https://www.google.com/logo.png"})
            ], {"class":"bold"})
        self.assertEqual(p_node.to_html(), '<p class="bold"><strong>This is a bold text</strong><em>This is an italic text</em><div class="container"><span>This is a span text</span><td>This is a table</td></div><img src="https://www.google.com/logo.png">This is a division text</img></p>')


if __name__ == "__main__":
    unittest.main()