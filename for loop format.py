sink=['bowl','plate','cup']

for dish in list(sink):
    print(f'putting {dish} in the dishwasher')
    sink.remove(dish) 