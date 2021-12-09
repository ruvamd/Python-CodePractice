import random
import pprint


class SomethingUseful:
    def __init__(self):
        self.magic_number = random.randint(1, 100)


def main():
    dictionary_of_classes = dict()
    for instance_key in range(20):
        dictionary_of_classes[instance_key] = SomethingUseful()

    for instance in dictionary_of_classes.values():
        print(instance.magic_number)

    pprint.pprint(dictionary_of_classes.items())


if __name__ == "__main__":
    main()
