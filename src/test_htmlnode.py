import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode(
            "a",
            "Click here", 
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
    def test_values(self):
        node = HTMLNode(
            "a",
            "Hello",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.tag,
            "a"
        )
        self.assertEqual(
            node.value,
            "Hello"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            {"href": "https://www.google.com", "target": "_blank"}
        )

    def test_repr(self):
        node = HTMLNode(
            "a",
            "Hello",
            None,
            {'href': 'https://www.google.com', 'target': '_blank'}
            # {"href": "https://www.google.com"}, -> Course solution
        )
        self.assertEqual(
            node.__repr__(),
            "tag=a, value=Hello, children=None, props={'href': 'https://www.google.com', 'target': '_blank'}"
            # "HTMLNode(a, Hello, children: None, {'href': 'https://www.google.com'})" # -> Course solution
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(
            "p",
            "this is paragraph"
        )
        self.assertEqual(
            node.to_html(),
            "<p>this is paragraph</p>"
        )
    def test_to_html_anchor_tag(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )
    def test_no_tag(self):
        node = LeafNode(
            None,
            "no tag",
        )
        self.assertEqual(
            node.to_html(),
            'no tag'
        )

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    def test_nesting_parent_node(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")]),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold text</b>Normal text</p></div>"
        )
    def test_no_children(self):
        node = ParentNode(
            "div",
            []
        )
        self.assertEqual(
            node.to_html(),
            "<div></div>"
        )
    def test_children_with_anchor_tags(self):
        node = ParentNode(
            "p",
            [
                LeafNode(
                    "a",
                    "Click me!",
                    {"href": "https://www.google.com", "target": "_blank"}
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><a href="https://www.google.com" target="_blank">Click me!</a>Normal text</p>'
        )
    
        
        
if __name__ == "__main__":
    unittest.main()