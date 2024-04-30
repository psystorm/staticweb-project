import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()