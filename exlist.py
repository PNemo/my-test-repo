names = ['paul', 'john', 'archie', 'admin', 'jane']

if names:
    for name in names:
        if name == 'admin':
            print(f'You are doing kind of a hard work, {name.title()}!')
        else:
            print(f'Hello, {name.title()}!')
else:
    print(f'Where are all the users?')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f'{number}st\n')
    elif number == 2:
        print(f'{number}nd\n')
    elif number == 3:
        print(f'{number}rd\n')
    else:
        print(f'{number}th\n')