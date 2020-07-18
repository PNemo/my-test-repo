prompt = "\nPlease ented some toppings which you would like to see in your pizza"
prompt += "\nYou may choose up to 3 toppings"

x = 0

while True and x <= 2:
    x +=1
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"You have successfully added {topping.title()} to your pizza!")


