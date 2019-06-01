---
jupyter:
  jupytext:
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
    description: How to configure and style the legend in Plotly with Python.
    display_as: layout_opt
    has_thumbnail: false
    ipynb: ~notebook_demo/14
    language: python
    layout: user-guide
    name: Legends
    order: 14
    page_type: example_index
    permalink: python/legend/
    thumbnail: thumbnail/legend.jpg
    title: Legends | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Plotly's Python API is updated frequently. Run pip install plotly --upgrade to update your Plotly version.

```python
import plotly
plotly.__version__
```

#### Show Legend
By default the legend is displayed on Plotly charts with multiple traces. 

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
)

data = [trace0, trace1]
fig = go.Figure(data=data)

py.iplot(fig, filename='default-legend')
```

Add `showlegend=True` to the `layout` object to display the legend on a plot with a single trace.

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
)

data = [trace0]
layout = go.Layout(showlegend=True)
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='show-legend')
```

#### Hide Legend

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
)

data = [trace0, trace1]
layout = go.Layout(showlegend=False)
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='hide-legend')
```

#### Hide Legend Entries

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    showlegend=False
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
)

data = [trace0, trace1]
fig = go.Figure(data=data)

py.iplot(fig, filename='hide-legend-entry')
```

#### Legend Names

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    name='Positive'
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    name='Negative'
)

data = [trace0, trace1]
fig = go.Figure(data=data)

py.iplot(fig, filename='legend-names')
```

#### Horizontal Legend

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
)

data = [trace0, trace1]
layout = go.Layout(
    legend=dict(orientation="h")
)
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='horizontal-legend')
```

#### Legend Position

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
)

data = [trace0, trace1]
layout = go.Layout(
    legend=dict(x=-.1, y=1.2)
)
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='position-legend')
```

#### Style Legend

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
)
data = [trace0, trace1]

layout = go.Layout(
    legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=12,
            color='#000'
        ),
        bgcolor='#E2E2E2',
        bordercolor='#FFFFFF',
        borderwidth=2
    )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='style-legend')
```

#### Grouped Legend

```python
import plotly.plotly as py

data = [
    {
        'x': [1, 2, 3],
        'y': [2, 1, 3],
        'legendgroup': 'group', # this can be any string, not just "group"
        'name': 'first legend group',
        'mode': 'markers',
        'marker': {
            'color': 'rgb(164, 194, 244)'
        }
    },
    {
        'x': [1, 2, 3],
        'y': [2, 2, 2],
        'legendgroup': 'group',
        'name': 'first legend group - average',
        'mode': 'lines',
        'line': {
            'color': 'rgb(164, 194, 244)'
        }
    },   
    {
        'x': [1, 2, 3],
        'y': [4, 9, 2],
        'legendgroup': 'group2', 
        'name': 'second legend group',
        'mode': 'markers',
        'marker': {
            'color': 'rgb(142, 124, 195)'
        }
    },        
    {
        'x': [1, 2, 3],
        'y': [5, 5, 5],
        'legendgroup': 'group2',
        'name': 'second legend group - average',
        'mode': 'lines',
        'line': {
            'color': 'rgb(142, 124, 195)'
        }
    }
]

py.iplot(data, filename='basic-legend-grouping')
```

You can also hide entries in grouped legends: 

```python
import plotly.plotly as py

data = [
    {
        'x': [1, 2, 3],
        'y': [2, 1, 3],
        'legendgroup': 'group',
        'name': 'first legend group',
        'mode': 'markers',
        'marker': {
            'color': 'rgb(164, 194, 244)'
        }
    },
    {
        'x': [1, 2, 3],
        'y': [2, 2, 2],
        'legendgroup': 'group',
        'name': 'first legend group - average',
        'mode': 'lines',
        'line': {
            'color': 'rgb(164, 194, 244)'
        },
        'showlegend': False
    },
    {
        'x': [1, 2, 3],
        'y': [4, 9, 2],
        'legendgroup': 'group2',
        'name': 'second legend group',
        'mode': 'markers',
        'marker': {
            'color': 'rgb(142, 124, 195)'
        }
    },
    {
        'x': [1, 2, 3],
        'y': [5, 5, 5],
        'legendgroup': 'group2',
        'name': 'second legend group - average',
        'mode': 'lines',
        'line': {
            'color': 'rgb(142, 124, 195)'
        },
        'showlegend': False
    }
]

py.iplot(data, filename='hiding-entries-from-grouped-legends')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-legend) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-legend/", width="100%", height="820px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-legend/code", width="100%", height=500, frameBorder="0")
```

#### Reference
See https://plot.ly/python/reference/#layout-legend for more information!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'legend.ipynb', 'python/legend/', 'Legends | plotly',
    'How to configure and style the legend in Plotly with Python.',
    title = 'Legends | plotly',
    name = 'Legends',
    thumbnail='thumbnail/legend.jpg', language='python',
    page_type='example_index', has_thumbnail='false', display_as='layout_opt', order=14, 
    ipynb='~notebook_demo/14')
```