#!/usr/bin/python3.5 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Financial Time Series 
df = pd.DataFrame([10,20,30,40],index=['a','b','c','d'],columns=['numbers']) 
print(df) 
print( df.index, df.columns, df.loc['c'], df.ix['c'], sep='\n' ) 
print( df.loc[['b','c']] ) 
print( df.loc[df.index[1:3]] ) 
print( "sum:\n", df.sum() ) 
print( "mean:\n", df.mean() ) 
print( df**2 ) 
print('.apply():\n ',df.apply( lambda x: x**2 ) ) # like map() to some degrees. 

# Enlarge DataFrame 
df["float"] = [ 1.2, 2.3, 3.4, 4.5 ] 
print('enlarge DataFrame:\n', df) 

# indices are aligned automatically 
df["names"] = pd.DataFrame( ["Apple","Banana","Cat","Egg"], 
                            index=['a','c','b','d'] ) 
print("Indices aligned automatically:\n",df) 

# Appended I  
df_ = df.append( {"numbers":100,"float":3.2,"names":"hat"}, ignore_index=True,sort=False ) 
print( "Append I:\n", df_ ) 
# Appended II 
df_ = df.append( pd.DataFrame({"numbers":100,"float":3.2,"names":"hat"}, index=['e']) ) 
print("Append II:\n", df_ ) 


# Join with no outer  
df3 = pd.DataFrame( [1,4,9,16,25],index=['a','b','c','d','z'],columns=['squares'] ) 
df_ = df_.join(df3) 
print( 'join with no outer :\n', df_ ) 
# Join with outer  
df3 = pd.DataFrame( [1,4,9,16,25],index=['a','b','c','d','z'],columns=['squares'] ) 
df_ = df.append( pd.DataFrame({"numbers":100,"float":3.2,"names":"hat"}, index=['e']) ) 
df_ = df_.join(df3, how='outer') 
print( 'join with outer :\n', df_ ) 
# Join with inner  
df3 = pd.DataFrame( [1,4,9,16,25],index=['a','b','c','d','z'],columns=['squares'] ) 
df_ = df.append( pd.DataFrame({"numbers":100,"float":3.2,"names":"hat"}, index=['e']) ) 
df_ = df_.join(df3, how='inner') 
print( 'join with inner :\n', df_ ) 


df2 = pd.DataFrame( {'numbers':[10,20,30,40]}, index=['a','b','c','d'] ) 
print( df2 ) 



print("\n\n") 
print("#"*90) 
# Others 
rand = np.random.standard_normal( (9,4) ) 
df_rand = pd.DataFrame( rand ) 
print( df_rand ) 
print("\n") 


# Create columns 
df_rand.columns = [ ["Col1","Col2","Col3","Col4"] ] 
print( df_rand ) 
print("\n") 

# Create index 
df_rand.index = [ ["No."+str(val) for val in range(1,10)] ]
print( df_rand ) 




