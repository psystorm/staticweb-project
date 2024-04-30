import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    # def test_eq(self):
    #     node = HTMLNode("p", "This is a text node", None, {"class":"bold"})
    #     node2 = HTMLNode("p", "This is a text node", None, {"class":"bold"})
    #     self.assertEqual(node, node2, f'{node} should be equal to {node2}')
    def test_render(self):
        node = LeafNode("p", "This is a text node")
        self.assertEqual(node.to_html(), '<p>This is a text node</p>')
        
        node2 = LeafNode("p","This is a text node",{"class":"bold"})
        self.assertEqual(node2.to_html(), '<p class="bold">This is a text node</p>')

        node3 = LeafNode("p","This is a text node",{"class":"bold", "id":"1", "style":"color:red"})
        self.assertEqual(node3.to_html(), '<p class="bold" id="1" style="color:red">This is a text node</p>')


if __name__ == "__main__":
    unittest.main()