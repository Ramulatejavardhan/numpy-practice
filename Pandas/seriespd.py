# series= A pandas 1 dimensional labeled array that can hold any data type think of it like a single column in a spreadsheet(1-dimensional)
import pandas as pd
data =[1,2,3,4]
# data=pd.Series(data)#gives with index as well
data=pd.Series(data,index=["a","b","c","d"])#changes the index with given values
data.loc["a"]=99 # we can update the value
print(data.loc["a"])# we access the value