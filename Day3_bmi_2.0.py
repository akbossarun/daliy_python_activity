# getting input from user 
heigth = float(input("enter your heigth in m: "))
weight = float(input("enter your weight in kg: "))

# calculating bmi as 2 floating point eg. 16.80
cal = weight/pow(heigth, 2)
bmi = round(cal, 2)

# checking these conditions and print the values and messages
if bmi <= 18.5:
	bmi = int(round(bmi, 0))
	print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi <= 25 :
	bmi = int(round(bmi, 0))
	print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi <= 30:
	bmi = int(round(bmi, 0))
	print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi <= 35:
	bmi = int(round(bmi, 0))
	print(f"Your BMI is {bmi}, you are obese.")
else:
	bmi = int(round(bmi, 0))
	print(f"Your BMI is {bmi}, you are clinically obese.")
