import urllib.request
def main():
    webUrl=urllib.request.urlopen('http://google.com')
    print('result code: '+str(webUrl.getcode()))
    data=webUrl.read()
    print(data)
main()