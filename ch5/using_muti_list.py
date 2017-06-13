avaliable_toppings = ["mushroom","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings = ["mushroom","olives","french fries"]
for requested_topping in requested_toppings:
	if requested_topping in avaliable_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have the requested topping " + requested_topping+".")
