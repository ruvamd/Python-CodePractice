class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f'the restaurant name is {self.restaurant_name} and cuisine type {self.cuisine_type} was served {self.number_served} times')

    def set_number_served(self,number):
        self.number_served=number
    
    def increment_number_served(self,cust_number):
        self.number_served+=cust_number

# restaurant=Restaurant('la plachinte','moldavian')
# restaurant.describe_restaurant()

# restaurant.number_served=24
# print(f'was served {restaurant.number_served} times')

# restaurant.set_number_served(4)
# restaurant.describe_restaurant()

# restaurant.increment_number_served(222)
# restaurant.describe_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['vanile','berry','cherry','mango']

    def display_flavors(self):
        print(f'the flavor of the ice cream{self.flavors}')

ice_cream=IceCreamStand('ice berg','ice cream')
ice_cream.display_flavors()
            