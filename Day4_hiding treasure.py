# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜"]
row3 = ["⬜️","⬜️","⬜️"]
mapa = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#32
horizonal = int(position[0])#3
vertical = int(position[1])#2
selected_row = mapa[vertical - 1]
selected_row[horizonal - 1] = "X"
'''
mapa[vertical -1][horizonal-1] = "X"
'''
#Write your code above this row 👆

#🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")