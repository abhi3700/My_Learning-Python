"""
    Buttons with outline
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
        [
            dbc.Button("Primary", outline= True, color="primary", className="mr-1"),
            dbc.Button("Secondary", outline= True, color="secondary", className="mr-1"),
            dbc.Button("Success", outline= True, color="success", className="mr-1"),
            dbc.Button("Warning", outline= True, color="warning", className="mr-1"),
            dbc.Button("Danger", outline= True, color="danger", className="mr-1"),
            dbc.Button("Info", outline= True, color="info", className="mr-1"),
            dbc.Button("Light", outline= True, color="light", className="mr-1"),
            dbc.Button("Dark", outline= True, color="dark", className="mr-1"),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)
