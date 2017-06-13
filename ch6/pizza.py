pizza1 = {"crust": "Thick", "Topping": ["mushroom", "extra cheese"]}
pizza2 = {"crust": "Thin", "Topping": ["extra cheese"]}
pizzas = [pizza1, pizza2]
for pizza in pizzas:
    print("You ordered a " + pizza["crust"] +
          "-crust pizza with the following topping(s) :")
    for topping in pizza["Topping"]:
        print(topping).capitalize()
