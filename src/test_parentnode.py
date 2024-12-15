import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        actual = node.to_html()
        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        # ignore whitespace
        self.assertEqual("".join(actual.split()),"".join(expected.split()))