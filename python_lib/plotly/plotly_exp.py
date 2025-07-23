import plotly.express as px 

a = 2 , 3 ,4 , 5 , 6 
b = 2 , 4 , 6 ,8 , 0 

fig = px.line ( x = a , y = b )
fig.show()