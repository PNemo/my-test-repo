# in this game you'll need to guess random number from 1 to 100
# here we go!
import random

print('\t\t\tGreetings, traveller. Sit down and have some rest.\t\t\t')
print('\t\t\tRelax with our simple, but really astonishing game!\t\t\t')

num = random.randint(1, 100)
pnum = int(input('\nChoose your number: '))
attempt = 1

while pnum != num:
    attempt += 1
    if attempt == 10:
        print('\nYou tried so hard...')
        break
    if pnum > num:
        print('\nWrong, babe, it is less. It is your', attempt, 'attempt')
        pnum = int(input('Select again: '))
    elif pnum < num:
        print('\nWrong, babe, it is bigger. It is your', attempt, 'attempt')
        pnum = int(input('Select again: '))
else:
    print('\nVerrry nice. It was really', pnum, end='!')

input('\n\nPress Enter to finish')
