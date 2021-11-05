#person
# per_inf={'first_name':'vadim','last_name':'rusu','age':'38','city':'seattle'}
# print(per_inf)
#personal numbers
# per_numb={'a':123,'b':456,'c':789,'d':987,'f':654}
#print(per_numb['a'])

# for key,value in per_numb.items():
#     print(f'the name {key} has the following definition: {value} which is the favorite number')

# for key in per_numb:
#     print(key,per_numb[key])

# [print(key,':',value) for key,value in per_numb.items()]

#glossary
# glossary={'dictionary':'the collection type','lists':'uses square brackets','tuples':'has the parenthesis'}

# for key,value in glossary.items():
    # print(f'I know that {key} is a {value}')

# for value in glossary.values():
#     print(value)

# for key in glossary.keys():
#     print(key)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(name)
#     if name in friends:
#         print(name)

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")
# rivers={'nile':'egypt','amazon':'brasil','lena':'russia'}
# for river,country in rivers.items():
    # print(f'the {river} runs through {country}')
# for river in rivers:
#     print(river)
# for country in rivers.values():
#     print(country)

# favorite_languages = {'jen': 'python','edward': 'ruby'}
# names = ['phil','sarah','jen','edward']
# for name in names:
#     if name in favorite_languages:
#         print(f'thanks {name} for vote')
#     else:print(f'{name} invited to vote')

#people
# people=['staf_1':{'jen':'python','edward':'ruby'},'staf_2':{'phil':'java','sarah':'c++'},'staf_3':{'kay':'c#','nic':'r'}]
# staf_1={'first_name':'vadim','last_name':'rusu','age':'38','city':'seattle'}
# staf_2={'first_name':'nic','last_name':'jul','age':'38','city':'bellevue'}
# staf_3={'first_name':'di','last_name':'ru','age':'42','city':'redmond'}
# people=[staf_1,staf_2,staf_3]

# for staf in people:
#     print(staf)

#pets
# cat={'color':'red','owner':'me'}
# dog={'color':'yellow','owner':'he'}
# pets=[cat,dog]
# for pet in pets:
#     print(pet)

#favorite places
# favorite_places={'adam':['mayorca'],
#                 'vadim':['hawaii','new zeland','australia'],
#                 'di':['rome','germany']}
# for name,places in favorite_places.items():
#     if len(places)==1:
#         print(f'')
#     print(f'\n{name} favorite places are')
#     for place in places:
#         print('t',place)

#favorite number
# favorite_number={'jen':[1,2],
#                 'adam':[3,11],
#                 'kile':[7,12],
#                 'mur':[4,13],
#                 'heily':[9,19]}
# print(favorite_number)

#cities
cities={'seattle':{'country':'usa',
                    'population':'350m',
                    'fact':'best'},
        'melbourn':{'country':'australia',
                    'population':'80m',
                    'fact':'hot'},
        'tokyo':{'country':'japan',
                'population':'140m',
                'fact':'best of the best'}
}
for city,info_cities in cities.items():
    print('\n',city)
    
    country=f"the country is {info_cities['country']}"
    population=f"the population is {info_cities['population']}"
    fact=f"the fact is {info_cities['fact']}"
    
    print('\t',country)
    print('\t',population)
    print('\t',fact)
    if info_cities['population']=='80m' in info_cities['population']:
            info_cities['population']='100m'
            print(f'\t the population is rised by 20m')