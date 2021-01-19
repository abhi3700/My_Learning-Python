"""
    Badges can be used as part of buttons or links to provide a counter.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

badge = dbc.Button(
    ["Notifications", dbc.Badge("4", color="light", className= "ml-1")],
    color="primary",
)

app.layout = html.Div(badge)

if __name__ == '__main__':
    app.run_server(debug=True)