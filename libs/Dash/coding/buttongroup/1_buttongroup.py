"""
    - Wrap a list of Button components with ButtonGroup.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
        dbc.ButtonGroup([
                dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")
            ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)