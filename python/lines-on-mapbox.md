---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.3
  plotly:
    description: How to draw a line on Map in Python with Plotly.
    display_as: maps
    has_thumbnail: true
    ipynb: ~notebook_demo/56
    language: python
    layout: user-guide
    name: Lines on Mapbox
    order: 1
    page_type: example_index
    permalink: python/lines-on-mapbox/
    thumbnail: thumbnail/line_mapbox.jpg
    title: Lines on Mapbox | plotly
---

### Mapbox Access Token

To plot on Mapbox maps with Plotly you *may* need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](/python/mapbox-layers/) documentation for more information.

### How to draw a Line on a Map 

To draw a line on your map, you either can use [line_mapbox](https://www.plotly.express/plotly_express/#plotly_express.line_mapbox) in plotly express, or [Scattermapbox](https://plot.ly/python/reference/#scattermapbox) and [scattergeo](https://plot.ly/python/reference/#scattergeo) trace type in plotly. Below we show you how to draw a line on Mapbox using plotly express.

```python
import pandas as pd

us_cities1 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
States = ['New York', 'Ohio']
us_cities = us_cities1[us_cities1.State.isin(States)]

import plotly.express as px

fig = px.line_mapbox(
    us_cities, 
    lat="lat", 
    lon="lon", 
    line_group='State', 
    hover_name="City", 
    hover_data=["State", "Population"],
    color_discrete_sequence=["fuchsia"], 
    zoom=3, 
    height=300)

fig.update_layout(
    mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 41,
    margin={"r":0,"t":0,"l":0,"b":0})

fig.show()
```

This example uses scattermapbox and defines
the drawing [mode](https://plot.ly/python/reference/#scattermapbox-mode) to the combination of markers and line.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon = [10, 20, 30], 
    lat = [10, 20,30], 
    marker = {'size': 10}))

fig.add_trace(go.Scattermapbox(
    mode = "markers+lines",      
    lon = [-50, -60,40], 
    lat = [30, 10, -20], 
    marker = {'size': 10}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain", 
        'center': {'lon': -20, 'lat': -20}, 
        'zoom': 1})

fig.show()
```

This example uses scattermapbox trace and shows how to customize hoverinfo in Mapbox.

```python
import pandas as pd

us_cities1 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
States = ['Washington']
us_cities = us_cities1[us_cities1.State.isin(States)]

import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(   
    lat=us_cities.lat, 
    lon=us_cities.lon, 
    mode='markers+lines',
    marker={'color':'fuchsia', 'size':10, 'opacity':0.8},
    hovertext=us_cities['City'],
    hoverinfo='lat+lon+text'))

fig.update_layout(
    mapbox={'style': 'stamen-terrain', 'center':{'lat':47, 'lon':-117}, 'zoom':5},
    margin={"r":0,"t":0,"l":0,"b":0})

fig.show()

```

#### Reference
See https://plot.ly/python/reference/#scattermapbox for more information about mapbox and their attribute options.
