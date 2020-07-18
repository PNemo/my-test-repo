sandwiches = ['pastrami', 'mushroooms and cheese', 'pastrami', 
            'eggs and bacon', 'pastrami', 'salami']
f_sandwiches = []

print(sandwiches)

print(f'\nSorry, but our cafe run out of pastrami!\n')

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

print(sandwiches)

while sandwiches:
    sandw = sandwiches.pop()
    print(f"Making sandwich with {sandw.title()}")
    f_sandwiches.append(sandw)

print("These sandwiches are ready: ")

for f_sandwich in f_sandwiches:
    print(f'\n{f_sandwich.title()}')

responses = {}

polling_active = True

while polling_active:
# Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Where would you like to have a vacation ")
# Store the response in the dictionary.
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person take a poll? (yes / no) ")
    if repeat == 'no' or 'n':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Here are the poll results ---")
for name, response in responses.items():
    print(f"{name} would like to have a vacation in {response}.")