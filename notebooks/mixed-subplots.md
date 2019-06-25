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
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to make mixed subplots in Python with Plotly.
    display_as: multiple_axes
    has_thumbnail: true
    ipynb: ~notebook_demo/132
    language: python
    layout: user-guide
    name: Mixed Subplots
    order: 5
    page_type: example_index
    permalink: python/mixed-subplots/
    thumbnail: thumbnail/mixed_subplot.JPG
    title: Mixed Subplots | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Subplots with multiple chart types (i.e. cartesian and 3D) are available in version <b>1.12.11+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Mixed Subplot

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

# read in volcano database data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv')

# frequency of Country
freq = df
freq = freq.Country.value_counts().reset_index().rename(columns={'index': 'x'})

# plot(1) top 10 countries by total volcanoes
locations = go.Bar(x=freq['x'][0:10],y=freq['Country'][0:10], marker=dict(color='#CF1020'))

# read in 3d volcano surface data
df_v = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

# plot(2) 3d surface of volcano
threed = go.Surface(z=df_v.values.tolist(), colorscale='Reds', showscale=False)

# plot(3)  scattergeo map of volcano locations
trace3 = {
  "geo": "geo3",
  "lon": df['Longitude'],
  "lat": df['Latitude'],
  "hoverinfo": 'text',
  "marker": {
    "size": 4,
    "opacity": 0.8,
    "color": '#CF1020',
    "colorscale": 'Viridis'
  },
  "mode": "markers",
  "type": "scattergeo"
}

data = [locations, threed, trace3]

# control the subplot below using domain in 'geo', 'scene', and 'axis'
layout = {
  "plot_bgcolor": 'black',
  "paper_bgcolor": 'black',
  "titlefont": {
      "size": 20,
      "family": "Raleway"
  },
  "font": {
      "color": 'white'
  },
  "dragmode": "zoom",
  "geo3": {
    "domain": {
      "x": [0, 0.55],
      "y": [0, 0.9]
    },
    "lakecolor": "rgba(127,205,255,1)",
    "oceancolor": "rgb(6,66,115)",
    "landcolor": 'white',
    "projection": {"type": "orthographic"},
    "scope": "world",
    "showlakes": True,
    "showocean": True,
    "showland": True,
    "bgcolor": 'black'
  },
  "margin": {
    "r": 10,
    "t": 25,
    "b": 40,
    "l": 60
  },
  "scene": {"domain": {
      "x": [0.5, 1],
      "y": [0, 0.55]
    },
           "xaxis": {"gridcolor": 'white'},
           "yaxis": {"gridcolor": 'white'},
           "zaxis": {"gridcolor": 'white'}
           },
  "showlegend": False,
  "title": "<br>Volcano Database",
  "xaxis": {
    "anchor": "y",
    "domain": [0.6, 0.95]
  },
  "yaxis": {
    "anchor": "x",
    "domain": [0.65, 0.95],
    "showgrid": False
  }
}

annotations = { "text": "Source: NOAA",
               "showarrow": False,
               "xref": "paper",
               "yref": "paper",
               "x": 0,
               "y": 0}

layout['annotations'] = [annotations]

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename = "Mixed Subplots Volcano")
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'mixed-subplots.ipynb', 'python/mixed-subplots/', 'Mixed Subplots',
    'How to make mixed subplots in Python with Plotly.',
    title = 'Mixed Subplots | plotly',
    name = 'Mixed Subplots',
    has_thumbnail='true', thumbnail='thumbnail/mixed_subplot.JPG',
    language='python', page_type='example_index',
    display_as='multiple_axes', order=5,
    ipynb= '~notebook_demo/132')
```

```python

```
