#!/usr/bin/python3.5 

import numpy as np 

''' 
 np.array only exist one data type.  
''' 
a = np.array([[1,2],[1,3]]) 
b = np.array([[3,2],[10,3]]) 

element_wise_product = a * b 
inner_matrix_product = np.dot(a,b) 

print( element_wise_product,inner_matrix_product, sep='\n' ) 


arr1 = np.array([1,2,3,12.2,2.1,3]) 
print(arr1.sum()) 
print(arr1.std()) 
print(arr1.cumsum()) 
print(arr1*2) 
print(arr1**2) 
print(np.sqrt(arr1)) 


arr2 = np.array([[3,2],[10,3]]) 
print( arr2.sum() ) 
print( arr2.sum(axis=0) ) 
print( arr2.sum(axis=1) ) 


arr3 = np.zeros((2,3)) 
print( arr3 ) 

arr3_1 = np.zeros((2,3,3)) 
print( arr3_1 ) 

arr4 = np.ones((2,3,3)) 
print( arr4 ) 

arr5 = np.array([[1,2.3],[1,3]]) # np.array only exist one data type.  
print( arr5 ) 

#############################################################################


import time 
import random 
SIZE = 5000 

''' Generate a 5000*5000 matrix at random and summation. ''' 
''' Pure Python ''' 
starttime = time.time() 
MATRIX_Pure_Python = [ [random.gauss(0,1) 
                            for col in range(SIZE)] 
                            for row in range(SIZE) ] 

endtime = time.time() 
print( "Duration by pure python: ", endtime-starttime ) 


''' Numpy ''' 
starttime = time.time() 
MATRIX_Numpy = np.random.standard_normal( (SIZE,SIZE) ) 
endtime = time.time() 
print( "Duration by Numpy: ", endtime-starttime ) 



