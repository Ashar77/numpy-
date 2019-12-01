import numpy as np  
x=np.random.randn(4,5)
#print(x)
y=x.reshape((2,2,5))
#print('---------------') 
print(y)

y = x.reshape((2,2,5),order='F')
#print(y)

z = x.reshape((2,2,-1))
#print(z)

r=z.ravel()   # or .flaten()
#print(r)