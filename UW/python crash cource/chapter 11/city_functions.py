def city_country(city,country,population=''):
    if population:
        city_country_name=(f'{city} {country} {population}')
    else:
        city_country_name=(f'{city} {country}')
    return city_country_name.title()