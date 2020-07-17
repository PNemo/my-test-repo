car = input('What kind of car do you want? ')

print(f'Let me see if I can offer you {car}.')

people = int(input('How many people are in your party? '))

if people > 8:
    print(f'You have to wait for a table with a sufficient amount of seats.')
elif people <= 0:
    print(f"Are you sure that you don't exist?")
else:
    print(f'Welcome aboard!')


num = int(input("Let me see if it is a multiple of ten. Put here a number: "))

if num % 10 == 0:
    print(f'Sure {num} is a multiple of ten!')
else:
    print(f'Sorry, but {num} is not a multiple of ten...')
