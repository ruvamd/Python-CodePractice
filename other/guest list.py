def guest_list(guests):
	for guest in guests:
		name,age,profession=guest
		print(f'{name} is {age} years old and works as {profession}')

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])