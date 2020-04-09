dishes=['bowl','plate','cup']

for dish in list(dishes):
    print(f'putting {dish} in the sink')
    dishes.remove(dish)