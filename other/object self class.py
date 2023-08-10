class Duck:
    sound='quaaack!'
    walking='walks like a duck'
    def quack(self):
        print(self.sound)
    def walk(self):
        print(self.walking)
def main():
    donald=Duck()
    donald.quack()
    donald.walk()
main()
