responses = {}
flag = True
while flag:
    name = input("What is your name? ")
    dream_vocation = input(
        "If you could visit one place in the world, where would you go? ")
    responses[name] = dream_vocation
    repeat = input("Do you want another person to response (yes/no)? ")
    if(repeat == "no"):
        break
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(name + " want to visit " + response)
