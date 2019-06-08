import pandas as pd
import numpy as np
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import geopandas as gpd
from shapely.geometry import Point, Polygon
import plotly.plotly as py
import plotly.graph_objs as go


file=pd.read_csv('Dice_US_jobs_utf81.csv',error_bad_lines=False)
print(file.columns)

location=dict()
states_list=['AK','AR','AZ','CA','FL','LA','NM','NV','OK','OR','TX','UT','AL','CO','CT','DE','GA','IA',
            'ID','IL','IN','KS','KY','MA','WI','MD','ME','MI','MN','MO','MS',
            'MT','NC','ND','NE','NH','NJ','NY','OH','PA','WV','RI','SC','SD',
            'TN','VA','VT','WA','WY','HI','RL']
for term in file['location']:
    
    try:
        location_cur=term.split(', ')[1]
    except:
        pass
    location_cur=location_cur.upper()
    if location_cur in states_list:
        if location_cur in location:
            location[location_cur]=location[location_cur]+1
        else:
            location[location_cur]=1
for temp_state in states_list:
    if temp_state not in location:
        location[temp_state]=1
print(location)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]

# df['text'] = df['state'] + '<br>' + \
#     'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
#     'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
#     'Wheat ' + df['wheat'] + ' Corn ' + df['corn']

data = [go.Choropleth(
#     colorscale = scl,
    autocolorscale = True,
#     locations = df['code'],
    locations=list(location.keys()),
#     z = df['total exports'].astype(float),
    z=list(location.values()),
    locationmode = 'USA-states',
    visible=True,
#     text = df['text'],
    text=list(location.values()),
    hovertext=list(location.values()),
#     ids=list(location.keys()),
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "Number of Jobs")
)]

layout = go.Layout(
    title = go.layout.Title(
        text = '2017 US Jobs On Monster.com'
    ),
    hovermode='closest',
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
        legend = go.layout.Legend(
           traceorder = 'reversed'
    )
)

fig = go.Figure(data = data, layout = layout)
plotly.offline.plot(fig, filename = 'd3-cloropleth-map')