"""
    Buttons with varying size
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
        [
            dbc.Button("Large button", size= "lg", color="primary", className="mr-1"),
            dbc.Button("Regular button", color="primary", className="mr-1"),
            dbc.Button("Small button", size= "sm", color="primary"),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)
