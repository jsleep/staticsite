
import extract
import convert
import os
import sys

def generate_page(from_path, template_path, dest_path):
    print(f'generating from {from_path} to {dest_path} using {template_path}')

    with open(from_path, 'r') as f:
        markdown = f.read()
    
    with open(template_path, 'r') as f:
        template = f.read()

    title = extract.extract_title(markdown)
    content = convert.markdown_to_html_node(markdown).to_html()

    page = template.replace('{{ Title }}', title).replace('{{ Content }}',content)

    with open(dest_path, 'w') as f:
        f.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        print('dir_path_content does not exist')
        sys.exit(-1)

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # copy source
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(from_path) and from_path.endswith('.md'):
            generate_page(from_path, template_path, dest_path.split('.md')[0]+'.html')
        else:
            # recursive directory call
            generate_pages_recursive(from_path, template_path, dest_path)