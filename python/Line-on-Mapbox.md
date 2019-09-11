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
    description: How to make a Mapbox Choropleth Map of US Counties in Python with
      Plotly.
    display_as: maps
    has_thumbnail: true
    ipynb: ~notebook_demo/56
    language: python
    layout: user-guide
    name: Mapbox Choropleth Maps
    order: 1
    page_type: example_index
    permalink: python/mapbox-county-choropleth/
    thumbnail: thumbnail/mapbox-choropleth.png
    title: Python Mapbox Choropleth Maps | plotly
---


### Mapbox Access Token

To plot on Mapbox maps with Plotly you *may* need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](/python/mapbox-layers/) documentation for more information.


### How to draw a Line on a Map 

To draw a line on your map, you either can use [Scattermapbox](https://plot.ly/python/reference/#scattermapbox) or [scattergeo](https://plot.ly/python/reference/#scattergeo) trace type. Then . In this example uses scattermapbox and define the drawing [mode](https://plot.ly/python/reference/#scattermapbox-mode) to the combination of markers and line. 

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon = [10, 20, 30], lat = [10, 20,30], 
    marker = {'size': 10}))

fig.add_trace(go.Scattermapbox(
    mode = "markers+lines",      
    lon = [-50, -60,40], lat = [30, 10, -20], 
    marker = {'size': 10}))

fig.update_layout(margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain", 
        'center': {'lon': -20, 'lat': -20}, 
        'zoom': 1})

fig.show()
```

### Set Marker Symbols 

You can define a symbol on your map by setting [symbol](https://plot.ly/python/reference/#scattermapbox-marker-symbol) attribute. This attribute only works on mapbox tiles (not work on raster tiles): 
- basic
- streets
- outdoors
- light
- dark
- satellite
- satellite-streets

```python
import plotly.graph_objects as go

token = open(".mapbox_token").read() # you need your own token

fig = go.Figure(go.Scattermapbox(
    mode = "markers+text+lines",
    lon = [-75, -80, -50], lat = [45, 20, -20], 
    marker = {'size': 20, 'symbol': ["bus", "harbor", "airport"]},
    text = ["Bus", "Harbor", "airport"],textposition = "bottom right"))

fig.update_layout(
    mapbox = {
        'accesstoken': token,
        'style': "outdoors", 'zoom': 0.7},
    showlegend = False)

fig.show()
```
### Contour Line on Glob
This example uses [scattergeo](https://plot.ly/javascript/reference/#scattergeo) trace type to visualize the data as lines on a geographic map.

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/globe_contours.csv')

scl = ['blue', 'yellow', 'pink', \
    'royalblue', 'fuchsia', 'blue', \
    'brown', 'purple', 'orange']

n_colors = len(scl)

fig = go.Figure()

for i, (lat, lon) in enumerate(zip(df.columns[::2], df.columns[1::2])):
    fig.add_trace(go.Scattergeo(
        lon = df[lon],
        lat = df[lat],
        mode = 'lines',
        line = dict(width = 2, color = scl[i % n_colors]
        )))

fig.update_layout(
    title_text = 'Contour lines over globe<br>(Click and drag to rotate)',
    showlegend = False,
    geo = dict(
        showland = True,
        showcountries = True,
        showocean = True,
        countrywidth = 0.5,
        landcolor = 'orange',
        lakecolor = 'cyan',
        oceancolor = 'cyan',
        projection = dict(
            type = 'orthographic',
            rotation = dict(
                lon = -100,
                lat = 40,
                roll = 0
            )
        ),
        lonaxis = dict(
            showgrid = True,
            gridcolor = 'black',
            gridwidth = 0.5
        ),
        lataxis = dict(
            showgrid = True,
            gridcolor = 'black',
            gridwidth = 0.5
        )
    )
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#choroplethmapbox for more information about mapbox and their attribute options.
