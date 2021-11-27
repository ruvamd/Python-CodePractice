class Text:
    def __init__(self,text):
        self.text='text'
        # text=
    def show_text(self):
        print(f'{self.text}')

class Image:
    def __init__(self):
        self.image='image'
    
    def show_image(self):
        print(f'{self.image}')

class PageBuilder(Text):
    def __init__(self):
        super().__init__()
    def builder(self):
        print(self.text)

page_builder=PageBuilder.builder()
print(page_builder)