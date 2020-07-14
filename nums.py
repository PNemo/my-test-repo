words = {
'if': 'is a very useful statement',
'for': 'helps you to create loops',
'upper': 'makes an instant CapsLock',
'append': 'adds a new position to the existed list or dictionary',
'del' : 'deletes an element from the list'
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