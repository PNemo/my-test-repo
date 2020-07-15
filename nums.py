words = {
'if': 'is a very useful statement',
'for': 'helps you to create loops',
'upper': 'makes an instant CapsLock',
'append': 'adds a new position to the existed list or dictionary',
'del' : 'deletes an element from the list',
'list' : 'stores data which you can edit',
'tuple' : 'stores uneditable data',
'nest' : 'can store lists and dictionaries in themselves',
'sort' : 'sorts elements in the alphabet order',
'get' : 'prints a value from each element of dicrionary'
}

for word, defin in words.items():
    print(f'{word.title()} in Python {defin}.')

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
    if key == 'username':
        print(f"\nKey: {key}")
        print(f"Value: {value}")
    else:
        print(f"\nKey: {key}")
        print(f"Value: {value.title()}")