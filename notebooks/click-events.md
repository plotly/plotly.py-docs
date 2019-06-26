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
    description: Click Events With FigureWidget
    display_as: chart_events
    has_thumbnail: true
    ipynb: ~notebook_demo/240
    language: python
    layout: user-guide
    name: Click Events
    order: 24
    page_type: example_index
    permalink: python/click-events/
    thumbnail: thumbnail/zoom.jpg
    title: Click Events
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Update Points Using a Click Callback

```python
import plotly.graph_objs as go

import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)

f = go.FigureWidget([go.Scatter(x=x, y=y, mode='markers')])

scatter = f.data[0]
colors = ['#a3a7e4'] * 100
scatter.marker.color = colors
scatter.marker.size = [10] * 100
f.layout.hovermode = 'closest'


# create our callback function
def update_point(trace, points, selector):
    c = list(scatter.marker.color)
    s = list(scatter.marker.size)
    for i in points.point_inds:
        c[i] = '#bae2be'
        s[i] = 20
        scatter.marker.color = c
        scatter.marker.size = s


scatter.on_click(update_point)

f
```

<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/figurewidget-click-event.gif'>


#### Reference


See [these Jupyter notebooks](https://github.com/jonmmease/plotly_ipywidget_notebooks) for even more FigureWidget examples.

```python
help(scatter.on_click)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'figurewidget-click-event.ipynb', 'python/click-events/', 'Click Events with go.FigureWidget',
    'Click Events With FigureWidget',
    title = 'Click Events',
    name = 'Click Events',
    has_thumbnail='true', thumbnail='thumbnail/zoom.jpg',
    language='python', page_type='example_index',
    display_as='chart_events', order=24,
    ipynb= '~notebook_demo/240')
```

```python

```
