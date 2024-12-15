import unittest

from textnode import TextNode, TextType
from convert import *

class TestConvert(unittest.TestCase):
    def test_bold_convert(self):
        node = TextNode("This is a text node", TextType.BOLD)
        actual = text_node_to_html_node(node).to_html()
        expected = '<b>This is a text node</b>'
        self.assertEqual(actual,expected)
    
    def test_text_to_textnodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        actual = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(actual,expected)
    
    def test_text_to_textnodes(self):
        markdown = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''

        actual = markdown_to_blocks(markdown)
        expected = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '''* This is the first list item in a list block
* This is a list item
* This is another list item'''
        ]
        self.assertEqual(actual,expected)
    
    def test_block_to_block_type(self):
        markdown = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

1. first item in ordered list
2. second
3. third

```
code_block
```

> quote
> block
> yay
'''

        blocks = markdown_to_blocks(markdown)
        actual = [block_to_block_type(block) for block in blocks]
        expected = [
            'heading',
            'normal',
            'unordered_list',
            'ordered_list',
            'code',
            'quote'
        ]
        self.assertEqual(actual,expected)

    def test_markdown_to_html_node(self):
        markdown = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

1. first item in ordered list
2. second
3. third

```
code_block
```

> quote
> block
> yay

this is paragraph with a [link](boot.dev) and an ![image](image_url.com)
'''
        actual = markdown_to_html_node(markdown).to_html()
        print(actual)
        expected = '''
        <div>
            <h1>This is a heading</h1>
            <p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>
            <ul>
                <li>This is the first list item in a list block</li>
                <li>This is a list item</li>
                <li>This is another list item</li>
            </ul>
            <ol>
                <li> first item in ordered list</li>
                <li> second</li>
                <li> third</li>
            </ol>
            <pre>
                <code>
                    code_block
                </code>
            </pre>
            <blockquote>
                quote
                block
                yay
            </blockquote>
            <p>
                this is paragraph with a <a href="boot.dev">link</a> and an <img src="image_url.com" alt="image"></img>
            </p>
        </div>
        '''
        # compare ignoring whitespace
        self.assertEqual("".join(actual.split()),"".join(expected.split()))

