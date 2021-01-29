"""
    sizing dropdown menu
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

items = [
    dbc.DropdownMenuItem("First"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Second"),
]

dropdown = html.Div(
    [
        dbc.DropdownMenu( items, label="large dropdown", bs_size="lg", className="mb-3" ),
        dbc.DropdownMenu( items, label="normal dropdown", className="mb-3" ),
        dbc.DropdownMenu( items, label="small dropdown", bs_size="sm", className="mb-3" ),
    ]
)

app.layout = html.Div([dropdown])


if __name__ == '__main__':
    app.run_server(debug=True)