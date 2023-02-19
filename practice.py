# Python3 code to print happy valentine's
# day
import math

n = 10

# Initializing String to print in heart
message = " HappY Valentines DaY <3 "

# Position from where from top
# message box would be placed.
print_message = 4

# Add space if message length is odd
if (len(message) % 2 != 0):
	message += " "

# Outer loop to adjust length of upper
# part message is not handled in this part
for a in range(n):
	
	# To print space and variable accordingly
	for b in range(4 * n + 1):
		
		# Computing distance to print variable
		distance1 = math.sqrt(pow(a - n, 2) +
							pow(b - n, 2))
		distance2 = math.sqrt(pow(a - n, 2) +
							pow(b - 3 * n, 2))
							
		if (distance1 < n + 0.5 or
			distance2 < n + 0.5):
			print("*", end = "")
		else:
			print(" ", end = "")

	# Ending line after each iteration
	print()

# Printing the message part and lower
# part of heart. Outer loop handles
# depth of the heart.
for a in range(1, 2 * n):

	# For getting the lower curve of heart
	for b in range(a):
		print(" ", end = "")
		
	# Inner loop
	# handles the message and spaces accordingly
	for b in range(4 * n + 1 - 2 * a):
		
		# Checks if the height is in range of
		# message space
		if (a >= print_message - 1 and
			a <= print_message + 1):
			point = b - (4 * n - 2 *
					a - len(message)) // 2

			# Prints message after leaving
			# appropriate space
			if (point < len(message) and point >= 0):
				if (a == print_message):
					print(message[point], end = "")
				else:
					print(" ", end = "")
			else:
				print("*", end = "")

		else:
			print("*", end = "")

	print()

# This code is contributed by subhammahato348
