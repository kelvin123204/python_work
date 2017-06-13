sandwich_orders = ["Bacon", "Egg", "BLT", "Bosna"]
fished_sandwichs = []
for sandwich_order in sandwich_orders:
    print("I made your " + sandwich_order + " sandwich.")
    fished_sandwichs.append(sandwich_order)
print("\nFinished sandwich :")
while fished_sandwichs:
    print(fished_sandwichs.pop())
