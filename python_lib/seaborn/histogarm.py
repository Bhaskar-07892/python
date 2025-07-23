import seaborn as sb 
import pandas as pd 
import matplotlib.pyplot as plt 

url = "https://raw.github.com/mwaskom/seaborn-data/master/penguins.csv"
df = pd.read_csv(url)

# print (df)

# in matplotlib use histplot but in seaborn use lineplot
# sb.displot(df['flipper_length_mm'])

# bins use for give intervel 
# sb.displot (df ['flipper_length_mm'] , bins = [170 , 180 , 190 , 200 , 210 , 220 , 230 ])

# color and dencity 
sb.displot (df ['flipper_length_mm'] , bins = [170 , 180 , 190 , 200 , 210 , 220 , 230 ] , color='r' , kde = True)

plt.show ()