from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('start tag:',tag)
        for attr in attrs:
            print('attr:',attr)
    def handle_endtag(self, tag):
        print('end tag:',tag)
    def handle_comment(self, data):
        print('comment:',data)
    def handle_data(self, data):
        print('data:',data)

parser=HTMLParser()
parser.feed('<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body>')
print()
input=input('put in html code:')
parser.feed(input)
print()