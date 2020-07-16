# Make an empty list for storing aliens.
aliens = []

# Make 30 aliens.
for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien_number in range(10):
    new_alien = {'color': 'blue', 'points': 15, 'speed': 'moderate'}
    aliens.append(new_alien)
for alien_number in range(10):
    new_alien = {'color': 'red', 'points': 10, 'speed': 'fast'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens:
    print(alien)

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

frone = {'jayden' : 23, 'hermos' : 75, 'claud' : 19}
frwto = {'smith' : 25, 'colm' : 66, 'jenny' : 34}
frthree = {'elmo' : 89, 'peep' : 44, 'howl' : 54}

persons = [frone, frwto, frthree]

for element in persons:
    for name, number in element.items():
        print(f'Hello, {name.title()}, I know that your favorite number is {number}.')

p1 = {'zebra' : 'jill'}
p2 = {'ostrich' : 'vetal'}
p3 = {'armadillo' : 'ivan'}
p4 = {'cobra' : 'cockman'}

pets = [p1, p2, p3, p4]

for pet in pets:
    for specie, owner in pet.items():
        print(f'Here is the {specie} and its owner named {owner.title()}.')

travs = {'peter' : ['alaska', 'honduras'],
        'olivia' : ['mars', 'okhahoma'],
        'jesus' : ['jerusalem', 'mecca']
        }

print (f"Here is the Peter's favorite places: ")

for place in travs['peter']:
    print(f'\t {place.title()}')

print (f"Here is the Olivia's favorite places: ")

for place in travs['olivia']:
    print(f'\t {place.title()}')

print (f"Here is the Jesus' favorite places: ")

for place in travs['jesus']:
    print(f'\t {place.title()}')

