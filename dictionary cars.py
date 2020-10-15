def car_listing(car_prices):
  result = ""
  for key in car_prices:
    result += f"{key} costs {car_prices[key]} dollars, "
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))