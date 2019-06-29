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

## Repositories
* [WorkCloud Plot](https://github.com/PrashantSaikia/Wordcloud-in-Plotly)
