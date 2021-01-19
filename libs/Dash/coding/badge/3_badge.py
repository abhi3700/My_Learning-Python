"""
    Badge conteztual color
    - Use the color argument to apply one of Bootstrap's contextual color classes.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

"""
NOTE: Here, `span` is used instead of `div` because `span` is to stylize texts 
     & the later is used for creating CSS based layouts
"""
badges = html.Span([
            dbc.Badge("Primary", color="primary", className="mr-1"),
            dbc.Badge("Secondary", color="secondary", className="mr-1"),
            dbc.Badge("Success", color="success", className="mr-1"),
            dbc.Badge("Warning", color="warning", className="mr-1"),
            dbc.Badge("Danger", color="danger", className="mr-1"),
            dbc.Badge("Info", color="info", className="mr-1"),
            dbc.Badge("Light", color="light", className="mr-1"),
            dbc.Badge("Dark", color="dark"),
    ])


"""main layout"""
# app.layout = html.Div(badge)
app.layout = badges

if __name__ == '__main__':
    app.run_server(debug=True)