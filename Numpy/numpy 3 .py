import numpy as np 
x=np.zeros((3,3))
#print(x)
y = np.ones((3,1))
#print(y)
z = np.empty((2,2))
#print(z)

# pasing list to form a numpy array
l = [2,3,4,7]
#print(np.array(l))
x=np.arange(1,100,10)
print(x.shape)
x = np.zeros((10,10))
print(x.shape)
x.reshape((2,2,5,5)) #for reshaping rxc must be same 
print(x.dtype)
print(x.ndim)
