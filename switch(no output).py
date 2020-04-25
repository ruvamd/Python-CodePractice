specials={'sunday':'spinach',
          'monday':'mushrooms',
          'tuesday':'pepperoni',
          'wednesday':'veggie',
          'thursday':'bbq chicken',
          'friday':'sausage',
          'saturday':'hawaiian'}
def order(day):
    pizza=specials[day]
    print(f'order the {pizza} pizza')