# import os
# import shutil

# from markdown_blocks import markdown_to_html_node
# from htmlnode import HTMLNode


# def main():
#     copy_static()
#     print(extract_markdown_title("# Hello"))

    
    

# def copy_static():
#     dest_path = "public/"
#     source_path = "static/"
#     if os.path.exists(dest_path): # check to clear existing stuff
#         shutil.rmtree(dest_path) #clears all public files and directory
#     os.mkdir(dest_path)
#     # Start the recursive copy from static to public
#     copy_recursive(source_path, dest_path) 
    
# def copy_recursive(src, dst):

#     print(os.listdir(src), "this is listdir(src)")
#     # output: ['images', 'index.css'] this is listdir(src)
#     # ['rivendell.png']


#     for item in os.listdir(src):
#         src_path = os.path.join(src, item)
#         # static/images, static/index.css..
#         print(src_path, "src_path")

#         dst_path = os.path.join(dst, item)
#         print(dst_path, "dst_path")
#         # public/images, public/index.css..
        
#         if os.path.isfile(src_path):
#             shutil.copy(src_path, dst_path)
#         else:
#             os.mkdir(dst_path)
#             # Pass the new source and destination paths
#             copy_recursive(src_path, dst_path) 

# def extract_markdown_title(markdown):
#     if markdown.startswith(("# ")):
#         text = markdown[2:]
#         return text
#     else:
#         raise ValueError("no heading")


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





# if __name__ == "__main__":
#     main()


import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Creating public directory...")
    os.makedirs(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    # Note: we pass directories now, not individual files
    generate_pages_recursive(
        dir_path_content,  # content directory
        template_path,     # template file
        dir_path_public    # public directory
    )


main()