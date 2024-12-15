from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        if value == None and props == None:
            raise ValueError('expected either value or props to not be None')
        if value == None:
            value = ""
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        open = ''
        close = ''
        if self.tag:
            if self.props:
                open = f'<{self.tag} {self.props_to_html()}>'
            else:
                open = f'<{self.tag}>'
            close = f'</{self.tag}>'
        return open+self.value+close