responses = {}
polling_act = True
while polling_act:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person response? (yes/no)")
    if(repeat == 'no'):
        polling_act = False
print("\n----- Poll Result -----")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
