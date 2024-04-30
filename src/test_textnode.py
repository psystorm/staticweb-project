import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()
