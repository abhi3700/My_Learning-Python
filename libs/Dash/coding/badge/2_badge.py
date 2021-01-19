"""
    Badge sizing
    - badges scale to match the size of their parent by using relative font sizing
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

badges = html.Div([
        html.H1(["Example Heading", dbc.Badge("New", className= "ml-1")]),
        html.H2(["Example Heading", dbc.Badge("New", className= "ml-1")]),
        html.H3(["Example Heading", dbc.Badge("New", className= "ml-1")]),
        html.H4(["Example Heading", dbc.Badge("New", className= "ml-1")]),
        html.H5(["Example Heading", dbc.Badge("New", className= "ml-1")]),
    ])


"""main layout"""
# app.layout = html.Div(badge)
app.layout = badges

if __name__ == '__main__':
    app.run_server(debug=True)