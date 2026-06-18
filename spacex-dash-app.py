# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px


# Read SpaceX launch data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()


# Create a Dash application
app = dash.Dash(__name__)


# Create an app layout
app.layout = html.Div(children=[

    html.H1(
        'SpaceX Launch Records Dashboard',
        style={
            'textAlign': 'center',
            'color': '#503D36',
            'font-size': 40
        }
    ),


    # TASK 1: Add dropdown list for Launch Site selection

    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),


    html.Br(),


    # TASK 2: Pie chart output

    html.Div(
        dcc.Graph(id='success-pie-chart')
    ),


    html.Br(),


    html.P("Payload range (Kg):"),


    # TASK 3: Add payload range slider

    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={
            0: '0',
            1000: '1000',
            2000: '2000',
            3000: '3000',
            4000: '4000',
            5000: '5000',
            6000: '6000',
            7000: '7000',
            8000: '8000',
            9000: '9000',
            10000: '10000'
        },
        value=[min_payload, max_payload]
    ),


    html.Br(),


    # TASK 4: Scatter plot output

    html.Div(
        dcc.Graph(id='success-payload-scatter-chart')
    )

])



# ============================================================
# TASK 2:
# Callback function for success-pie-chart
# ============================================================


@app.callback(
    Output(component_id='success-pie-chart',
           component_property='figure'),
    Input(component_id='site-dropdown',
          component_property='value')
)


def get_pie_chart(entered_site):

    if entered_site == 'ALL':

        success_count = (
            spacex_df[spacex_df['class'] == 1]
            .groupby('Launch Site')
            .size()
            .reset_index(name='Success Count')
        )


        fig = px.pie(
            success_count,
            values='Success Count',
            names='Launch Site',
            title='Total Successful Launches By Site'
        )

        return fig


    else:

        filtered_df = spacex_df[
            spacex_df['Launch Site'] == entered_site
        ]


        site_success = (
            filtered_df.groupby('class')
            .size()
            .reset_index(name='count')
        )


        fig = px.pie(
            site_success,
            values='count',
            names='class',
            title=f'Total Success Launches for site {entered_site}'
        )

        return fig



# ============================================================
# TASK 4:
# Callback function for scatter plot
# ============================================================


@app.callback(
    Output(component_id='success-payload-scatter-chart',
           component_property='figure'),

    [
        Input(component_id='site-dropdown',
              component_property='value'),

        Input(component_id="payload-slider",
              component_property="value")
    ]
)


def get_scatter_plot(entered_site, payload_range):


    low = payload_range[0]
    high = payload_range[1]


    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]


    if entered_site == 'ALL':

        fig = px.scatter(

            filtered_df,

            x='Payload Mass (kg)',

            y='class',

            color='Booster Version Category',

            title='Correlation between Payload and Success for all Sites'

        )


        return fig



    else:


        filtered_df = filtered_df[
            filtered_df['Launch Site'] == entered_site
        ]


        fig = px.scatter(

            filtered_df,

            x='Payload Mass (kg)',

            y='class',

            color='Booster Version Category',

            title=f'Correlation between Payload and Success for site {entered_site}'

        )


        return fig



# Run the app

if __name__ == '__main__':
    app.run()