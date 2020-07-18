def greet_user():
    x = input("What is your name? ")
    """Display a simple greeting."""
    print(f'Hello, {x.title()}!')

def print_message():
    """Displays a message."""
    print(f'We learned a lot about functions today!')

def fav_book(book):
    """Display a simple greeting."""
    print(f'My favorite book is {book}')

def make_shirt(size = 'l', text = 'i love Python'):
    """Prints a text on a shirt for you"""
    print (f'Your shirt with size {size.title()} and text "{text}" will be ready soon!')

def describe_city(city, country = 'ukraine'):
    """Prints a city in a certain country"""
    print (f'{city.title()} is located in {country.title()}.')

describe_city('kharkiv')
describe_city('lviv')
describe_city('nizza', 'italy')