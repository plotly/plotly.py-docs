---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  plotly:
    description: How to draw lines, great circles, and contours on maps in Python.
    display_as: maps
    has_thumbnail: true
    ipynb: ~notebook_demo/58
    language: python
    layout: user-guide
    name: Lines on Maps
    order: 4
    page_type: example_index
    permalink: python/lines-on-maps/
    thumbnail: thumbnail/flight-paths.jpg
    title: Lines on maps | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Plotly's python package is updated frequently. Run `pip install plotly --upgrade` to use the latest version.

```python
import plotly
plotly.__version__
```

### US Flight Paths Map

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_airports.head()

df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
df_flight_paths.head()

airports = [go.Scattergeo(
    locationmode = 'USA-states',
    lon = df_airports['long'],
    lat = df_airports['lat'],
    hoverinfo = 'text',
    text = df_airports['airport'],
    mode = 'markers',
    marker = go.scattergeo.Marker(
        size = 2,
        color = 'rgb(255, 0, 0)',
        line = go.scattergeo.marker.Line(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    ))]

flight_paths = []
for i in range(len(df_flight_paths)):
    flight_paths.append(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
            lat = [df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
            mode = 'lines',
            line = go.scattergeo.Line(
                width = 1,
                color = 'red',
            ),
            opacity = float(df_flight_paths['cnt'][i]) / float(df_flight_paths['cnt'].max()),
        )
    )

layout = go.Layout(
    title = go.layout.Title(
        text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)'
    ),
    showlegend = False,
    geo = go.layout.Geo(
        scope = 'north america',
        projection = go.layout.geo.Projection(type = 'azimuthal equal area'),
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)

fig = go.Figure(data = flight_paths + airports, layout = layout)
py.iplot(fig, filename = 'd3-flight-paths')
```

### London to NYC Great Circle

```python
import plotly.plotly as py
import plotly.graph_objs as go

nyc_london = [go.Scattergeo(
    lat = [40.7127, 51.5072],
    lon = [-74.0059, 0.1275],
    mode = 'lines',
    line = go.scattergeo.Line(
        width = 2,
        color = 'blue',
    ),
)]

layout = go.Layout(
    title = go.layout.Title(
        text = 'London to NYC Great Circle'
    ),
    showlegend = False,
    geo = go.layout.Geo(
        resolution = 50,
        showland = True,
        showlakes = True,
        landcolor = 'rgb(204, 204, 204)',
        countrycolor = 'rgb(204, 204, 204)',
        lakecolor = 'rgb(255, 255, 255)',
        projection = go.layout.geo.Projection(
            type = "equirectangular"
        ),
        coastlinewidth = 2,
        lataxis = go.layout.geo.Lataxis(
            range = [20, 60],
            showgrid = True,
            dtick = 10
        ),
        lonaxis = go.layout.geo.Lonaxis(
            range = [-100, 20],
            showgrid = True,
            dtick = 20
        ),
    )
)

fig = go.Figure(data = nyc_london, layout = layout)
py.iplot(fig, filename = 'd3-great-circle')
```

### Contour lines on globe

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
try:
    from itertools import izip# Python 2
except ImportError:
    izip = zip# Python 3

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/globe_contours.csv')
df.head()

contours = []

scl = ['rgb(213,62,79)', 'rgb(244,109,67)', 'rgb(253,174,97)', \
    'rgb(254,224,139)', 'rgb(255,255,191)', 'rgb(230,245,152)', \
    'rgb(171,221,164)', 'rgb(102,194,165)', 'rgb(50,136,189)'
]

def pairwise(iterable):
    a = iter(iterable)
    return izip(a, a)

i = 0
for lat, lon in pairwise(df.columns):
    contours.append(go.Scattergeo(
        lon = df[lon],
        lat = df[lat],
        mode = 'lines',
        line = go.scattergeo.Line(
            width = 2,
            color = scl[i]
        )))
    i = 0 if i + 1 >= len(df.columns) / 4 else i + 1

layout = go.Layout(
    title = go.layout.Title(
        text = 'Contour lines over globe<br>(Click and drag to rotate)'
    ),
    showlegend = False,
    geo = go.layout.Geo(
        showland = True,
        showlakes = True,
        showcountries = True,
        showocean = True,
        countrywidth = 0.5,
        landcolor = 'rgb(230, 145, 56)',
        lakecolor = 'rgb(0, 255, 255)',
        oceancolor = 'rgb(0, 255, 255)',
        projection = go.layout.geo.Projection(
            type = 'orthographic',
            rotation = go.layout.geo.projection.Rotation(
                lon = -100,
                lat = 40,
                roll = 0
            )
        ),
        lonaxis = go.layout.geo.Lonaxis(
            showgrid = True,
            gridcolor = 'rgb(102, 102, 102)',
            gridwidth = 0.5
        ),
        lataxis = go.layout.geo.Lataxis(
            showgrid = True,
            gridcolor = 'rgb(102, 102, 102)',
            gridwidth = 0.5
        )
    )
)

fig = go.Figure(data = contours, layout = layout)
py.iplot(fig, filename = 'd3-globe')
```

#### Reference
See https://plot.ly/python/reference/#scattergeo for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'lines_on_maps.ipynb', 'python/lines-on-maps/', 'Lines on maps | plotly',
    'How to draw lines, great circles, and contours on maps in Python.',
    title = 'Lines on maps | plotly',
    name = 'Lines on Maps',
    has_thumbnail='true', thumbnail='thumbnail/flight-paths.jpg',
    language='python', page_type='example_index',
    display_as='maps', order=4,
    ipynb= '~notebook_demo/58')
```

```python

```
