print ("Hello, citizen! \nLet's play a game")

age = int(input('Enter your age: '))
name = input('Enter your name: ')
message = f'Hello, {name.title()}, it will be {2020 + (-(age - 100))} when you will be polluting this planet for an age!'
print ((message + '\n') * age)