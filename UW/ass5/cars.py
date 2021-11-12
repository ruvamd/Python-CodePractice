def cars(manufacturer,model_name,**car_info):
    car_info['manuf']=manufacturer
    car_info['model']=model_name
    return car_info

cars_profile=cars('bmw','s5',
        color='red',
        year='2005')

print(cars_profile)