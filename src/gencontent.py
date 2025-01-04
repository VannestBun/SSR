import os
from markdown_blocks import markdown_to_html_node

# def generate_page(from_path, template_path, dest_path):
#     print(f"Generating page from {from_path} to {dest_path} using {template_path}")

#     with open(from_path) as f:
#         markdown_content = f.read()
#     print(markdown_content)

#     with open(template_path) as f:
#         template_content = f.read

    
#     html_node = markdown_to_html_node(from_path)
#     html_string = html_node.to_html()

#     extract_markdown_title()



def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        # Get full paths
        source_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        
        # Handle markdown files
        if os.path.isfile(source_path) and entry.endswith(".md"):
            # Convert .md to .html in destination path
            dest_path = dest_path.replace(".md", ".html")
            generate_page(source_path, template_path, dest_path)
            
        # Handle directories
        elif os.path.isdir(source_path):
            # Create the directory if it doesn't exist
            os.makedirs(dest_path, exist_ok=True)
            # Recurse into the directory
            generate_pages_recursive(source_path, template_path, dest_path)

            




# def extract_markdown_title(markdown):
#     if markdown.startswith(("# ")):
#         text = markdown[2:]
#         return text
#     else:
#         raise ValueError("no heading")