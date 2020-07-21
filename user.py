class User:
    """Modelling some users."""
    def __init__(self, first_name, last_name, age, gender):
        """Initializing attributes for user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        """Describing a user."""
        if self.gender == 'male':
            print(f"User's name is {self.first_name.title()} {self.last_name.title()}. He is {self.age} and his gender in {self.gender}.")
        elif self.gender == 'female':
            print(f"User's name is {self.first_name.title()} {self.last_name.title()}. She is {self.age} and her gender in {self.gender}.")
        else:
            print(f'Wrong gender, you should be male or female.')

    def greet_user(self):
        """Simulate user's greeting."""
        print(f"How's it going, {self.first_name.title()}? We hope you will enjoy programming!")

user1 = User('pavlo', 'prykhodko', 25, 'male')

print(f'\nUser {user1.first_name.title()} {user1.last_name.title()} aged {user1.age} is a {user1.gender}')
user1.describe_user()
user1.greet_user()

user2 = User('alina', 'punko', 19, 'female')
print(f'\nUser {user2.first_name.title()} {user2.last_name.title()} aged {user2.age} is a {user2.gender}')
user2.describe_user()
user2.greet_user()