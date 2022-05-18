from dash import dash, html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
import re
import base64
import prediction
import pandas as pd
import os

df = pd.read_csv('data.csv')


def create_product_card(img_path):
    a = img_path
    img_id = int(re.findall('[\d]+', a)[0])
    try:
        heading = df[df['id'] == img_id]['productDisplayName'].iloc[0]
        # print(heading)
    except:
        heading = 'No info found'

    card = dbc.Card(
        [dbc.Carousel(
            items=[{"key": "1", "src": img_path}], controls=False, indicators=False),
            dbc.CardBody(
                [
                    html.Label(heading[:30], className="card-title text-black"),
                    # dbc.Button(btn_name, color="primary"),
                    html.Br(),
                    dbc.CardLink("Web Search", href=f'https://www.google.com/search?q={"+".join(heading.split())}',
                                 target="_blank",className='text-primary'),
                ], className='text-center',
            ),
        ],
        style={"width": "200px", 'height': '400px'}, className='bg-light'
    ),
    return card


recommend_div = dbc.Container([
    dbc.Row([
        dbc.Card('Fashion Product Recommender Dashboard', className='text-center fs-4 fw-bold'),
        html.Br(),
        dbc.Row([
            dbc.Card([dbc.Row([
                dbc.Col([html.Img(id='input-img', style={
                    'width': '150px',
                    'height': '150px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',

                }),
                         html.Label('Uploaded Image')]),

                dbc.Col([dcc.Upload(['Drag and Drop or ', html.Br(), html.A('Select a File')],
                                    style={'width': '150px',
                                           'height': '150px',
                                           'lineHeight': '60px',
                                           'borderWidth': '1px',
                                           'borderStyle': 'dashed',
                                           'borderRadius': '5px',
                                           'textAlign': 'center'},
                                    id='upload-image'),
                         html.Label('Upload Here')])]),
                dbc.Row([dbc.Button('Show Recommendations', id='show-btn', n_clicks=0, className='m-2 text-center',
                                    style={'width': '50%', })],
                        justify='center',
                        align='center',
                        style={'textAlign': 'center'})

            ], className='p-2', style={'text-align': 'center','width': '350px'})
            ], className='p-3', style={'text-align': 'center'}, align='center', justify='center'),

        html.Div(dbc.Card([html.Label("10 closest Recommendations")], className='bg-light')),
        html.Br(),
dcc.Loading([
        dbc.Row([

            dbc.Col(id='product1'),
            dbc.Col(id='product2'),
            dbc.Col(id='product3'),
            dbc.Col(id='product4'),
            dbc.Col(id='product5'),
            dbc.Col(id='product6'),
            dbc.Col(id='product7'),
            dbc.Col(id='product8'),
            dbc.Col(id='product9'),
            dbc.Col(id='product10'),
        ],className='m-2')
],color="#119DFF", type="cube", fullscreen=True,className='bg-dark')

    ], justify='center', align='center', style={'text-align': 'center'})
])


def parse_contents(contents):
    return html.Div([
        html.Img(src=contents, style={'width': '200px', 'height': '200px'}),

    ])


@callback(
    Output('input-img', 'src'),
    Input('upload-image', 'contents')
)
def update_input_img(contents):
    if contents is not None:
        decodeit = open('assets/input_img.jpeg', 'wb')
        decodeit.write(base64.b64decode((contents.split('base64,')[1])))
        decodeit.close()
        return contents
    else:
        return 'assets/product.png'


@callback(
    Output('product1', 'children'),
    Output('product2', 'children'),
    Output('product3', 'children'),
    Output('product4', 'children'),
    Output('product5', 'children'),
    Output('product6', 'children'),
    Output('product7', 'children'),
    Output('product8', 'children'),
    Output('product9', 'children'),
    Output('product10', 'children'),
    Input('show-btn', 'n_clicks')
)
def update_result(n_clicks):
    if n_clicks > 0:
        try:
            result = prediction.get_result('assets/input_img.jpeg')
            os.remove("assets/input_img.jpeg")
            return create_product_card(result[0]), create_product_card(result[1]), \
               create_product_card(result[2]), create_product_card(result[3]),create_product_card(result[4]), \
               create_product_card(result[5]),create_product_card(result[6]),create_product_card(result[7]),\
                create_product_card(result[8]),create_product_card(result[9])
        except :
            return  html.P(''), html.P(''),html.P(''), html.P(''),html.P(''),html.P('Upload Image First or Change the Image!'), html.P(''), html.P(''),html.P(''), html.P(''),
    else:
        return html.P(''), html.P(''), html.P(''), html.P(''), html.P(''),html.P(''), html.P(''), html.P(''), html.P(''), html.P('')
