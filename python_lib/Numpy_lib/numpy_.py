import numpy as np 


# crating a array 
arr = np.array ([3,6,9])
print ("Array : \n" , arr)


# creating zeros array 
zeroes_arr = np.zeros((3,3))
print ("Zeroes Array : \n" , zeroes_arr)


# creating onces array 
ones_arr = np.ones((3,3))
print ("Onse Array : \n" , ones_arr)


# creating any numbers array 
num_arr = np.full ((3,3) , 3)
print ("Any number Array : \n" , arr)


# creating random array
rand_arr = np.random.random((3,3))
print ("Random Array : \n" , rand_arr)


# creating a sequencial array 
seq_arr = np.arange (1,11,2)
print ("Array in sequencial order \n" ,seq_arr) 


# # # Array , Matrix , Tensor # # #


# Array - same data type in one dimention list 

vector = np.array( [1,2,3,4,5,6,7,8,9] )
print ("Vector \n" ,vector) 

# Matrix - same as array but it is 2D 

matrix = np.array ( [
                    [1,2,3] ,
                    [4,5,6] ,
                    [7,8,9]
                    ] )
print ("Matrix \n" ,matrix) 

# Tensor - same as array but multi Dimention

tensor = np.array ( [
    [ [ 1 , 2 ] , [ 3 , 4 ] ],
    [ [ 5 , 6 ] , [ 7 , 8 ] ] 
    ] )
print ("Tensor \n" , tensor) 


# Array properties 

arr_1  =  np.array ([1,2,3,4,5,6,7,8,9])

print (arr.shape) 
print (arr.dtype)
print (arr.size)
print (arr_1.ndim)

# Reshaped Array 

reshaped = arr_1.reshape(3,3)
print ("Reshaped Array \n" , reshaped )

flatend = reshaped.flatten()
print ("Flattend Array \n" , flatend )

revaled = reshaped.ravel ()
print ("Ravel Array \n" , revaled )

trans = reshaped.transpose()
print ("transpose Array \n" , trans )

# Array opretions 

ArrAy = np.array ([3,7,9,6,1,5,2,8,4 ])

# slaicing ( indexing )
print ( " normal slaicing : " , ArrAy[2:7] )
print ( " with step : " , ArrAy [1:8:2] )
print ("negetive indexing " , ArrAy [-3])

# 2D array indexing 
Array_2D = np.array ( [ [ 3 ,7, 1], [ 4 , 9 , 6] , [2 , 8 , 5]])

print("2D array coloumn Indexing : " , Array_2D[1 , 2])
print ("Entier Row of 2D Array " , Array_2D [1])
print ("Entier Column of 2D Array " , Array_2D [:,1])

# Sorted Array 

print ( "Sorted array 1D : " ,np.sort (ArrAy) )
print ( "Sorted array 2D : " , np.sort (Array_2D))
print ( " Sorted coloumn of 2d array :  " , np.sort (Array_2D , axis = 1))