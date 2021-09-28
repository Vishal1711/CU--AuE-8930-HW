import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)

print("Values which is bigger than 10 =", x[x>10])
print("Those indices are ", np.nonzero(x > 10))
