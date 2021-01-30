"""
    Simple example
    NOTE: for keeping images, keep inside "assets/" folder.

    FACT:
    Including custom CSS or JavaScript in your Dash apps is simple. Just create a folder 
    named assets in the root of your app directory and include your CSS and JavaScript files 
    in that folder. Dash will automatically serve all of the files that are included in this 
    folder. By default the url to request the assets will be /assets but you can customize this 
    with the assets_url_path argument to dash.Dash.
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [
        dbc.CardImg(src="/assets/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text"
                ),
                dbc.Button("Go somewhere", color="primary")
            ])
    ],
    style={"width": "18rem"}
    )

app.layout = html.Div([card])

if __name__ == '__main__':
    app.run_server(debug=True)