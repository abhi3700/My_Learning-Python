# Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# defining array of children
app.layout = html.Div(children=[
	html.H1('Abhijit Roy'),
	html.H2('EOS Blockchain Developer'),
	html.H3('C++, Python, Java, XML'),
	html.H4('Android, Blockchain, Git, Excel-Python'),
	html.H5('Udacity, Udemy, Coursera'),
	html.H6('Github, Twitter, Facebook')
	])

if __name__ == '__main__':
	app.run_server(debug=True)