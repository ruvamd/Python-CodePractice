base_62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def to_base_10(videoId):
    return sum([base_62.index(char) * (62 ** index) for index, char in enumerate(videoId[::-1])])

def to_base_62(number):
    base_10 = number
    base_62_string = ""
    while base_10 > 0:
        base_62_string = base_62[base_10 % 62] + base_62_string
        base_10 = base_10 // 62
    return base_62_string

print(to_base_10("LpuPe81bc2w"))
print(to_base_62(18327995462734721974))
