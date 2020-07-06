people = ['jimbo', 'felix', 'ibrahim', 'sous vide']
message1 = f"Dear {people[0].title()}, please go with me for a dinner!"
message2 = f"Dear {people[1].title()}, please go with me for a dinner!"
message3 = f"Dear {people[2].title()}, please go with me for a dinner!"
message4 = f"Dear {people[3].title()}, please go with me for a dinner!"

print (message1 + '\n' + message2 + '\n' + message3 + '\n' + message4)
people.insert(0, 'peter')
people.insert(3, 'paul')
people.append('cockman')
message1 = f"Dear {people[0].title()}, please go with me for a dinner!"
message2 = f"Dear {people[1].title()}, please go with me for a dinner!"
message3 = f"Dear {people[2].title()}, please go with me for a dinner!"
message4 = f"Dear {people[3].title()}, please go with me for a dinner!"
message5 = f"Dear {people[4].title()}, please go with me for a dinner!"
message6 = f"Dear {people[5].title()}, please go with me for a dinner!"
message7 = f"Dear {people[6].title()}, please go with me for a dinner!"
print (message1 + '\n' + message2 + '\n' + message3 + '\n' + message4 + '\n' + message5 + '\n' + message6 + '\n' + message7)
print (people)

print(f'But I can invite only two people for a dinner!')
people.pop()
people.pop()
people.pop()
people.pop()
people.pop()

print (f'Dear {people[0].title()}, youre still invited!')
print (f'Dear {people[1].title()}, youre still invited!')

del people[0]
del people[0]

print (people)