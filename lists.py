people = ['jimbo', 'felix', 
        'ibrahim', 'sous vide']

for man in people:
    print (f"Dear {man.title()}, please go with me for a dinner!")

people.insert(0, 'peter')
people.insert(3, 'paul')
people.append('cockman')

for man in people:
    print (f"Dear {man.title()}, please go with me for a dinner!")

print (people)

print(f'But I can invite only two people for a dinner!')
people.pop()
people.pop()
people.pop()
people.pop()
people.pop()

print (f'Dear {people[0].title()}, youre still invited!')
print (f'Dear {people[1].title()}, youre still invited!')

print (f'There are {len(people)} people who are still invited.')