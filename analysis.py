import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback, State
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly.graph_objs as go

# df2 = pd.read_csv('data.csv')
df = pd.read_csv('data.csv')

dashboard = dcc.Loading([dbc.Row([
    dbc.Row([
        dbc.Card([
            html.H4('Data Analysis Dashboard'),
        ], className='bg-success bg-gradient text-black'),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    html.Label(' Filter Data: ')
                ], className='bg-gradient ')

            ], width='auto'),
            dbc.Col([
                dcc.Dropdown([x for x in df.columns][2:-1], id='columns',
                             style={'color': 'black'}, placeholder="Select Field...(Default no filter applied)"),
            ]),
            dbc.Col([
                dcc.Dropdown(id='col_value', multi=True, style={'color': 'black'}, placeholder='Select Sub-Field...'),
            ])

        ], className='m-2', align='center', justify='center'),

    ], className='p-2'),
    dbc.Row([
        dbc.Col([
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Label('Total Records', className='text-black'),
                        html.H1(df.shape[0], id='features', className='text-white')
                    ]),
                ], color="primary", className='m-2 bg-gradient'),
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Label('Total Features', className='text-black'),
                        html.H1(df.shape[1], id='features', className='text-white')
                    ]),
                ], color="primary", className='m-2 bg-gradient'),
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Label('Null Values', className='text-black '),
                        html.H1(df.isnull().sum().sum(), id='features', className='text-white')
                    ]),
                ], color="primary", className='m-2 bg-gradient'),
            ]),
            dbc.Col([
                dbc.Col([
                    dbc.Card([html.Header(f'Null Values {str(round((df.isnull().mean() * 100).sum(), 2))} %',
                                          className='text-black'),
                              daq.Gauge(id='acc_gauge',
                                        color={"gradient": True,
                                               "ranges": {"red": [30, 100], "yellow": [10, 30], "green": [0, 10]}},
                                        value=round((df.isnull().mean() * 100).sum(), 2), max=100, min=0, size=110),
                              # html.P(str(round((df.isnull().mean() * 100).sum(), 2)) + '%')
                              ], className=' bg-success m-2 bg-gradient')
                ]),
            ]),

        ], xl=2, lg=2, md=6, sm=12, xs=12),
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    dbc.Col([
                        dcc.Graph(id='gender_bar')
                    ]),
                ], style={'width': 'auto', 'border-radius': '3px'}, className='m-1'),

                dbc.Card([
                    dbc.Col([
                        dcc.Graph(id='category_pie')
                    ]),
                ], style={'width': 'auto', 'border-radius': '3px'}, className='m-1'),

                dbc.Card([
                    dbc.Col([
                        dcc.Graph(id='subcat_sunburst')
                    ]),
                ], style={'width': 'auto', 'border-radius': '3px'}, className='m-1'),
                dbc.Card([
                    dbc.Col([
                        dcc.Graph(id='brand_pie')
                    ]),
                ], style={'width': 'auto', 'border-radius': '3px'}, className='m-1'),
            ]),

            dbc.Row([
                dbc.Card([
                    dbc.Col([
                        dcc.Graph(id='color_stackbar')
                    ]),
                ], style={'width': 'auto', 'border-radius': '3px'}, className='m-1'),

                dbc.Card([
                    dbc.Col([
                        dcc.Graph(id='usage_pie')
                    ]),
                ], style={'width': 'auto', 'border-radius': '3px'}, className='m-1'),

                dbc.Card([
                    dbc.Col([

                        dcc.Graph(id='season_funnel')
                    ]),
                ], style={'width': 'auto', 'border-radius': '3px'}, className='m-1'),
            ])
        ]),
    ])
], justify='center', align='center', style={'text-align': 'center'})
], color="#119DFF", type="graph", fullscreen=True, className='bg-dark')

df = df.dropna()


