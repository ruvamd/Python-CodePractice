class duck:
    sound='crea'
    movement='walk'
    def crea(self):
        print(self.sound)
    def move(self):
        print(self.movement)
def main():
    donald=duck()
    donald.crea()
    donald.move()
main()