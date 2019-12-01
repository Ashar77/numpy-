import numpy as np  
x = np.array([1,7,9,8,5])

#print(x[4])  
#print(x>5) 
#print(x[x>5])  
y = x[x>7]        # BOOLEAN INDEXING !!!
#print(y) 
# print(y.shape)
#print(len(y))
zero = np.zeros((10))
#print(zero)
zero[0:len(y)] = y 
#print(zero)

#print(x[[2,1]])     #PASSING A LIST OF DESIRED INDEXES ---> FANCY INDEXING !

x = np.random.randn(10,10)
#print(x)
#print(x[0])
#print(x[0][4])
#print(x[1::2])
#print(x[::,0:4])





'''x = np.zeros((5,5))
print(x)
print('--------------')
#print(x[0])
x[1:4:1,1:4] = 1 
print(x)           '''


'''
x = np.zeros((5,5))
x[0:5:2] = 1 
print(x) '''



x = np.zeros((5,5))
x[0:5:2,0:5:2] = 1
print(x) 




















