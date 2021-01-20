"""
    Button with Active and disabled states
    - When a user hovers the cursor over a button the background and border
     will darken in response. You can enforce this active state if needed by setting active=True.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
        [
            dbc.Button("Regular", color="primary", className="mr-1"),
            dbc.Button("Active", color="primary", active=True, className="mr-1"),
            dbc.Button("Disabled", color="primary", disabled=True),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)
