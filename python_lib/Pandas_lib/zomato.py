import pandas as pd 

Zomato_df=pd.read_csv(r'C:\Users\op_Bh\code_base\data_science\Zomato_data.csv')

print (Zomato_df)

#print top 5 
top_5_restaurent = Zomato_df.head()
print (f"Top 5 restaurent \n: {top_5_restaurent} \n")

# print last 5 
last_5_restaurrent = Zomato_df.tail()
print (f"Last 5 restorent \n: {last_5_restaurrent}\n")

"""display_20_rest = Zomato_df [45 : 60]
print (f"Print restaurent from 45 to 65 : \n {display_20_rest} \n")"""

display_6_rest = Zomato_df.iloc [0:6]
print (f"Print restaurent from 0 to 6: \n {display_6_rest} \n")


#check the data type of all keys
check_data_type = Zomato_df.dtypes 
print (f"Data type of all rows \n: {check_data_type}\n")

#all details
summary_statistics  = Zomato_df.describe()
print (f"All details of data\n {summary_statistics }\n")

#your coloum
restaurants_with_online_order = Zomato_df [Zomato_df [ "online_order"]=="Yes"] [ [ "name" , "online_order"]]
print (f"Restaurent with online order \n: {restaurants_with_online_order}\n")
print(f"Num of restaurent with online order\n {len(restaurants_with_online_order)} \n ")

#datatype == obj
obj_data_type = Zomato_df.dtypes == object
print (f" Obj data type : \n {obj_data_type} \n ")

#print data of only int 
int_data = Zomato_df [Zomato_df.dtypes [ Zomato_df.dtypes == 'int64'].index ]
print (f"print data of int colum \n: {int_data}\n")


#display all column name 
print (Zomato_df.columns)

# add column at end
Zomato_df['last column'] = 'none'

#add coloum at spesific index
Zomato_df.insert(loc=2 , column="Location" , value = "Hyd" )  

# change first 10 colums index and print name 
first_10 = Zomato_df['name'] [0:10]
print (f" {first_10} {type(first_10)} ")

index_1 = ["a" , "b" , "c" , "d" , "e" , "g" , "h" , "i" , "j" , "k" ]
change_ind = pd.Series( first_10.values , index=index_1)
print(change_ind)


#del row
del_row = Zomato_df.drop ( index=2 )
print (f"One column deleted : \n {del_row} \n")  # this is a temprery change .

print(Zomato_df)

# permanent del row
"""
per_del_row = Zomato_df.drop (index = 3 , inplace=True)
print (f"forth row delete permanent {per_del_row}")

print(Zomato_df)
"""

# temp del col
del_col = Zomato_df.drop ("listed_in(type)" , axis = 1)
print (del_col)

# permanent del col
"""
per_del_col = Zomato_df.drop ("listed_in(type)" , axis = 1)
print (per_del_col)
"""

# index 

#set index
set_ind = Zomato_df.set_index ('name')
print (set_ind)

#reset index
"""
reset_ind = Zomato_df.reset_index ()
print (reset_ind)

"""

# making a new freme using dict

d_freme = {
    "Key_1" : [1 , 2 , 3 , 4 , 5 ] ,
    "Key_2" : [6 , 7 , 8 , 9 , 10] , 
    "Key_3" : [11 , 12 , 13 , 14 , 15] 
}
print (pd.DataFrame(d_freme))



# del nan col 

"""
del_nan_row = Zomato_df.dropna(axis=1)
print (del_nan_row)

"""

# replace nan with another 
"""
fill_nan = Zomato_df.fillna("bhaskar")
print(fill_nan)

"""