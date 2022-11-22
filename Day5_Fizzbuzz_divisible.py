l = []
for x in range(1,101):
	if x % 15 == 0:
		l.append("FizzBuzz")	
	elif x % 3 == 0:
		l.append("Fizz")
	elif x % 5 == 0:
			l.append("Buzz")
	else:
		l.append(x)	

for num in l:
	print(num)
'''
for number in range(1,101):
	if number % 3 == 0 and number % 5 == 0:
		print("FizzBuzz")
	elif number % 3 == 0:
		print("Fizz")
	elif number % 5 == 0:
		print("Buzz")
	else:
		print(number)
'''