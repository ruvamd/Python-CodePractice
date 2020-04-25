def transmitToSpace(message):
    'this is the enclosing function'
    def dataTransmitter():
        'the nested function'
        print(message)
    return dataTransmitter

fun2=transmitToSpace('burn the sun!')
fun2()
