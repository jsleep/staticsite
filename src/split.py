from textnode import TextNode, TextType
from extract import extract_markdown_links, extract_markdown_images
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, new_type):
    res = []
    for node in old_nodes:
        node_text = node.text
        old_type = node.text_type

        if delimiter not in node_text:
            res.append(node)
            continue
        
        split_text = node_text.split(delimiter)

        for i,text in enumerate(split_text):
            if text:
                if i % 2 == 1:
                    res.append(TextNode(text, new_type))
                else:
                    res.append(TextNode(text, old_type))
    return res

def split_nodes_image(old_nodes):
    new_type = TextType.IMAGE
    res = []
    
    for node in old_nodes:
        node_text = node.text
        old_type = node.text_type

        extracted_images = extract_markdown_images(node_text)
        if not extracted_images:
            res.append(node)
            continue
        
        for alt, url in extracted_images:
            delimiter = f'![{alt}]({url})'
            
            pre_text, node_text = node_text.split(delimiter, 1)
            res.append(TextNode(pre_text, old_type))
            res.append(TextNode(alt, new_type, url))

        # add final split old text, if any left
        if node_text:
            res.append(TextNode(node_text, old_type))
    
    return res

def split_nodes_link(old_nodes):
    new_type = TextType.LINK
    res = []
    
    for node in old_nodes:
        node_text = node.text
        old_type = node.text_type

        extracted_links = extract_markdown_links(node_text)
        if not extracted_links:
            res.append(node)
            continue
        
        for alt, url in extracted_links:
            delimiter = f'[{alt}]({url})'
            
            pre_text, node_text = node_text.split(delimiter, 1)
            res.append(TextNode(pre_text, old_type))
            res.append(TextNode(alt, new_type, url))

        # add final split old text, if any left
        if node_text:
            res.append(TextNode(node_text, old_type))
    
    return res