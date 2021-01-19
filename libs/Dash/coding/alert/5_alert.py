"""
    toggle alert with auto dismissal
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

@app.callback(
    Output("alert-auto", "is_open"),
    [Input("alert-toggle-auto", "n_clicks")],
    [State("alert-auto", "is_open")],
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open


app.layout = html.Div(
        [
            dbc.Button("Toggle", id="alert-toggle-auto", className="mr-1"),
            html.Hr(),
            dbc.Alert(
                "Hello! I am an alert",
                id="alert-auto",
                is_open=True,
                duration=4000       # in milliseconds
            ),
        ])


if __name__ == '__main__':
    app.run_server(debug=True)