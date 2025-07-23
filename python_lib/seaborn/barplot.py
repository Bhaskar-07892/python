import seaborn as  sb 
import pandas as pd 
import matplotlib.pyplot as plt

url = "https://raw.github.com/mwaskom/seaborn-data/master/penguins.csv" 
df = pd.read_csv(url)

# print ('dataframe', df )

island_order = ['Biscoe' , 'Dream' , 'Torgersen']

# sb.barplot(x=df.island , y= df.bill_depth_mm ,data=df , hue = df.sex )

print (' ')
sb.barplot(x=df.island , y=df.bill_depth_mm ,data = df , hue = df.island , order = island_order , palette='Accent' , saturation=0.4)
plt.show()