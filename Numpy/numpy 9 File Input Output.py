import numpy as np  
x = [1,4,5,7]
y = [8,7,9]
np.save('testx',x) 
loadx = np.load('testx.npy')
#print(loadx)

np.savez('testxy',x,y)
loadxy = np.load('testxy.npz')
print(loadxy)
print(loadxy['x'])  
