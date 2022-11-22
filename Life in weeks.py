#Life in weeks program logic

age = int(input("Enter your current age :\n"))
bal= 90 - age
days,weeks,months = 365*bal,52*bal,12*bal
print(f"you have {days} days, {weeks} weeks, and {months} months left.")
