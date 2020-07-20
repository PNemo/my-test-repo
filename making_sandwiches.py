def make_sandwich(bread, *toppings):
    """Creates a proper sandwich"""
    print(f'\nMaking a sandwich with {bread} bread and these toppings:')
    for topping in toppings:
        print(f'> {topping.title()}')