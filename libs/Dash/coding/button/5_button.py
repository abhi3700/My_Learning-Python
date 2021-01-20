"""
    Block button
    - Create a block level button (one which spans the full width of the parent) by seeing block=True.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
        [
            dbc.Button("Block button", color="primary", block=True),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)
