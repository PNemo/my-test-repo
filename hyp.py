# this is a simple hypotenuse calculator
# just testing the work of "math" library
import math

print('\t\t\tWelcome to the HypCalc!\t\t\t')
print('\t\t\tI wish you will enjoy this simple, but very useful program.\t\t\t')

a = int(input('\n\nChoose length of the first cathetus: '))
b = int(input('Choose length of the second cathetus: '))


def hyp():
    return math.sqrt((a*a)+(b*b))

print('\nSo, here comes an answer! The hypotenuse equals to', hyp(), end='.')

input('\n\nPress Enter to quit program')
