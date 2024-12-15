class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ''
        l = []
        for key in self.props:
            l.append(f'{key}="{self.props[key]}"')
        return ' '.join(l)

    def __repr__(self) -> str:
        return  f'''HTMLNode(
                    tag={self.tag}
                    value={self.value}
                    children={self.children}
                    props={self.props}
                )'''