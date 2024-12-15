from leafnode import LeafNode
from textnode import TextNode, TextType

from htmlnode import *
from parentnode import ParentNode


from split import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.IMAGE:
            return LeafNode(tag='img',props={'src': text_node.url, 'alt': text_node.text})
        case TextType.LINK:
            return LeafNode(tag='a',value=text_node.text, props={'href': text_node.url})
        case TextType.CODE:
            return LeafNode(tag='code',value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag='i',value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag='b',value=text_node.text)
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        
def text_to_textnodes(text):
    # generic delimiter, types
    # fun bug - BOLD comes before ITALIC or else delimiter screws up
    delimiters = ['**', '*', '`']
    types = [TextType.BOLD, TextType.ITALIC, TextType.CODE]

    text_nodes = [TextNode(text, TextType.TEXT)]

    # image - doing image first here should ideally help with same []() formatting
    # betweeen image and links
    text_nodes = split_nodes_image(text_nodes)

    # link
    text_nodes = split_nodes_link(text_nodes)

    # generic
    for delimiter, new_type in zip(delimiters,types):
        text_nodes = split_nodes_delimiter(text_nodes, delimiter, new_type)
    
    return text_nodes

def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split('\n\n') if not block.isspace()]

def is_ordered_list(block):
    list_num = 1
    for line in block.split('\n'):
        if not line.startswith(f'{list_num}. '):
            return False
        list_num += 1
    return True

def block_to_block_type(block):
    if block.startswith('#'):
        return 'heading'
    elif block.startswith('```') and block.endswith('```'):
        return 'code'
    elif all(block_line.startswith('> ') for block_line in block.split('\n')):
        return 'quote'
    elif all(block_line.startswith('* ') or block_line.startswith('- ') for block_line in block.split('\n')):
        return 'unordered_list'
    elif is_ordered_list(block):
        return 'ordered_list'
    else:
        return 'normal'


def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)

    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case 'heading':
                header_num = 0
                for c in block:
                    if c == '#':
                        header_num += 1
                    else: 
                        break
                html_node = LeafNode(f'h{header_num}', block[header_num+1:])
            case 'quote':
                html_node = LeafNode('blockquote', block.replace('> ',''))
            case 'unordered_list':
                child_nodes = []
                for line in block.split('\n'):
                    html_nodes = get_children_nodes(line[2:])
                    child_nodes.append(ParentNode('li',html_nodes))
                html_node = ParentNode('ul', child_nodes)
            case 'ordered_list':
                child_nodes = []
                for line in block.split('\n'):
                    html_nodes = get_children_nodes(line[3:])
                    child_nodes.append(ParentNode('li',html_nodes))
                html_node = ParentNode('ul', child_nodes)
            case 'code':
                child = LeafNode('code', block.replace('`',''))
                html_node = ParentNode('pre', [child]) # may need to slice off numbers
            case _:
                html_node = ParentNode('p', get_children_nodes(block))
        
        nodes.append(html_node)
    return ParentNode('div', nodes)

def get_children_nodes(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
    return html_nodes