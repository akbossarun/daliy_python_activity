print("!!! (✿◠‿◠)....Welcome to the Love Calculator..(✿◠‿◠) !!!\n")
name1 = input("(✿◠‿◠)..what is your name? ")
name2 = input("(✿◠‿◠)..what is their name? ")

combined_string = name1+name2
lower_string = combined_string.lower()
t,r,u,e = lower_string.count('t'),lower_string.count('r'),lower_string.count('u'),lower_string.count('e')
l,o,v,e = lower_string.count('l'),lower_string.count('o'),lower_string.count('v'),lower_string.count('e')
true = t+r+u+e
love = l+o+v+e
love_score = int(str(true)+str(love))

if love_score <=10 or love_score >= 90:
	print(f"\n(✿◠‿◠)...Your score is {love_score}, you go together like coke and mentos...")
elif love_score >= 40 and love_score <=50:
	print(f"\n(✿◠‿◠)...Your score is {love_score}, you are alright together.")
else:
	print(f"\n(✿◠‿◠)...Your score is {love_score}.")

