"""
    dropdown menu with style
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

items = [
    dbc.DropdownMenuItem("Item 1"),
    dbc.DropdownMenuItem("Item 2"),
    dbc.DropdownMenuItem("Item 3"),
    ]

dropdown = html.Div([
    dbc.DropdownMenu( items, label="Primary", color="primary", className="m-1" ),
    dbc.DropdownMenu( items, label="Secondary", color="secondary", className="m-1" ),
    dbc.DropdownMenu( items, label="Success", color="success", className="m-1" ),
    dbc.DropdownMenu( items, label="Warning", color="warning", className="m-1" ),
    dbc.DropdownMenu( items, label="Danger", color="danger", className="m-1" ),
    dbc.DropdownMenu( items, label="Info", color="info", className="m-1" ),
    dbc.DropdownMenu( items, label="Link", color="link", className="m-1" ),
    ],
    style={
    "display":"flex",           # it's for displaying horizontally
    "flexWrap": "wrap"          # optional
    },
)


app.layout = html.Div([dropdown])


if __name__ == '__main__':
    app.run_server(debug=True)