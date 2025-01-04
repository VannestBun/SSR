# import re

# block_type_paragraph = "paragraph"
# block_type_heading = "heading"
# block_type_code = "code"
# block_type_quote = "quote"
# block_type_olist = "ordered_list"
# block_type_ulist = "unordered_list"

# from htmlnode import ParentNode
# from inline_markdown import text_to_textnodes
# from textnode import text_node_to_html_node

# def markdown_to_blocks(markdown):
#     block_strings = []
#     split_markdown = markdown.split("\n\n")
#     for text in split_markdown:
#         if text:
#             block_strings.append(text.strip())
#     return block_strings

# def block_to_block_type(block):
#     match = re.match(r"^(#{1,6}) .+", block)
#     if match:
#         count = len(match.group(1))  # Count the number of '#' characters
#         return "heading", count
#     lines = block.split('\n')
#     if lines[0].startswith("```") and lines[-1].endswith("```"):
#         return "code"
#     if all(line.startswith(">") for line in lines):
#         return "quote"
#     if all(line.startswith("* ") or line.startswith("- ") for line in lines):
#         return "unordered_list"
#     expected_number = 1
#     is_ordered = True
#     for line in lines:
#         if not line.startswith(f"{expected_number}. "):
#             is_ordered = False
#             break
#         expected_number += 1
#     if is_ordered:
#         return "ordered_list"
#     else:
#         return "paragraph" 


# def markdown_to_html_node(markdown):

#     blocks = markdown_to_blocks(markdown)

#     children = []
#     parent_div = ParentNode("div", children)

#     for block in blocks:
#         block_type = block_to_block_type(block)
#         if "paragraph" == block_type:
#             text_childrens = text_to_textnodes(block)
#             paragraph_node = ParentNode("p", text_childrens)
#             children.append(paragraph_node)

#         if "heading" == block_type[0]:
#             text_childrens = text_to_textnodes(block)
#             heading_node = ParentNode(f"h{block_type[1]}", text_childrens)
#             children.append(heading_node)


#         if "code" == block_type:
#             code_node = ParentNode("code", text_to_textnodes(block))
#             pre_node = ParentNode("pre", [code_node])
#             children.append(pre_node)


#         if "quote" == block_type:
#             quote_text = text_to_textnodes(block.lstrip(">").strip())
#             quote_node = ParentNode("blockquote", quote_text)
#             children.append(quote_node)


#         if "unordered_list" == block_type:
#             items = block.split("\n")
#             li_nodes = []
#             for item in items:
#                 item_text = item.lstrip("- ").strip()
#                 item_children = text_to_textnodes(item_text)
#                 li_node = ParentNode("li", item_children)
#                 li_nodes.append(li_node)
#             ul_node = ParentNode("ul", li_nodes)
#             children.append(ul_node)

#         if "ordered_list" == block_type:
#             items = block.split("\n")
#             li_nodes = []
#             for item in items:
#                 item_text = item[item.find('.')+1:].strip()
#                 item_children = text_to_textnodes(item_text)
#                 li_node = ParentNode("li", item_children)
#                 li_nodes.append(li_node)
#             ol_node = ParentNode("ol", li_nodes)
#             children.append(ol_node)

#     return parent_div

# def text_to_children():
#     pass


from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)