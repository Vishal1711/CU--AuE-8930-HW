import math
number = input('Enter a number: ')
C = 50
H = 30
list = number.split(",")
value = []
for D in list:
    value.append(str(int(round(math.sqrt(2*C*float(D)/H)))))

print(','.join(value))
