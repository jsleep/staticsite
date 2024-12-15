from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None) -> None:
        if tag == None:
            raise ValueError('expected tag to not be None')
        if children == None:
            raise ValueError('expected children to not be None')
        super().__init__(tag, None, children, None)
    
    def to_html(self):
        l = []
        if self.props:
            open = f'<{self.tag} {self.props_to_html()}>'
        else:
            open = f'<{self.tag}>'
        close = f'</{self.tag}>'
        l.append(open)
        for child in self.children:
            l.append(child.to_html())
        l.append(close)
        return ''.join(l)
        
