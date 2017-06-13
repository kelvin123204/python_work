prompt = "You can input what toppings do you want"
prompt += "\nYou can input 'quit' to exit the program\n"
flag = True
while (flag):
    topping = input(prompt)
    if(topping != "quit"):
        print("I will add " + topping + " to the pizza!")
    else:
        flag = False
