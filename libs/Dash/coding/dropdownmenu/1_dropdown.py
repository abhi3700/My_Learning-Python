"""
    Simple example
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

dropdown = dbc.DropdownMenu(
        label="Menu",
        children= [
            dbc.DropdownMenuItem("Item 1"),
            dbc.DropdownMenuItem("Item 2"),
            dbc.DropdownMenuItem("Item 3"),
        ]
    )

app.layout = html.Div([dropdown])

if __name__ == '__main__':
    app.run_server(debug=True)