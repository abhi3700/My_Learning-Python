import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


level3_items = [
    dbc.DropdownMenuItem("Item 5", id="item_5"),
]
level2_items = [
    dbc.DropdownMenuItem("Item 3", id="item_3"),
    dbc.DropdownMenuItem("Item 4", id="item_4"),
    dbc.DropdownMenu(level3_items),
]
level1_items = [
    html.Div(
        id="submenu",
        children=[
            dbc.DropdownMenuItem("Item 1"),
            dbc.DropdownMenuItem("Item 2"),
            dbc.DropdownMenu(level2_items),
        ],
    )
]

app.layout = dbc.Container(
    html.Div(
        id="menu",
        children=dbc.DropdownMenu(label="Menu", bs_size="lg", children=level1_items,),
    )
)


@app.callback(
    Output("submenu", "className"),
    Input("item_3", "n_clicks"),
    Input("item_4", "n_clicks"),
    Input("item_5", "n_clicks"),
    Input("menu", "n_clicks"),
)
def hide_show_submenu(*_):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    return "d-block" if input_id == "menu" else "d-none"


if __name__ == "__main__":
    app.run_server(debug=True)