print("{0_0}...Welcome to the tip calculator..!!")
bill = float(input("What was the total bill ? "))
tip = int(input("what percentage tip would you like to give ? 10,12 or 15 ? "))
split = int(input("How many people to split the bill ? "))
total_bill = ((tip / 100)*bill) + bill
total = total_bill/split
val = round(total, 2)
print(f"Ecah person should pay : {val:.2f}")
#print("{:.3f}".format(val))