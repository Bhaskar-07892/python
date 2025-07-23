""" 
Q2. Draw Pie Chart for Family Budget 
Given:

Food = Rs.240
Clothing = Rs.100
House Rent = Rs.120
Fuel = Rs.36
Recreation = Rs.24
Transport = Rs.48
Insurance/Savings = Rs.32
Education = Rs.70
Miscellaneous = Rs.50

"""

import matplotlib.pyplot as plt 

print ( " Family budget Pie chart : " )

x = [ "Food" , "Clothing" ,"House Rent" ,"Fuel" ,"Recreation" ,"Transport" ,"Insurance/Savings" ,"Education" ,"Miscellaneous" ]

y = [ 240 , 100 ,120 ,36 , 24 , 48 , 32 , 70 , 50 ]

colour = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB6C1', '#FFD700', '#D3FFCE', '#87CEFA']
plt.pie ( y, labels=x)
plt.title ('Family budget Pie chart :')
plt.legend(loc='center left',bbox_to_anchor=(1, 0.5) )
plt.show () 