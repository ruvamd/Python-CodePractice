# combine two sorted list using sorted()

# initializing lists
list1 = [1, 5, 6, 9, 11]
list2 = [3, 4, 7, 8, 10]

# printing original lists
print ("list 1: " + str(list1))
print ("list 2: " + str(list2))

# using sorted() to combine two sorted lists
res = sorted(list1 + list2)

# printing result
print ("combined sorted list: " + str(res))


