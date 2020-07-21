class Restaurant:
    """Modelling restaurants."""
    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes."""
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """Describing a restaurant."""
        print(f"Welcome to the {self.name.title()} restaurant! We provide you {self.cuisine.title()} cuisine.")
    
    def res_open(self):
        """Simulate opening a restautant."""
        print(f"{self.name.title()} is open for customers and it's ready to fill you!")
    
res1 = Restaurant('manjomdo', 'korean')
print(f'\nFood in the {res1.name.title()} restaurant with {res1.cuisine.title()} cuisine is absolutely gorgeous!')
res1.describe_restaurant()
res1.res_open()

res2 = Restaurant('hlek', 'ukrainian')
print(f'\nFood in the {res2.name.title()} restaurant with {res2.cuisine.title()} cuisine is absolutely gorgeous!')
res2.describe_restaurant()
res2.res_open()

res3 = Restaurant('baba yetu', 'african')
print(f'\nFood in the {res3.name.title()} restaurant with {res3.cuisine.title()} cuisine is absolutely gorgeous!')
res3.describe_restaurant()
res3.res_open()