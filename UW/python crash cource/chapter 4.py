# l=['a','b','c','d','f','j']

# l2=l[:]
# l3=l[:]

# print('the first three items in the list are:',l[:3])
# print('three items from the middle of the list are:',l2[1:4])
# print('the last three items in the list are:',l3[-3:])

#pizza
pizzas=['pepperoni','mashrooms','fourmeats']
friends_pizzas=pizzas[:]
pizzas.append('cheese')
friends_pizzas.append('veggie')

print('my favorites pizzas are:',[n for n in pizzas])
print('me friend ')