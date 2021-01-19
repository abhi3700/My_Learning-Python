"""
    Links
    - Add a link with the href argument to create actionable badges with hover and focus states.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

badges = html.Span([
            dbc.Badge("Primary", href="https://github.com", pill= True, color="primary", className="mr-1"),
            dbc.Badge("Secondary", href="https://github.com", pill= True, color="secondary", className="mr-1"),
            dbc.Badge("Success", href="https://github.com", pill= True, color="success", className="mr-1"),
            dbc.Badge("Warning", href="https://github.com", pill= True, color="warning", className="mr-1"),
            dbc.Badge("Danger", href="https://github.com", pill= True, color="danger", className="mr-1"),
            dbc.Badge("Info", href="https://github.com", pill= True, color="info", className="mr-1"),
            dbc.Badge("Light", href="https://github.com", pill= True, color="light", className="mr-1"),
            dbc.Badge("Dark", href="https://github.com", pill= True, color="dark"),
    ])

app.layout = badges

if __name__ == '__main__':
    app.run_server(debug=True)