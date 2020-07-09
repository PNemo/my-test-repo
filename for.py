pizzas = ['joullienne', 'meaty', 
        'cheesy', 'creamy', 'savory']
fr_pizzas = pizzas[:]
for pizza in pizzas:
    print(f'Sure I do like {pizza.title()} with a couple of beers!\n')

print (f"The first three pizzas are: {pizzas[0:3]}")
print (f"The first three pizzas are: {pizzas[2:]}")
print (f"The first three pizzas are: {pizzas[-2:]}")

pizzas.append('unsalted butter')
fr_pizzas.append('salted caramel')

print(pizzas)
print(fr_pizzas)

print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(f'{pizza.title()}')

print (f"\nMy friend's favorite pizzas are:")
for fr_pizza in fr_pizzas:
    print(f'{fr_pizza.title()}')