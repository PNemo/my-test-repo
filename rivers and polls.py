rivers = {'nile' : 'egypt',
        'gang' : 'india',
        'dnipro' : 'ukraine',
        'murom' : 'rushka',
        'mekong' : 'vietnam'
        }

for riv, country in rivers.items():
    print(f'{riv.title()} is running through {country.title()}.')

for river in rivers.keys():
    print(f'\n{river.title()}')

for coun in rivers.values():
    print(f'\n{coun.title()}')