'''#0,1,2,3,4,5...,n Postive indexing (left to right)
#n....,-4,-3,-2,-1 negative indexing (right to left)
# [start : stop : step ] 3-1= 2

txt = "welcome" 
print(txt[-7:])
print(txt[::-2])
'''
# modify Strings (18/02 11.45am)
str1 = "        hello, UniVerse                "
#upper case method 1
print(str1.upper())
#lower case method 2
print(str1.lower())
#Remove Whitespace method 3
print(str1.strip())
#replace method 4
print(str1.replace("hello", "hi"))
#split method 5
str2= "apple Banana|Cherry|Guava" # ['Apple,Banana,Cherry,Guava']
str3 = str2.split("|") # separating by defaut (word spacing) 
print(str3)

#capitalize method 6
str1 = "  BCA student BCA BCA  " #|--->
print(str1.capitalize())

#title method 7
print(str1.title())
#count
print(str1.count("BCA"))
#find
print(str1.find("Q"))
#index
print(str1.index("student"))

#lstrip , rstrip
print(str1.lstrip())
print(str1.rstrip())

#swapcase
print(str1.swapcase())


