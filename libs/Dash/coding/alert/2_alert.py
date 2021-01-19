"""
    Alert with a link
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

alerts = [
            dbc.Alert(
                [
                    "This is a primary alert with an ",
                    html.A("example link", href="https://github.com/", className="alert-link"),
                ], 
                color="primary"),
            dbc.Alert(
                [
                    "This is a danger alert with an ",
                    html.A("example link", href="https://morioh.com/p/68e6c284a59c", className="alert-link"),
                ], 
                color="danger"),

        ]

# entire layout
app.layout = html.Div(alerts)

if __name__ == '__main__':
    app.run_server(debug=True)