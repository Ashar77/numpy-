import pandas as pd

#apples = pd.Series([3,2,0,1])
#oranges = pd.Series([3,2,0,1])

#data = {"apples":apples,"oranges":oranges}

#fruit_df = pd.DataFrame(data)

#print(fruit_df)

#----------------------------------------------

'''
states = ['Ohio','florida','Alaska','Kentucky','California','Arizona']

data = {'state':states,'year':[2000,2001,2002,2003,2004,2005],
        'population':[1.5,1.6,0.6,2,4.5,3]}


# we can provide index in the pd.DataFrame, if not given it will by default given
# integer index from 0 to n 
#indexes must be equal to the number of rows(elements in list) in each columns !


population_frame = pd.DataFrame(data,index=['1st','2nd','3rd','4th','5th','6th'])


print(population_frame)
                                '''

#----------------------------------------------------

#frame.head() returns top 5 rows of each column
'''
states = ['Ohio','florida','Alaska','Kentucky','California','Arizona']

data = {'state':states,'year':[2000,2001,2002,2003,2004,2005],
        'population':[1.5,1.6,0.6,2,4.5,3]}


population_frame = pd.DataFrame(data,index=['1st','2nd','3rd','4th','5th','6th'])

print(population_frame.head())
print()
print()
# we can change the position of columns in dataFrame
population_frame = pd.DataFrame(data,index=['1st','2nd','3rd','4th','5th','6th'],columns=['year','state','population'])
print(population_frame.head())

print()
#we can also add another columns in our dataFrame it will have Nan Value in every row
population_frame_with_area = pd.DataFrame(data,index=['1st','2nd','3rd','4th','5th','6th'],columns=['year','state','population','area'])
print(population_frame_with_area)
print()
print(population_frame.columns)         #returns the list containing names of columns in dataFrame

print(population_frame.index)            #returns the list containing the index/names of rows in each columns of dataframe 
                                                                                                                                            '''
#--------------------------------------------------------------------------------------------------------------------------------------------
# a column in a dataFrame can be retrived as a Series either by dict-like notation or by attribute

data = {'year':[2000,2001,2002,2003,2004,2005],
        'population':[1.5,1.6,0.6,2,4.5,3]}

#print(data['year'])  #  accessing data in dictionary / dictionary-notation

population_frame = pd.DataFrame(data,index=['1st','2nd','3rd','4th','5th','6th'])
#print(population_frame['year'])      # accesing data using dictionary like notation   # series of year is obtained

#print(population_frame.year) # using attribute style to access DF column

# data of each column from a particular row can also be accesss using loc method frame-name.loc(index of row)

#print(population_frame.loc['3rd'])

#print(len(population_frame))  #len() -- returns number of rows in frame
#---------------------------------------------------

#adding another columna and assigning values to each row of the columns

#population_frame = pd.DataFrame(data,index=['1st','2nd','3rd','4th','5th','6th'])
#print(population_frame)
import numpy as np
'''
data = {'year':[2000,2001,2002,2003,2004,2005],
        'population':[1.5,1.6,0.6,2,4.5,3],}

population_frame = pd.DataFrame(data,index=['1st','2nd','3rd','4th','5th','6th'],columns=['year','population','debt'])
#print(population_frame)
ln = len(population_frame)   # finding number of rows of each column 
debt_received = np.arange(ln)  # assinging value to the debt column        
population_frame['debt'] = debt_received
print()
print()
print(population_frame) '''

#-------------------------------------------
'''
frame =  pd.DataFrame(np.random.randn(4,3),columns=list('abc'),index=['Ohio','Utah','Alaska','California'])

# print(frame)

# print()

# print(frame['a'].max()) # print max value in column a 
# print(frame['b'].min()) # min value in column b
#print(frame)
print(frame['c'].max()-frame['c'].min())

f = lambda x: x.max() - x.min()    # applying the function on the whole dataFrame
print(frame.apply(f,axis=0))   # axis = 0 ---> along x axis ----> on each column
                               # axis = 1 ---> along y axis ----> on each row
                                                                                '''
#-------------------------------------------------------------------------------
'''
#state_frame = pd.DataFrame([np.arange(16).reshape(4,4)])
states = ['Ohio','florida','Alaska','Kentucky','California','Arizona']

data = {'state':states,'year':[2000,2001,2002,2003,2004,2005],
        'population':[1.5,1.6,0.6,2,4.5,3]}

df = pd.DataFrame(data,index=['fir','sec','thr','for','fiv','six'])
print(df)
print()
#find_large = lambda x:  x =='Alaska'
#print(df.apply(find_large,axis=0))   # return boolean df

#print(df['state'].apply(find_large))
print(df.loc[['fir','sec'],['state','year']])  # using loc
print()
print()
print(df.iloc[[0,1],[0,1]]) #using iloc                         '''


#----------------------------------------------------------------------------------


#ARITHEMATIC AND DATA ALIGNMENT

df1 = pd.DataFrame(np.arange(9.).reshape(3,3),columns=list('bcd'),index=['Ohio','Texas','Colorado'])

df2 = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])

#print(df1)
print()
print()
# print(df2)

df3 = df1 + df2   # map corresponding values #Nan will be returned in case of mismatch

# print(df3)   


#while performing arithematic operations Nan will occur at some position  fill_value is used to give the default value if Nan appear at any position

df3 = df1.add(df2,fill_value=0) # replacing Nan with 0 and then adding a/c to command

# print()
# print(df3)

series = pd.Series([1,2,3],index=['b','c','d']) #row wise

result = df1-series

#print(result)

#--------------------------------
# DELETING DATA 
'''
print(df1)

df1.drop('b',axis=1)

print(df1)

df1 = df1.drop('b',axis=1)

print()

print(df1)

print()

df1.drop('d',axis=1,inplace=True)

print(df1)

print()
df1.drop('Texas',axis=0,inplace=True)
print(df1)
                                                '''
#-----------------------------------------

# INDEXING , SELECTION AND FILTERING
'''
data = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
print(data)

print()
print()

data_2=data[['b','d']]
#print(data_2)

print(data[2:])
                                        '''
#----------------------------------------------------------

# SORTING
'''
frame = pd.DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])

print(frame)
print()
print()
print(frame.sort_index(axis=1,ascending=True))
print()
print()
print(frame.sort_index(axis=1,ascending=False))
print()
print(frame.sort_index(axis=0,ascending=True))          '''
#-------------------------------------------------------------

#REINDEX
'''
obj3 = pd.Series(['blue','purple','yellow'],index=[0,3,6])

print(obj3)

obj3=obj3.reindex(range(9),method='ffill')

print(obj3)             '''
#--------------------------------------------------------------

'''
states = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','c','d']
                ,columns=['Ohio','Texas','California'])

print(states)

states_names = ['Texas','Utah','California','Ohio']

index_names = ['a','b','c','d']

states = states.reindex(columns=states_names)

#print(states)

states = states.reindex(index=index_names)
print()

#print(states)

                        '''

























