#!/usr/bin/python3.5 

import numpy as np 
import pandas as pd 

df = pd.read_csv(r'./rates-oanda-USD-CAD_1548662729.csv').drop(['open_midpoint','close_midpoint'], axis=1) 
print(df.info()) 


# Numpy
v = list(range(1,6)) 
v_np = np.array(range(6)) 
print( 'v:',v,', v_np:',v_np ) 
print( '2*v:',2*v,', 2*v_np:',2*v_np ) 

# float 
c = 0.5 
c = c.as_integer_ratio() 
print(c) 


