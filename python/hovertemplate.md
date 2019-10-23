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
    description: How to use hover template in Python with Plotly.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/60
    language: python
    layout: base
    name: Hover Template
    order: 40
    page_type: u-guide
    permalink: python/hovertemplate/
    thumbnail: thumbnail/hovertemplate.jpg
    title: Hover Template and Formatting| plotly
    v4upgrade: true
---

### Add Hover Template to Pie Chart

To customize the tooltip on your graph you can use [hovertemplate](https://plot.ly/python/reference/#pie-hovertemplate), which is a template string used for rendering the information that appear on hoverbox. 

```python
import plotly.graph_objects as go

fig = go.Figure(go.Pie(
    name = "",
    values = [2, 5, 3, 2.5],
    labels = ["R", "Python", "Java Script", "Matlab"],
    text = ["textA", "TextB", "TextC", "TextD"],
    hovertemplate = "%{label}: <br>Popularity: %{percent} </br> %{text}"
))

fig.show()
```

### Format Hover Template

```python
import plotly.io as pio
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")
A = []
B = []

for i in range(5):
    A = {'target': df['continent'][[i]].unique()}
    B.append(A)

data = [{
    'type': 'scatter',
    'mode': 'markers',
    'x': df['lifeExp'],
    'y': df['gdpPercap'],
    'text': df['continent'],
    'hovertemplate':
    "<b>%{text}</b><br><br>" +
    "GDP per Capita: %{y:$,.0f}<br>" +
    "Life Expectation: %{x:.0%}<br>" +
    "Population: %{marker.size:,}" +
    "<extra></extra>",
    'marker': {
      'size': df['pop'],
      'sizemode': 'area',
      'sizeref': 200000
  },
    'transforms': [{
      'type': 'filter',
      'target': df['year'],
      'orientation': '=',
      'value': 2002
  },{
      'type': 'groupby',
      'groups': df['continent'],
      'styles': B
  }]
}]

layout = {'yaxis': {'type': 'log'}}

pio.show({'data': data, 'layout': layout}, validate=False)
```

### Set Hover Template to Mapbox

```python
import plotly.graph_objects as go

token = open(".mapbox_token").read() # you need your own token

fig = go.Figure(go.Scattermapbox(
    name = "",
    mode = "markers+text+lines",
    lon = [-75, -80, -50], 
    lat = [45, 20, -20], 
    marker = {'size': 20, 'symbol': ["bus", "harbor", "airport"]},
    hovertemplate =
    "<b>%{marker.symbol} </b><br><br>" +
    "longitude: %{lon}<br>" +
    "latitude: %{lat}<br>" ))

fig.update_layout(
    mapbox = {
        'accesstoken': token,
        'style': "outdoors", 'zoom': 1},
    showlegend = False)

fig.show()
```
