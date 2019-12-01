import numpy as np 
d = np.array([1,2,3,4,5,6,7,8,9]) 
#print(np.split(d,[2,5]))

arr1 = np.array([[1,2,3],[7,3,1]])
print(np.split(d,[1],axis=0))

print('--------------------------')

x = [[1,4,5,6,7,9,1,4],[11,14,15,16,17,19,11,14]]
d = np.array(x)
#print(np.split(d,[4,6],axis=1))
