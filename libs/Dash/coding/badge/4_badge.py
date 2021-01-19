"""
    Pill badges
    - Set pill=True to make the badges more rounded (with a larger border-radius and additional horizontal padding).
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

badges = html.Span([
            dbc.Badge("Primary", pill= True, color="primary", className="mr-1"),
            dbc.Badge("Secondary", pill= True, color="secondary", className="mr-1"),
            dbc.Badge("Success", pill= True, color="success", className="mr-1"),
            dbc.Badge("Warning", pill= True, color="warning", className="mr-1"),
            dbc.Badge("Danger", pill= True, color="danger", className="mr-1"),
            dbc.Badge("Info", pill= True, color="info", className="mr-1"),
            dbc.Badge("Light", pill= True, color="light", className="mr-1"),
            dbc.Badge("Dark", pill= True, color="dark"),
    ])

app.layout = badges

if __name__ == '__main__':
    app.run_server(debug=True)