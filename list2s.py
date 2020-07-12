list = []
suggest = list.append(input(
        f'Enter your topping: '))

if 'pineapple' in list:
    print(f'Wow, we will prepare it!')
elif 'cheese' in list:
    print(f'Rocky, huh?')
else:
    print(f'Your pizza will be ready just in a moment!')


age = int(input(f'Enter your age: '))

if age < 2:
    print(f'You are like a little baby!')
elif 4 > age >= 2:
    print(f'You are a toddler.')
elif 13 > age >= 4:
    print(f'You are a kid.')
elif 20 > age >= 13:
    print(f'You are a teenager.')
elif 65 > age >= 20:
    print(f'You are an adult.')
elif age >= 65:
    print(f'You are an elder!')
