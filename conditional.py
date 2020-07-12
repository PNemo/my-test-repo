age = int(input('Enter your age, please: '))
name = input('Enter your name, please: ')

if age < 4:
    print(f'Step freely wighout charge, {name.title()}.')
elif age >=4 and age < 18:
    print(f'Hey, {name.title()}, you have to pay $25!')
else:
    print(f'Pay 40 bucks, {name.title()}.')

print('\n\n')

alien = 'yellow'

if alien == 'green':
    print(f'You have earned 5 points!')
elif alien == 'red':
    print (f'You have earned 10 points!')
else:
    print(f'You have earned 15 points!')

favorite_fruits = ['apples', 'bananas', 'kivis', 'oranges', 'watermelons']

if 'bananas' in favorite_fruits:
    print(f'Enjoying your babanas, huh?')
if 'kivis' in favorite_fruits:
    print(f'Do you like New Zealand?')
if 'cranberries' not in favorite_fruits:
    print(f'Zombies are not your passion anymore...')
