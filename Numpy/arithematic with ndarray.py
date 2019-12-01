import numpy as np 
a=np.random.randn((10))
b = np.random.randn((10))
#print(a)
#print(b)
# #print(a>0)
# print(a[1])
# print(a[a>0]) # selecting the desired elements from the array

names = np.array(['ahmed','kashi','ali','morris','kashi'])
print(names=='kashi')
print(names[0])
print(names[names=='kashi']) # returing names[True]

