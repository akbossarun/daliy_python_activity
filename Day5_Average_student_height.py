# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
add = 0
count = 0
for x in student_heights:
  add += x
  count += 1
print(round(add/count))
#Write your code below this row 👇
