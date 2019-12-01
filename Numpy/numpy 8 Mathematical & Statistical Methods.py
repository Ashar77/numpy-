import numpy as np 
x = np.array([8,9,29,17,6])
#print(x.mean())
#print(x.cumsum())

y =x>6
#print(y)

print(y.sum())      # returns number of TRUE in the array

print(y.any())

print(y.all())

arr = np.array([7,9,33,0,1])
# print(np.sort(arr))
print(np.unique(arr))