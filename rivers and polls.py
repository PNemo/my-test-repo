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


plangs = {'clyde' : 'python', 
        'jim' : 'c', 
        'ibrahim' : 'java', 
        'harry' : 'fasm', 
        'lee' : 'c++'
}

people = ['clyde', 'peter', 'josh', 'jim', 
        'ibrahim', 'erza', 'harry', 'lee'
]

for man in people:
    if man in plangs.keys():
        print(f'\nThanks for taking a poll, {man.title()}!')
    else:
        print(f'\nPlease take a poll, {man.title()}.')