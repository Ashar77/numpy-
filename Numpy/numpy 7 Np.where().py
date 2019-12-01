# in data sciene we can get some null value in a certain data set in that situation 
# this function of where is very important

import numpy as np 
salary = np.array([0,-1,10000,50000])

x = np.where(salary<=0,25000,salary)
print(x)

y = np.where(salary<=0,'not ok',salary)
print(y)


