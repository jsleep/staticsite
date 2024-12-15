import re

def extract_markdown_images(text):
    matches = re.findall('!\[(.*?)\]\((.*?)\)', text)
    return matches

def extract_markdown_links(text):
    matches = re.findall('\[(.*?)\]\((.*?)\)', text)
    return matches

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            title = line.split('# ')[1]
            return title
    raise ValueError('No header')