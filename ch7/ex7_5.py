flag = True
price = 0
while flag:
    age = input("What is your age?\n")
    if age == 'quit':
        break
    if int(age) < 3:
        price = 0
        print("The ticket price is :$" + str(price))
    elif int(age) >= 3 and int(age) < 12:
        price = 10
        print("The ticket price is :$" + str(price))
    else:
        price = 15
        print("The ticket price is :$" + str(price))
