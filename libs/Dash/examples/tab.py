import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
	dcc.Tabs(
		tabs=[{'label':'Pie1', 'value': 1},
			{'label': 'Pie2', 'value': 2},
			{'label': 'Pie3', 'value': 3},
			{'label': 'Pie4', 'value': 4}
			],
		value=1,
		id='tabs'
		),
	html.Div(id='output-tab')
	])


# Reference
# ===========
# https://community.plot.ly/t/how-to-create-a-pie-chart-in-dash-app-under-a-particular-tab/7700/2