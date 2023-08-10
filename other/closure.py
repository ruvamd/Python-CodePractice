def transmit_to_space(message):
    'this is enclosing function'
    def data_transmitter():
        'the nested function'
        print(message)
    data_transmitter()
print(transmit_to_space('test message'))