from textnode import TextType, TextNode
import re 

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for old_node in old_nodes:
       if old_node.text_type != TextType.TEXT:
           new_list.append(old_node)
           continue
       
       split_nodes = []
       text_split = old_node.text.split(delimiter)

       if len(text_split) % 2 == 0:
           raise Exception("Invalid Markdown")
       
       for i in range(len(text_split)):
           if text_split[i] == "":
               continue
           if i % 2 == 0:
               new_list.append(TextNode(text_split[i], TextType.TEXT))  
           else:
               new_list.append(TextNode(text_split[i], text_type))
       new_list.extend(split_nodes)
    return new_list

def extract_markdown_images(text):
    matching_image_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matching_image_text

def extract_markdown_links(text):
    matching_link_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matching_link_text

def split_nodes_image(old_nodes):
     new_list = []
     for old_node in old_nodes:
         if old_node.text_type != TextType.TEXT:
           new_list.append(old_node)
           continue
         
         original_text = old_node.text
         images = extract_markdown_images(original_text)
         if len(images) == 0:
            new_list.append(old_node)
            continue

         for image in images:
             section = original_text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
             if len(section) != 2:
                raise ValueError("Invalid markdown, image section not closed")
             if section[0] != "":
                new_list.append(TextNode(section[0], TextType.TEXT))
             new_list.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1] #url
                )
            )
             original_text = section[1]
         if original_text != "":
                new_list.append(TextNode(original_text, TextType.TEXT))
     return new_list

def split_nodes_link(old_nodes):
     new_list = []
     for old_node in old_nodes:
         if old_node.text_type != TextType.TEXT:
           new_list.append(old_node)
           continue
         original_text = old_node.text
         links = extract_markdown_links(original_text)
         if len(links) == 0:
            new_list.append(old_node)
            continue

         for link in links:
             section = original_text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
             if section[0] != "":
                new_list.append(TextNode(section[0], TextType.TEXT))
             new_list.append(
                TextNode(
                    link[0],
                    TextType.LINK,
                    link[1] #url
                )
            )
             original_text = section[1]
         if original_text != "":
             new_list.append(TextNode(original_text, TextType.TEXT))
     return new_list

