"Write a function that takes an integer value and returns its binary representation as a string."
convert_to_binary = lambda n: bin(n)[2:]
print(convert_to_binary(10))

convert_to_decimal = lambda n: int(n, 2)
print(convert_to_decimal('1010'))
