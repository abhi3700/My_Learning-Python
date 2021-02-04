# Callback
## Coding
* DropdownMenu
```py
# ====================================================UI================================================================
autoplot_title = dbc.Card(
        dbc.Row(
            [
                dbc.DropdownMenu(
                    label="AutoPlot",
                    children= [
                        dbc.DropdownMenuItem("Home", id= "home-id"),
                        dbc.DropdownMenuItem("CMP", id= "cmp-id"),
                        dbc.DropdownMenuItem("Diffusion", id= "diffusion-id"),
                        dbc.DropdownMenuItem("Dry Etch", id= "dryetch-id"),
                        dbc.DropdownMenuItem("Implant", id= "implant-id"),
                        dbc.DropdownMenuItem("Photo", id= "photo-id"),
                        dbc.DropdownMenuItem("Thin Film", id= "thinfilm-id"),
                        dbc.DropdownMenuItem("Wet Etch", id= "wetetch-id"),
                        dbc.DropdownMenuItem("Yield", id= "yield-id"),
                    ],
                    bs_size="lg",
                    color="success",
                )
            ],
            justify="center",
        ),
        color="success",
        inverse=True,
        className="autoplot-shadow",
        style={
        #     'background-color': "#4caf50"
            "width": "8rem",
            "height": "3rem",
        },
    )

fab_area = dbc.Badge(children="Home", id="fab-area", className="ml-1 autoplot-shadow", pill=True, style={"color": "#424242", "background-color": "#ff8f00", "font-size": "14px"})


# ====================================================CALLBACK================================================================
# callback for changing fab_area text (badge) by clicking dropdown menu item
@app.callback(
    Output('fab-area', 'children'),
    [
        Input('home-id', 'n_clicks'),
        Input('cmp-id', 'n_clicks'),
        Input('diffusion-id', 'n_clicks'),
        Input('dryetch-id', 'n_clicks'),
        Input('implant-id', 'n_clicks'),
        Input('photo-id', 'n_clicks'),
        Input('thinfilm-id', 'n_clicks'),
        Input('wetetch-id', 'n_clicks'),
        Input('yield-id', 'n_clicks'),
    ]
)
def update_fabarea_badge(*args):
    # create a dict for mapping the button-id with desired label
    fabarea_label = { 
                        'home-id': 'Home',
                        'cmp-id': 'CMP',
                        'diffusion-id': 'Diffusion',
                        'dryetch-id': 'Dry Etch',
                        'implant-id': 'Implant',
                        'thinfilm-id': 'Thin Film',
                        'photo-id': 'Photo',
                        'wetetch-id': 'Wet Etch',
                        'yield-id': 'Yield',
                    }

    ctx = dash.callback_context
    if not ctx.triggered:
        out_text = "Home"
    else:
        button_id = ctx.triggered[0]['prop_id'].split(".")[0]
        # print(ctx.triggered[0])
        # print(button_id)
        out_text = fabarea_label[button_id]

    return out_text

```

## References
* https://community.plotly.com/t/dash-bootstrap-components-dropdownmenu-value/22011
* https://github.com/facultyai/dash-bootstrap-components/issues/141