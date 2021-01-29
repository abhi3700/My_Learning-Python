"""
    dropdown menu direction
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

dropdown = dbc.Row(
    [
        dbc.Col(dbc.DropdownMenu( items, label="Dropdown (default)", direction= "down", className="mb-3" ), width="auto"),
        dbc.Col(dbc.DropdownMenu( items, label="Dropleft", direction= "left", className="mb-3" ), width="auto"),
        dbc.Col(dbc.DropdownMenu( items, label="DropRight", direction= "right", className="mb-3" ), width="auto"),
        dbc.Col(dbc.DropdownMenu( items, label="Dropup", direction= "up", className="mb-3" ), width="auto"),
    ],
    # justify="between",
)

app.layout = html.Div([dropdown])


if __name__ == '__main__':
    app.run_server(debug=True)