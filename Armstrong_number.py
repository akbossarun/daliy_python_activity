def is_Armstrong(num):
    digits, last, result = 0,0,0
    temp = num
    while temp>0:
        temp=int(temp/10)
        digits +=1
    
    temp = num
    while(temp>0):
        last=int(temp%10)
        result += pow(int(last), int(digits))
        temp = int(temp/10)
        
    if num==result:
        return True
    else:
        return False
    
for i in range(1000):
   if is_Armstrong(i):
       print(i," is a Armstrong Number")