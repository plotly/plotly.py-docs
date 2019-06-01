---
jupyter:
  jupytext:
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
    description: How to make radar charts in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/202
    language: python
    layout: user-guide
    name: Radar Charts
    order: 30
    page_type: u-guide
    permalink: python/radar-chart/
    thumbnail: thumbnail/radar.gif
    title: Radar Charts | Plotly
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

#### Basic Radar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Scatterpolar(
  r = [39, 28, 8, 7, 28, 39],
  theta = ['A','B','C', 'D', 'E', 'A'],
  fill = 'toself'
)]

layout = go.Layout(
  polar = dict(
    radialaxis = dict(
      visible = True,
      range = [0, 50]
    )
  ),
  showlegend = False
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename = "radar/basic")
```

#### Multiple Trace Radar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatterpolar(
      r = [39, 28, 8, 7, 28, 39],
      theta = ['A','B','C', 'D', 'E', 'A'],
      fill = 'toself',
      name = 'Group A'
    ),
    go.Scatterpolar(
      r = [1.5, 10, 39, 31, 15, 1.5],
      theta = ['A','B','C', 'D', 'E', 'A'],
      fill = 'toself',
      name = 'Group B'
    )
]

layout = go.Layout(
  polar = dict(
    radialaxis = dict(
      visible = True,
      range = [0, 50]
    )
  ),
  showlegend = False
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename = "radar/multiple")
```

#### Reference
See https://plot.ly/python/reference/#scatterpolar for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'radar.ipynb', 'python/radar-chart/', 'Radar Charts',
    'How to make radar charts in Python with Plotly.',
    title = 'Radar Charts | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/radar.gif', 
    language='python', 
    display_as='scientific',
    order=30, 
    ipynb='~notebook_demo/202')
```

```python

```