#Project
print("Welcome to the Rollarcostar !!!")
heigth = int(input("What is your height in cm ? "))

if heigth > 120 :
	print("You can ride the Rollarcostar !")
	age = int(input("What is your age ? "))
	bill = 0
	
	if age < 12:
		bill += 5
		print("Child tickets are $5.")	
	elif age <= 18:
		bill += 7
		print("Youth tickets are $7.")	
	elif age >= 45 and age <= 55:
		bill += 0
		print("Midlife Crisis people can ride free")
	else:
		bill += 12
		print("Adult tickets are $12.")

	photo = input("Do you want to take photos ? Y / N. ")
	if photo == "Y":
		bill += 3
	print(f"Your final bill is ${bill}")
	
else:
	print("Sorry, you have to grow taller before you can ride.")