import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_rep(self):
        node_str = str(TextNode("This is a text node", TextType.BOLD))
        expected_str = 'TextNode(This is a text node, bold, None)'
        self.assertEqual(node_str, expected_str)


if __name__ == "__main__":
    unittest.main()