import numpy as np 
d = np.array([1,5,7,8])
print(np.repeat(d,2))
print(np.repeat(d,3))

print(np.tile(d,2))


arr = np.array([[1,2,3],[4,5,6]])
print(np.tile(arr,3))