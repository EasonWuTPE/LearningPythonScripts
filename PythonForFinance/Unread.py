#!/usr/bin/python3.5 

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

# mpl_finance => Not read. pp.125  

# 3D plotting => Not read. pp.129 
x = np.linspace(50,150,24) 
y = np.linspace(0.5,2.5,24) 

X, Y = np.meshgrid( x, y ) 
print( X ) 
print( Y ) 


