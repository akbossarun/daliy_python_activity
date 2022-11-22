import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# 345234
# Angela, Jane, Jeremy, Tom, Robin
# 352354234
# Tom, Dick, Harry

#Write your code below this line 👇
last = len(names[-1])
toss = random.randint(0,last)-1
print(last,toss)
print(names[toss],"is going to buy the meal today!")