def update_gender(df):
    gender = df['gender'].value_counts().reset_index()
    fig = px.bar(x=gender['index'], y=gender['gender'], color=gender['index'],
                 labels={'x': 'Gender', 'y': 'Product Counts'}, template='plotly_dark', width=230, height=220)
    fig.update_layout(title_text='Gender and Products', title_x=0.5)
    fig.update(layout_showlegend=False)
    fig.update_layout(
        margin=dict(l=2, r=2, t=30, b=2),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig


def update_category(df):
    mastercategory = df['masterCategory'].value_counts().reset_index()
    fig = px.pie(data_frame=mastercategory, names='index', values='masterCategory', hole=0.5,
                 template='plotly_dark', width=190, height=200)
    fig.update(layout_showlegend=False)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    # fig.update_layout(title_text='Category', title_x=0.5)
    fig.update_layout(
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Category', x=0.5, y=0.5, font_size=15, showarrow=False),
                     ])
    fig.update_layout(
        margin=dict(l=2, r=2, t=30, b=2),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig


def update_subcategory(df):
    fig = px.sunburst(df, path=['masterCategory', 'subCategory'],
                      width=190, height=200, color_discrete_sequence=px.colors.qualitative.G10)
    fig.update_layout(title_text='Category SubCategory', title_x=0.5, font_color='white')
    fig.update_layout(
        margin=dict(l=2, r=2, t=40, b=2),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig


def update_brand(df):
    df['brand'] = df['productDisplayName'].str.split().str[0]
    brand = df['brand'].value_counts().head().reset_index()
    layout = go.Layout(
        autosize=False,
        width=250,
        height=200, )
    fig = go.Figure(data=[go.Pie(labels=brand['index'], values=brand['brand'])], layout=layout)
    fig.update_traces(textposition='inside', textinfo='percent+label+value', hole=.4)
    fig.update_layout(title_text='Top 5 Brands', title_x=0.5, font_color='white')
    fig.update(layout_showlegend=False)

    fig.update_layout(
        margin=dict(l=2, r=2, t=40, b=2),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig


def update_productColor(df):
    colors = df[['gender', 'baseColour']].value_counts().reset_index()
    fig = px.bar(colors, x='gender', y=0, color='baseColour', width=340, height=240,
                 text='baseColour')
    fig.update_yaxes(title_text='Product Counts')
    fig.update(layout_showlegend=False)
    fig.update_layout(title_text='Product Color and Gender', title_x=0.5, font_color='white')
    fig.update_layout(
        margin=dict(l=2, r=2, t=35, b=2),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig


def update_usage(df):
    usage = df['usage'].value_counts().reset_index()
    fig = px.pie(usage, values='usage', names='index', color_discrete_sequence=px.colors.sequential.RdBu,
                 width=190, height=240)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update(layout_showlegend=False)
    fig.update_yaxes(visible=False)
    fig.update_layout(title_text='Usage Type', title_x=0.5, font_color='white')
    fig.update_layout(
        margin=dict(l=2, r=2, t=35, b=2),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig


def update_season(df):
    season = df['season'].value_counts().reset_index()
    fig = px.funnel(season, x='season', y='index', color='season', text='index', width=370, height=240)
    # fig = px.funnel(season, x=0, y='season', color='gender',width=400, height=200,)
    fig.update(layout_showlegend=False)
    fig.update_yaxes(visible=False)
    fig.update_layout(title_text='Season', title_x=0.5, font_color='white')
    fig.update_layout(
        margin=dict(l=2, r=2, t=35, b=2),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig


@callback(
    Output('col_value', 'options'),
    Input('columns', 'value')
)
def update_drop(x):
    if x == '' or x is None:
        return ['']
    else:
        x = df[x].value_counts().index.tolist()
        return x


@callback(
    # Output('data-selected', 'children'),
    Output('gender_bar', 'figure'),
    Output('category_pie', 'figure'),
    Output('subcat_sunburst', 'figure'),
    Output('brand_pie', 'figure'),
    Output('color_stackbar', 'figure'),
    Output('usage_pie', 'figure'),
    Output('season_funnel', 'figure'),
    Input('columns', 'value'),
    Input('col_value', 'value'))
def update_data(x, y):
    df2 = None
    if x is not None and y is not None:
        df2 = df[df[x].isin(y)]
    else:
        df2 = df
    df2 = df2.dropna()
    gender = update_gender(df2)
    category = update_category(df2)
    subcat = update_subcategory(df2)
    brand = update_brand(df2)
    color = update_productColor(df2)
    usage = update_usage(df2)
    season = update_season(df2)
    return gender, category, subcat, brand, color, usage, season
