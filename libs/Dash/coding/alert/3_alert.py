"""
    Alert with additional content
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

alerts = dbc.Alert(
        [
            html.H4("Well done!", className="alert-heading"),
            html.P(
                "This is a success alert with loads of extra text in it. So much "
                "that you can see how spacing within an alert works with this "
                "kind of content."                   
            ),
            html.Hr(),
            html.P(
                "Let's put some more text down here, but remove the bottom margin",
                className="mb-0",
            ),
        ]
    )

# entire layout
app.layout = html.Div(alerts)

if __name__ == '__main__':
    app.run_server(debug=True)

