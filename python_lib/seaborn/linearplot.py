import seaborn as  sb 
import pandas as pd 
import matplotlib.pyplot as plt

url = "https://raw.github.com/mwaskom/seaborn-data/master/penguins.csv" 
df = pd.read_csv(url)

# print ('Penguins data for Seaborn librery : \n' , df) 

print ('\n')

nan_col = df.isna().sum().sum()
# print ('no of nan in dataframe : \n' , nan_col )

print ('\n')

# df.dropna ( axis = 0 , how = 'all' )   ---    its use when all row value has nan 
df.dropna ( axis = 0 , how = 'any' , inplace=True)
# print ('after delete all nan row  : \n' , df )

print ('\n')

df.reset_index(drop=True , inplace=True)    # drop = True  mean replce old index into new index
# print ('After reseting index : \n' , df ) 

print ('\n')

# sb.lineplot( x = 'bill_length_mm' ,  y = 'flipper_length_mm' , data = df )
# sb.lineplot( x = 'bill_length_mm' ,  y = 'flipper_length_mm' , data = df , hue = 'sex' )
# plt.show()

print ('\n')

print ('Take some data for another styling : \n')
sample_data_20 = df.head(20) 
print ( sample_data_20 )

sb.lineplot( x = 'bill_length_mm' ,  y = 'flipper_length_mm' , data = sample_data_20 , hue = 'sex' , style = 'sex' , palette='rocket_r' , markers= ['o','>'])
plt.grid()
plt.title('Data of Peguins')
plt.show ( )