prompt = "\nPlease enter your age to let us know which price " 
prompt += "will be established for your ticket: "

y = 1

while True and y <= 5:
    y += 1
    age = int(input(prompt))
    if 3 > age > 0:
        print(f"You shouldn't pay for a ticket! Have fun")
    elif 12 >= age >= 3:
        print(f"You should pay $10! Have fun")
    elif age > 12:
        print(f"You should pay $15! Have fun")
    else:
        print(f"Please, enter a proper age: ")