def get_city(city, country):
    """Returns a city and a country."""
    full_info = f"{city}, {country}"
    return full_info.title()

pair = get_city('kyiv', 'ukraine')

def build_album(name, title, song_num=None):
    """Return a dictionary of information about a person."""
    album = {'art_name': name, 'alb_title': title}
    if song_num:
        album['song_num'] = song_num
    return album

while True:
    print("\nPlease add the artist and the album:")
    print("(enter 'q' at any time to quit)")
    art = input("Artist: ")
    if art == 'q':
        break

    alb = input("Album: ")
    if alb == 'q':
        break

    alb_form = build_album(art, alb)
    print (f'Here is the {alb_form}')

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"\nHello, {name.title()}, how was your day?"
        print(msg)

usernames = ['big lou', 'ibrahim', 'cockman']
greet_users(usernames)

def messages(msgs):
    """Print a simple greeting to each user in the list."""
    for msg in msgs:
        msg = f"\nThe message of the day is '{msg}'!"
        print(msg)

message_pool = ['we love you', 'you will stand against everything', 'perserve and deliberate']
messages(message_pool)