cat = 'animal'
print (f"Is cat an animal? It have to be true.")
print (cat == 'animal')

cat = 'animal'
print (f"Is cat a camel? It have to be not true.")
print (cat == 'camel')

spartans = 300
persians = 280

print (spartans >=250 and persians >= 250)
print (spartans >=300 and persians >= 300)
print (spartans == 300 or persians == 300)

dish = 'Lavash'
dish.lower() == 'lavash'

print (dish.lower() == 'lavash')

spices = ['salt', 'pepper', 'cinnamon', 'cognac']

if 'cock' not in spices:
    print(f'Salty!')
else:
    print(f'Where is my salt?')