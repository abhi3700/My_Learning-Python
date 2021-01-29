"""
    Simple example with links
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

dropdown = html.Div([
    dbc.DropdownMenu(
        label="Menu",
        children= [
            dbc.DropdownMenuItem("A button", id= "dropdown-button"),
            dbc.DropdownMenuItem(
                "Internal link", href="https://github.com/"),
            dbc.DropdownMenuItem("External Link", href="https://github.com/"),
            dbc.DropdownMenuItem("External relative", href="https://github.com/", external_link= True),
        ]
    ),
    html.P(id="item-clicks", className="mt-3")
])


@app.callback(
    Output("item-clicks", "children"), [Input("dropdown-button", "n_clicks")]
    )
def count_clicks(n):
    if n:
        return f"Button clicked {n} times"
    return "Button not clicked yet."

app.layout = html.Div([dropdown])


if __name__ == '__main__':
    app.run_server(debug=True)