def messages(message_pool, new_messages):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while message_pool:
        current_message = message_pool.pop()
        print(f"Fetching message: {current_message}")
        new_messages.append(current_message)

def show_new_messages(new_messages):
    """Show all the models that were printed."""
    print("\nThe following messages have been fetched:")
    for new_message in new_messages:
        print(new_message)

message_pool = ['we love you', 'you will stand against everything', 'perserve and deliberate']
new_messages = []

messages(message_pool[:], new_messages)
show_new_messages(new_messages)

print(message_pool)
print(new_messages)