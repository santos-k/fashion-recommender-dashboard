from dash import dash, html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
import base64
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup

import prediction
df = pd.read_csv('flipkart_data.csv')


def create_product_card(index):
    img_url = df.iloc[index]['img']
    title = df.iloc[index]['title']
    url = df.iloc[index]['url']

    data = requests.get(url)
    # print('data get')
    soup = BeautifulSoup(data.text, 'html.parser')
    ratings = soup.find_all('div', {'class': '_3LWZlK _3uSWvT'})
    price_web = soup.find_all('div', {'class': '_30jeq3 _16Jk6d'})
    rating = 0
    price = 0
    # print(rating,price)
    for i in ratings: rating = i.text
    for i in price_web: price = i.text

    heading = title

    card = dbc.Card(
        [dbc.Carousel(
            items=[{"key": "1", "src": img_url, "img_style": {'max-height': "200px"}}], controls=False,
            indicators=False),
            dbc.CardBody(
                [
                    html.Label(f'{heading[:30]}...', className="card-title text-black"),
                    html.Br(),
                    html.Div([
                        dbc.Badge([
                            dbc.Row([
                                dbc.Col([
                                    html.Label('₹')
                                ], width="auto"),

                                dbc.Col([
                                    html.Label(price.replace('₹', ''))
                                ])
                            ])
                        ], pill=True, color="primary", className="me-1", style={}),
                        dbc.Badge([
                            dbc.Row([
                                dbc.Col([
                                    html.Img(src='assets/star.svg')
                                ], width="auto"),

                                dbc.Col([
                                    html.Label(rating)
                                ])
                            ])
                        ], pill=True, color="primary", className="me-1", style={}),

                    ]),

                    dbc.Button("Buy", outline=True, href=url, size='sm', target="_blank", color="danger",
                               className="m-2", style={'height': 'auto'}),
                    # html.Br(),
                    # dbc.CardLink("Buy", className='text-primary'),
                ], className='text-center',
            ),
        ],
        style={"width": "200px", 'height': '350px'}, className='bg-gradient, m-2'
    ),

    return card


recommend_div = dbc.Container([
    dbc.Row([
        dbc.Badge('Flipkart Fashion Product Recommender', pill=True, color="success", text_color='black',
                  className="me-1 text-center fs-4 fw-bold", style={'width': "auto"}),
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

                dbc.Col([dcc.Upload(['Drag and Drop or ', html.Br(), html.A('Select an Image', href='#')],
                                    style={'width': '150px',
                                           'height': '150px',
                                           'lineHeight': '60px',
                                           'borderWidth': '1px',
                                           'borderStyle': 'dashed',
                                           'borderRadius': '5px',
                                           'textAlign': 'center'},
                                    id='upload-image'),
                         html.Label('Upload Here')])]),
                dbc.Row([dbc.Button('Search', outline=True, color="primary", id='show-btn', n_clicks=0,
                                    className='m-2 text-center',
                                    style={'width': '50%', })],
                        justify='center',
                        align='center',
                        style={'textAlign': 'center'})

            ], className='p-2 bg-gradient', style={'text-align': 'center', 'width': '350px'})
        ], className='p-3', style={'text-align': 'center'}, align='center', justify='center'),
        html.Div(dbc.Badge('Recommendations', color='#85e35f', text_color='black')),
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
            ], className='m-2')
        ], color="#119DFF", type="default", fullscreen=True, className='bg-dark bg-gradient')

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
            # print(result)
            return create_product_card(result[0]), create_product_card(result[1]), \
                   create_product_card(result[2]), create_product_card(result[3]), create_product_card(result[4]), \
                   create_product_card(result[5]), create_product_card(result[6]), create_product_card(result[7]), \
                   create_product_card(result[8]), create_product_card(result[9])
        except:
            return html.P(''), html.P(''), html.P(''), html.P(''), html.P(
                'Upload Image First or Change the Image!'), html.P(''), html.P(''), html.P(''), html.P(''), html.P(''),
    else:
        return html.P(''), html.P(''), html.P(''), html.P(''), html.P(''), html.P(''), html.P(''), html.P(''), html.P(
            ''), html.P('')
