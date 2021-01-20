"""
    Using buttons
    - Use the n_clicks prop as an input to your callbacks to trigger the callback when buttons are clicked by the user.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
        [
            dbc.Button("Click me", id="example-button", className="mr-2"),
            html.Span(id="example-output", style={"verticle-align": "middle"}),
        ]
    )

@app.callback(
    Output("example-output", "children"),
    [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"Clicked {n} times."

if __name__ == '__main__':
    app.run_server(debug=True)