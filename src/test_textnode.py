import unittest

from textnode import TextNode
from textnode import split_nodes_delimiter
from textnode import split_nodes_delimiter_mkII


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold")
		self.assertEqual(node, node2, f'{node} should be equal to {node2}')
		
		node6 = TextNode("This is a text node","bold",None)
		self.assertEqual(node2,node6, f'{node2} should be equal to {node6}, explict None url in node6')

	def test_neq(self):
		node = TextNode("This is a text node", "bold")
		node3 = TextNode("This is a different text node","bold")
		self.assertNotEqual(node, node3, f'{node} should not be equal to {node3}')

		node4 = TextNode("This is a text node","italic")
		self.assertNotEqual(node, node4, f'{node} should not be equal to {node4}')

		node5 = TextNode("This is a text node","bold","www.example.com")
		self.assertNotEqual(node, node5, f'{node} should not be equal to {node5}')

		node6 = TextNode("This is a text node","bold",None)
		self.assertNotEqual(node5,node6, f'{node5} should not be equal to {node6}, explict None url in node6')

	def test_delimit_split(self):
		node = TextNode("This is a **text** node", "text")
		node1 = TextNode("**This** is a text **node**", "text")
		node2 = TextNode("This is a text node", "text")
		node3 = TextNode("This **is** a **text** node", "text")
		node4 = TextNode("**This is a **text** node", "text")
		node5 = TextNode("This **is a** text **node**", "text")

		n_node = split_nodes_delimiter([node], "**", "bold")
		n_node1 = split_nodes_delimiter([node1], "**", "bold")
		n_node2 = split_nodes_delimiter([node2], "**", "bold")
		n_node3 = split_nodes_delimiter([node3], "**", "bold")
		self.assertRaises(ValueError,split_nodes_delimiter,[node4], "**", "bold")
		n_node5 = split_nodes_delimiter([node5], "**", "bold")

		print(n_node)
		print(n_node1)
		print(n_node2)
		print(n_node3)
		#print(n_node4)
		print(n_node5)
		print(split_nodes_delimiter_mkII([node1], "**", "bold"))
		print(split_nodes_delimiter_mkII([node3], "**", "bold"))
		print(split_nodes_delimiter_mkII([node5], "**", "bold"))


		self.assertEqual(n_node, [TextNode("This is a ",'text'),TextNode("text",'bold'),TextNode(' node','text')])

if __name__ == "__main__":
    unittest.main()
