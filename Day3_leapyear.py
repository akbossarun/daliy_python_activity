year = int(input("Which year do you want to check? "))

leap = year%4
leap1 = year%100
leap2 = year%400
'''
if leap == 0:
	if leap1 != 0 :
		print("Leap year.")
	elif leap2 == 0:
		print("Leap year.")
	else:
		print("Not leap year.")	
else:
	print("Not leap year.")
'''
if leap == 0:
	if leap1 == 0 :
		if leap2 == 0:
			print("Leap year.")
		else:
			print("Not leap year.")	
	else:
		print("Leap year.")	
else:
	print("Not leap year.")



