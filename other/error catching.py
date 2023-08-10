import urllib.request
try:
    webpage=urllib.request.urlopen('http://goog.le')
except:
    print('Could not access webpage!')
else:
    for line in webpage:
        print(line)
        