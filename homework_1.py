# 1 
num1 = 10
num2 = 5 
num3 = num1 + num2
print (num3)

# 2
num1 = 7
num2 = 5
num2 = num1 // num2 
print (num2) 

# 3
num1 = 7
num2 = 5
num3 = num1 % num2  
print (num3) 

# 4
num1 = float(10.5)
num2 = float(7.7)
num3 = float(4.8)
num4 = float( num1 * num2 / num3 )
print (num4)

# 5
num1 = float(2.2 ** 3)
num2 = round (num1 / 2, 1) 
print (num2)

# 6
import math as mt
num1 = float(5.6)
num2 = float(7.49)
num6 = mt.floor(num1 - num2)
print (num6)

# 7
num1 = float (6.23)
num2 = float (7.45)
num7 = mt.ceil (num1 - num2)
print (num7)

# 8
a = 5
b = 7
num8 = mt.sqrt ( a**2 + b**2)
print (num8)

# 9 
pos_num = 5
neg_num = -7
num9 = abs(pos_num) + abs(neg_num)
print (num9)

# 10
temp = 90
num10 = round(((temp - 32) * (5/9)),2)
print (num10)

# 11
a = float (6 + 7/12)
b = float (2 + 17/36)
c = float (2.5)
d = float (4 + 1/3)
e = float (0.65)
f = float (4 / (1/4))
g = float (0.5)
num11 = ((a -b) * c - (d / e)) / (f - g)
print (num11)

# 15
num15 = (5.75 * 100) / 2.5
print (num15)