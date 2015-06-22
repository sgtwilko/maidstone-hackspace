from scaffold.web import www

class control(www.default.html_ui):

    def create(self, cols=2):
        self.cols = []
        self.current_column = 0
        for c in range(0, cols):
            self.cols.append([])
        return self

    def next_column(self):
        for c in self.cols:
            yield ''.join(c)

    def append(self, content):
        if self.current_column > len(self.cols)-1:
            self.current_column = 0
        self.cols[self.current_column].append(content)
        self.current_column += 1

    def render(self):
        return '<div>%s</div>' % '</div><div>'.join(self.next_column())