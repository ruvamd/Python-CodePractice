def multiplication_table(start, stop):
	for x in range(1,10):
		for y in range(1,10):
			print(str(x*y), end=" ")
		print('\n')

multiplication_table(1, 3)
# Should print the multiplication table shown above