"""
    Alerts
    - Provide contextual feedback messages for user actions with the Alert component.
    - Set the color of Alert using the color argument and one of the eight supported contextual color names.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

alerts = [
            dbc.Alert("This is a primary", color= "primary"),
            dbc.Alert("This is a secondary alert", color="secondary"),
            dbc.Alert("This is a success alert! Well done!", color="success"),
            dbc.Alert("This is a warning alert... be careful...", color="warning"),
            dbc.Alert("This is a danger alert. Scary!", color="danger"),
            dbc.Alert("This is an info alert. Good to know!", color="info"),
            dbc.Alert("This is a light alert", color="light"),
            dbc.Alert("This is a dark alert", color="dark"),
        ]


# defining array of alerts
app.layout = html.Div([alerts])

if __name__ == '__main__':
    app.run_server(debug=True)