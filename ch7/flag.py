flag = True
message = ""
prompt = "\nYou can type 'quit' to exit the program"
prompt += "\nI can speak what you type in except 'quit':"
while flag:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(message)
flag = False
