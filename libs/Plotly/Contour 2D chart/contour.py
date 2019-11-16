import plotly as py
import plotly.graph_objs as go

import pandas as pd

# Read data from a csv
df = pd.read_csv('REML1_contour_plot.csv', skiprows= 9)
df = df[['site_1', 'site_2', 'site_3', 'site_4', 'site_5', 'site_6', 'site_7',
        'site_8', 'site_9', 'site_10', 'site_11', 'site_12', 'site_13']]

# print(df)
# print(df.iloc[2].tolist())

x1 = [0,0,30,0,-30,0,60,0,-60,0,90,0,-90]
y1 = [0,-30,0,30,0,-60,0,60,0,-90,0,90,0]

j = 1
def contour_plot(i, l):
    trace1 = go.Contour(
                x= x1,
                y= y1,
                z= df.iloc[i].tolist(),
                contours=dict(
                            # coloring ='heatmap',
                            showlabels = True, # show labels on contours
                            labelfont = dict( # label font properties
                                size = 12,
                                color = 'white',
                               )
                        ),
                )
    

    layout = dict(
                title = 'Al ER Contour plot for ' + 'RUN ' + str(l.index(i)+1),
                xaxis = dict(
                            title= 'x-axis',
                            # type='linear',
                            range= [-100, 100]
                            ),
                yaxis = dict(
                            title= 'y-axis',
                            # type='linear',
                            range= [-100, 100]
                            ),
                autosize= True,
                width=800, height=800,

                )

    data = [trace1]
    fig = dict(data= data, layout= layout)
    py.offline.plot(fig, filename= 'Al_ER_Contour_plot_' + str(l.index(i)+1) + '.html', auto_open= True)
    # j += 1

row_list = [2, 5, 8, 11, 14]

for i in row_list:
    contour_plot(i, row_list)

# fig = go.Figure()
# fig.update_layout(
#     shapes=[
#         # unfilled circle
#         go.layout.Shape(
#             type="circle",
#             xref="x",
#             yref="y",
#             x0=1,
#             y0=1,
#             x1=3,
#             y1=3,
#             line_color="LightSeaGreen",
#         ),
#         # # filled circle
#         # go.layout.Shape(
#         #     type="circle",
#         #     xref="x",
#         #     yref="y",
#         #     fillcolor="PaleTurquoise",
#         #     x0=3,
#         #     y0=3,
#         #     x1=4,
#         #     y1=4,
#         #     line_color="LightSeaGreen",
#         # ),
#     ]
# )


# REFERENCE: 
# - https://help.plot.ly/documentation/python/shapes/
# - https://plot.ly/python/shapes/