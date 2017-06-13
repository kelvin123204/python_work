prompt = "You can input what toppings do you want"
prompt += "\nYou can input 'quit' to exit the program\n"
time = 0
while time < 3:
    topping = input(prompt)
    if(topping != "quit"):
        print("I will add " + topping + " to the pizza!")
    else:
        break
    time += 1
