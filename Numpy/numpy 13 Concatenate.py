import numpy as np
arr1 = np.array([[1,2,3],[7,8,9]])
arr2 = np.array([[11,12,13],[14,15,16]])

# a=np.concatenate((arr1,arr2),axis=0)
# print(a)

# b = np.concatenate((arr2,arr1),axis=1)
# print(b)



# c = np.concatenate((arr1,arr2),axis=1)
# print(c)

d = np.vstack((arr1,arr2))
print(d)

e = np.hstack((arr1,arr2))
print(e)