import plotly as py
import plotly.graph_objs as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('mt_bruno_elevation.csv')
# print(z_data.values)
# trace = go.Figure(data=[go.Surface(z=z_data.values)])
trace1 = go.Surface(z=z_data.values)

layout = dict(
            title = 'Mt Bruno Elevation',
            xaxis = dict(title= 'unif_poly_plot_xlabel'),
            yaxis = dict(title= 'unif_poly_plot_ylabel'),
            # autosize=True,
            # width=500, height=500,
            # margin=dict(l=65, r=50, b=65, t=90)        
            )
# fig.update_layout(title='Mt Bruno Elevation', autosize=False,
#                   width=500, height=500,
#                   margin=dict(l=65, r=50, b=65, t=90))

data = [trace1]
fig = dict(data= data, layout= layout)
py.offline.plot(fig, filename= 'mt_bruno_elevation.html')
