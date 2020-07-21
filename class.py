class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")

mydog = Dog("jimbo", "12")
yourdog = Dog("keke", "7")

print(f"My dog's name {mydog.name.title()} and he is {mydog.age}!")
mydog.sit()
mydog.roll_over()

print(f"My dog's name {yourdog.name.title()} and she is {yourdog.age}!")
yourdog.sit()
yourdog.roll_over()