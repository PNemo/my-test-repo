frone = {'jayden' : [23, 17], 'hermos' : [75, 33], 'claud' : [19, 22]}

for name, numbers in frone.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

cities = {
    'oklahoma' : {
        'country' : 'usa', 
        'people' : '370k', 
        'fact' : 'people moved from this place in 30s'
        }, 
    'sloviansk' : {
        'country' : 'ukraine', 
        'people' : '120k', 
        'fact' : 'this city survived after war conflict'
        }, 
    'paris' : {
        'country' : 'france', 
        'people' : '3800k', 
        'fact' : 'very dirty plase with huge amount of noise'
        }
    }

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = f"{city_info['country']}"
    population = f"{city_info['people']}"
    inter = f"{city_info['fact']}"
    if country == 'usa':
        print(f"\tCountry: {country.upper()}.")
        print(f"\tPopulation: {population}.")
        print(f"\tInteresting fact: {inter}.")
    else:
        print(f"\tCountry: {country.title()}.")
        print(f"\tPopulation: {population}.")
        print(f"\tInteresting fact: {inter}.")