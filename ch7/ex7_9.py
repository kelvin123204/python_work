sandwich_orders = ["Pastrami", "Bacon", "Egg",
                   "Pastrami", "BLT", "Bosna", "Pastrami", "BLT",
                   "Bosna", "Pastrami", "Egg"]
fished_sandwichs = []
print("We run out of Pastrami")
print(sandwich_orders)
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
while sandwich_orders:
    fished_sandwich = sandwich_orders.pop()
    fished_sandwichs.append(fished_sandwich)
    print("I made your " + fished_sandwich + " sandwich.")
print("\nFinished sandwich :")
while fished_sandwichs:
    print(fished_sandwichs.pop())
