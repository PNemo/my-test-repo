def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def make_sandwich(bread, *toppings):
    """Creates a proper sandwich"""
    print(f'\nMaking a sandwich with {bread} bread and these toppings:')
    for topping in toppings:
        print(f'> {topping.title()}')

make_sandwich('white', 'mayonnaise')


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('pavlo', 'prykhodko',
            location='sloviansk',
            language='python',
            favorite_dish='pizza')

for parameter, name in user_profile.items():
    print (f'\n> {parameter.title()}: {name.title()}')

def build_car(brand, body, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['brand'] = brand
    user_info['body'] = body
    return user_info

car = build_car('toyota', 'hatchback', color = 'blue', tow_package = True)

print(car)