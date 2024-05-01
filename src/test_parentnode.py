import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    # def test_eq(self):
    #     node = HTMLNode("p", "This is a text node", None, {"class":"bold"})
    #     node2 = HTMLNode("p", "This is a text node", None, {"class":"bold"})
    #     self.assertEqual(node, node2, f'{node} should be equal to {node2}')
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