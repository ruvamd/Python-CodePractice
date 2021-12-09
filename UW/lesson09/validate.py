validate_my_data = dict()


def begins_with_a(name):
    if name[0] == "a":
        return True
    return False


validate_my_data["name"] = begins_with_a

name = "andy"

print(validate_my_data["name"](name))


for key, value in validate_my_data.items():
    print(value(name))


def print_report():
    pass


menu = {
    1: {"prompt": "Print report", "function": print_report},
    # 2: {},
}
