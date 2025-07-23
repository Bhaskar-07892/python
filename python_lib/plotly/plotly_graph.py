import plotly.graph_objects as pg 

a = [ 2 , 3 , 3.7 , 2 , 3.7 , 2 ]
b = [ 1 , 3.5 , 1 , 2.8 , 2.8 , 1] 

fig = pg.Figure(pg.Scatter(x = a , y = b))

# adding a title 
fig.update_layout ( title = 'Line chart : Star ' , xaxis_title = ' x axis ' , yaxis_title = ' y axis ')

# fig.show ()

# adding more graph on this graph 

x1 , y1 = [1 ,3, 8 ,2 ,9 ] , [ 3, 8 ,4 , 3 , 7]
x2 , y2 = [6 ,7 ,3, 6 , 1] , [8, 3 , 6 , 1 , 9]
x3 , y3 = [1 ,3, 8 ,2 ,9 ] , [6 , 7 ,3, 6 , 1 ]

fig = pg.Figure()

# fig.add_trace (pg.Scatter (x = x1 , y = y1 ))
# fig.add_trace (pg.Scatter (x = x2 , y = y2 ))
# fig.add_trace (pg.Scatter (x = x3 , y = y3 ))

fig.update_layout ( title = '3 Line chart : ' , xaxis_title = ' x axis ' , yaxis_title = ' y axis ')

# change the name of trace and change the mode
fig.add_trace (pg.Scatter ( x = x1 , y = y1 , name = 'blue line' , mode = 'lines' ))
fig.add_trace (pg.Scatter ( x = x2 , y = y2 , name = 'red line' , mode = 'markers' ))
fig.add_trace (pg.Scatter ( x = x3 , y = y3 , name = 'red line' , mode = 'lines + markers' ))

# fig.show() 

# bubble graph 

x , y = [1 ,3, 8 ,2 ,9 ] , [ 3, 8 ,4 , 3 , 7] 

fig = pg.Figure ( )
fig.add_trace ( pg . Scatter ( x = x , y = y , name = 'bubble' , mode = 'markers' , marker_size = 70))
fig.show ()