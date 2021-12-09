messages = {
    1: "hello",
    2: "goodbye",
}

for choice in [1, 2]:
    if choice == 1:
        assert messages[choice] == "hello"
    else:
        assert messages[choice] == "goodbye"

choice = 2
print(messages[choice])


def adder(number1, number2):
    return number1 + number2


def suber(number1, number2):
    return number1 - number2


todo = {
    1: adder,
    2: suber,
}

assert todo[2](3, 4) == -1
assert todo[1](3, 4) == 7
