
import time
import numpy as np
# import pycuda.driver as cuda
# import pycuda.autoinit
# from pycuda.compiler import SourceModule
start = time.time()

BLOCK_SIZE = 256

n = 1600
ni = np.int32(n)

# matrix A
a = np.random.randn(n, n)*10
a = a.astype(np.float32)

# matrix B
b = np.random.randn(n, n)*10
b = b.astype(np.float32)

# matrix C
c = np.empty([n, n])
c = c.astype(np.float32)


x = np.matmul(a, b)
print(A)

end = time.time()
#matrix d-using cpu
d =np.matmul(a,b)
print ("Time: %.5f s"%(end-start))
print(c-d)
print(np.greater_equals(c,d))
