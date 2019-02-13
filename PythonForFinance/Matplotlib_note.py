#!/usr/bin/python3.5 

import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(10000) 

y = np.random.standard_normal(20) 
x = range(len(y)) 
plt.plot(x,y) 
plt.grid(True) 
plt.axis('tight') # Adjust the axis range by off, equal, scaled, tight, image 
plt.title("Figure I") 
plt.show() 


# Two dimensional plt. 
# also set the mini and max values of each axis by plt.xlim(), plt.ylim() 
# plt.plot( x, y, color, ls, lw, label, marker ) 
plt.figure(figsize=(10,4)) # define the size of figure in (width,height) 
plt.plot(x,y.cumsum(), color='b',label="cumsum of y", lw=2.5) # lw means line width 
plt.plot(x,y,color='r',ls='--',label="y",marker='*' ) # ls means line style  
plt.legend(loc='best') #plt.legend(loc='best',labels=["cumsum of y", "y"]) 
plt.grid(True) 
plt.xlim(-1,20) 
plt.ylim(np.min(y.cumsum())-1, np.max(y.cumsum())+1) 
plt.axis('tight') 
plt.title("Figure II") 
plt.show() 


# Two dimensional plt. 
# Two y axis. 
plt.figure(figsize=(5,4)) # define the size of figure in (width,height) 
plt.plot(x,y.cumsum()+100, color='b',label="cumsum of y", lw=2.5) # lw means line width 
plt.legend(loc='best')  
plt.twinx() # setting right y axis 
plt.plot(x,y,color='r',ls='--',label="y",marker='*' ) # ls means line style  
plt.legend(loc='best')  
plt.grid(True) 
plt.xlim(-1,20) 
plt.ylim(np.min(y.cumsum())-1, np.max(y.cumsum())+1) 
plt.axis('tight') 
plt.title("Figure III") 
plt.show() 


# Two graph 
plt.figure(figsize=(7,5)) 
plt.subplot(2,1,1) # plt.subplot(211)  
plt.title("Figure IV") 
plt.plot(x,y.cumsum()+100, color='b',label="cumsum of y", lw=2.5) # lw means line width 
plt.grid(True) 
plt.legend(loc='best')  

plt.subplot(2,1,2) # plt.subplot(212)  
plt.plot(x,y,color='r',ls='--',label="y",marker='*' ) # ls means line style  
plt.legend(loc='best')  
plt.grid(True) 
plt.xlim(-1,20) 
plt.ylim(np.min(y.cumsum())-1, np.max(y.cumsum())+1) 
plt.axis('tight') 
plt.show() 


# Two graph with different type  
plt.figure(figsize=(7,5)) 
plt.subplot(2,1,1) # plt.subplot(211)  
plt.title("Figure V") 
plt.plot(x,y.cumsum()+100, color='b',label="cumsum of y", lw=2.5) # lw means line width 
plt.grid(True) 
plt.legend(loc='best')  

plt.subplot(2,1,2) # plt.subplot(212)  
plt.bar(x,y,width=0.8,color='g',label='y')   
plt.legend(loc='best')  
plt.grid(True) 
plt.xlim(-1,20) 
plt.ylim(np.min(y.cumsum())-1, np.max(y.cumsum())+1) 
plt.axis('tight') 
plt.show() 


# Two dimensional graph with different type  
plt.figure(figsize=(7,5)) 
plt.title("Figure VI") 
plt.bar(x,y,width=0.8,color='g',label='y')   
plt.legend(loc='best')  
plt.twinx() # setting right y axis 
plt.plot(x,y.cumsum()+100, color='b',label="cumsum of y", lw=2.5) # lw means line width 
plt.legend(loc='best')  
plt.grid(True) 
plt.xlim(-1,20) 
plt.ylim(np.min(y.cumsum())-1, np.max(y.cumsum())+1) 
plt.axis('tight') 
plt.show() 
