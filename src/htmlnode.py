
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML.")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

    # def __repr__(self):
    #     return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})" 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a value.")
        if self.children is None:
            raise ValueError("Parent node must have atleast one children node")
        results = ""
        for children in self.children:
            results += children.to_html()
        return f"<{self.tag}{self.props_to_html()}>{results}</{self.tag}>"
    
