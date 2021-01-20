"""
    Buttongroup with dropdown menu
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dbc.ButtonGroup(
            [
            dbc.Button("First"), 
            dbc.Button("Second"), 
            dbc.DropdownMenu([dbc.DropdownMenuItem("Item 1"),dbc.DropdownMenuItem("Item 2")],
                label="Dropdown",
                group=True)
            ],
            ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)