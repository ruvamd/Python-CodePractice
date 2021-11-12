def sandwiches(*toppings):
    for item in toppings:
        print(f'topping {item}')
    summary=f"the sandwith has {toppings} toppings"
    print(summary)

sandwiches('a','b','c')


