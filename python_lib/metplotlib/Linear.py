import matplotlib.pyplot as plt

print ("Simple Linear Graph : " )

x = [ 1 , 2 , 3 , 4 , 5]
y = [ 10 , 20 , 30 , 40 , 50 ]
c = 'r' # colour

plt.plot ( x , y , c) # c argument for colour 
plt.title ( "simple linear graph")
plt.show ()


print ("Some random Linear Graph with marker : " )

x = [ 7 , 0 , 3 , 5 , 1 ]
y = [ 5 , 4 , 9 , 8 , 2 ]

plt.plot (x,y,marker = 'o' )
plt.title ( ' Linear Graph ' )
plt.show ()


print ( "Make diffrent - diffrent graph of X and Y : " )
x = [ 8 , 5 , 7 , 3 , 1 ]
y = [ 10 , 36 , 28 , 40 , 29 ]
x_colour = 'g'
y_colour = 'r'

plt.plot ( x , y )
plt.title ( "X and Y" )
plt.plot ( y , y_colour , marker = ">" )
plt.plot ( x , x_colour , marker = "o" )
plt.show ()


print ( " Lable and grid : " )
x = [ 8 , 5 , 7 , 3 , 1 ]
y = [ 10 , 36 , 28 , 40 , 29 ]
c = 'orange'

plt.plot (x,y ,c)
plt.xlabel(' X lable ') 
plt.ylabel(' Y lable ')
plt.grid (True)
plt.show ( )