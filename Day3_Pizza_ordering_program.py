print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")
pizza_cost = 0

# Checking the pizza size and updating the pizza cost
if size == "S":
	pizza_cost += 15
elif size == "M":
	pizza_cost += 20
elif size == "L":
	pizza_cost += 25

# Adding Pepperoni and updating the pizza cost
if pepperoni == "Y" and size == "S":
	pizza_cost += 2
if pepperoni == "Y" and (size == "M" or size == "L"):
	pizza_cost += 3
'''
# Adding Pepperoni and updating the pizza cost
if pepperoni == "Y":
	if size == "S":
		pizza_cost += 2
	else:
		pizza_cost += 3
'''
# Adding cheese and updating the pizza cost
if cheese == "Y":
	pizza_cost += 1 

print(f"Your final bill is: ${pizza_cost}.")