import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold")
		self.assertEqual(node, node2)
		
		node3 = TextNode("This is a different text node","bold")
		self.assertNotEqual(node, node3)
		
		node4 = TextNode("This is a text node","italic")
		self.assertNotEqual(node2, node4)
		
		node5 = TextNode("This is a text node","bold","www.example.com")
		self.assertNotEqual(node, node5)
		
		node6 = TextNode("This is a text node","bold",None)
		self.assertNotEqual(node5,node6)


if __name__ == "__main__":
    unittest.main()
