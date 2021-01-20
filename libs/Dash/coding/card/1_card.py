"""
    Simple example
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [
        dbc.CardImg(src="/images/placeholder286x180.png", top=True),
        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
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