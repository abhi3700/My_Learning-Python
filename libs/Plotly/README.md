# Plotly
## Installation


## Shortcuts
* Line plot: <kbd>double-click</kbd> to reset from zoom.
* Marker shapes in Plotly charts: `'star-triangle-up'` | `'x'` | `'diamond'` & default (i.e. circle)
	
	E.g.-1
```py
trace2 = go.Scatter(
        x = x,
        y = y2,
        name = thick_plot_trace2_name,
        mode = thick_plot_trace2_mode_cnt,
        line = dict(
                color = thick_plot_trace2_line_color_cnt,
                width = 2),
        marker = dict(
                color = thick_plot_trace2_marker_color_cnt,
                size = 8,
                line = dict(
                    color = thick_plot_trace2_marker_border_color_cnt,
                    width = 0.5),
                symbol = 'diamond'
                ),
        # text = remarks
)


```
* Plotly Offline display of charts
    - M-1:
    ```py
    fig = dict(data= data, layout= layout)
    py.offline.plot(fig, filename= "cp_plot_html_file.html")
    py.offline.plot(fig, filename= "cp_plot_html_file.html", auto_open= False)  # default auto_open is set to `true`, which opens in browser automatically
    py.offline.plot(fig, filename= "cp_plot_html_file.html")
    ```
    - M-2:
    ```py
    fig = go.Figure(data= data, layout= layout)
    py.offline.plot(fig, filename= "cp_plot_html_file.html")
    py.offline.plot(fig, filename= "cp_plot_html_file.html", auto_open= False)  # default auto_open is set to `true`, which opens in browser automatically
    py.offline.plot(fig, filename= "cp_plot_html_file.html")
    ```

## Troubleshooting
* When drawing many traces with portion_1, portion_2 as dates then,
```
data = [trace1_1, trace1_2, trace2, trace3, trace4, trace5]
// just replace above line with below one
data = [trace2, trace1_1, trace1_2, trace3, trace4, trace5]

'''
    Reason: trace1_1, trace1_2 contained portions of dates, where some data points were missing.
    So, instead plotted the trace with 'x' instead of 'x1_1' or 'x1_2'
'''
```

## Repositories
* [WorkCloud Plot](https://github.com/PrashantSaikia/Wordcloud-in-Plotly)
* [Ploty draw shapes - Rectangle, Circle, line](https://help.plot.ly/documentation/python/shapes/)

## References
* 2020, Plotly versions: Plotly, plotly.express - https://medium.com/analytics-vidhya/interactive-data-visualization-became-much-easier-with-help-of-plotly-express-64c56e781b53