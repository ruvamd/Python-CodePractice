class revstr(str):
    def __str__(self):
        return self[::-1]
def main():
        hello=revstr('hello,world')
        print(hello)
main()
    