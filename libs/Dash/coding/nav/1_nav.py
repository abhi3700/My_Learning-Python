"""
    Simple example
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

dropdown = dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Active", active=True, href="#")),
            dbc.NavItem(dbc.NavLink("A link", href="#")),
            dbc.NavItem(dbc.NavLink("Another link", href="#")),
            dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
            dbc.DropdownMenu(
                [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
                label="Dropdown",
                nav=True,
            ),
        ]
    )

app.layout = html.Div([dropdown])

if __name__ == '__main__':
    app.run_server(debug=True)