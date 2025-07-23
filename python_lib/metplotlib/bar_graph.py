import matplotlib.pyplot as plt 
import numpy as np 

x = [ 1,2,3,4]
y = [ 5,6,7,8]
c = ['r','g','b','y' ]

plt.bar(x,y,color = c)
plt.show()

x = np.array (['A' , 'B' , 'C' , 'D'])
y = np.array ([10 , 20 ,30 , 40])

plt.barh (x,y,color ='hotpink',height=0.2)
plt.title('Bar Digrame')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()