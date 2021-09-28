import numpy as np

# 1-Dimensional arrays

a1 = np.arange(0, 4).reshape(4,1)
b1 = np.arange(4,8).reshape(4,1)
Add1 = a1 + b1
Sub1 = a1 - b1
Div1 = a1/b1
Mul1 = np.multiply(a1, b1)
print('Addition1: ')
print(Add1)
print('Substraction1: ')
print(Sub1)
print('Division1: ')
print(Div1)
print('Multiplication1: ')
print(Mul1)



# 2-Dimensional arrays
a2 = np.arange(1, 17).reshape(4,4)
b2 = np.arange(17, 33).reshape(4,4)
Add2 = a2 + b2
Sub2 = a2 - b2
Mul2 = np.multiply(a2, b2)
Div2 = a2 / b2
print('Addition: ')
print(Add2)
print('Substraction: ')
print(Sub2)
print('Multiplication: ')
print(Mul2)
print(a2)
print(b2)
print('Division: ')
print(Div2)
