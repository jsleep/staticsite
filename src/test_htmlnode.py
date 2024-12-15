import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {'test': 1}
        node = HTMLNode(None,None,None,props)
        props_str = node.props_to_html()
        expected_str = 'test="1"'

        self.assertEqual(props_str, expected_str)