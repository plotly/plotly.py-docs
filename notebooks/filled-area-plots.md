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
    description: How to make filled area plots in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/8
    language: python
    layout: user-guide
    name: Filled Area Plots
    order: 3.5
    page_type: u-guide
    permalink: python/filled-area-plots/
    thumbnail: thumbnail/area.jpg
    title: Filled Area Plots | plotly
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

#### Basic Overlaid Area Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[0, 2, 3, 5],
    fill='tozeroy'
)
trace2 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[3, 5, 1, 7],
    fill='tonexty'
)

data = [trace1, trace2]
py.iplot(data, filename='basic-area')
```

#### Overlaid Area Chart Without Boundary Lines

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[0, 2, 3, 5],
    fill='tozeroy',
    mode= 'none'
)
trace2 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[3, 5, 1, 7],
    fill='tonexty',
    mode= 'none'
)

data = [trace1, trace2]
py.iplot(data, filename='basic-area-no-bound')
```

#### Interior Filling for Area Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[3, 4, 8, 3],
    fill= None,
    mode='lines',
    line=dict(
        color='rgb(143, 19, 131)',
    )
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 6, 2, 6],
    fill='tonexty',
    mode='lines',
    line=dict(
        color='rgb(143, 19, 131)',
    )
)

data = [trace0, trace1]
py.iplot(data, filename='filling-interior-area')
```

#### Stacked Area Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

# Add original data
x=['Winter', 'Spring', 'Summer', 'Fall']

trace0 = dict(
    x=x,
    y=[40, 60, 40, 10],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(131, 90, 241)'),
    stackgroup='one'
)
trace1 = dict(
    x=x,
    y=[20, 10, 10, 60],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(111, 231, 219)'),
    stackgroup='one'
)
trace2 = dict(
    x=x,
    y=[40, 30, 50, 30],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(184, 247, 212)'),
    stackgroup='one'
)
data = [trace0, trace1, trace2]

fig = dict(data=data)
py.iplot(fig, filename='stacked-area-plot-hover', validate=False)
```

### Stacked Area Chart with Normalized Values

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = dict(
    x=['Winter', 'Spring', 'Summer', 'Fall'],
    y=['40', '20', '30', '40'],
    mode='lines',
    line=dict(width=0.5,
              color='rgb(184, 247, 212)'),
    stackgroup='one',
    groupnorm='percent'
)
trace1 = dict(
    x=['Winter', 'Spring', 'Summer', 'Fall'],
    y=['50', '70', '40', '60'],
    mode='lines',
    line=dict(width=0.5,
              color='rgb(111, 231, 219)'),
    stackgroup='one'
)
trace2 = dict(
    x=['Winter', 'Spring', 'Summer', 'Fall'],
    y=['70', '80', '60', '70'],
    mode='lines',
    line=dict(width=0.5,
              color='rgb(127, 166, 238)'),
    stackgroup='one'
)
trace3 = dict(
    x=['Winter', 'Spring', 'Summer', 'Fall'],
    y=['100', '100', '100', '100'],
    mode='lines',
    line=dict(width=0.5,
              color='rgb(131, 90, 241)'),
    stackgroup='one'
)
data = [trace0, trace1, trace2, trace3]
layout = go.Layout(
    showlegend=True,
    xaxis=dict(
        type='category',
    ),
    yaxis=dict(
        type='linear',
        range=[1, 100],
        dtick=20,
        ticksuffix='%'
    )
)
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='stacked-area-plot-norm', validate=False)
```

#### Select Hover Points

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[0,0.5,1,1.5,2],
    y=[0,1,2,1,0],
    fill= 'toself',
    fillcolor = '#ab63fa',
    hoveron = 'points+fills',
    line = dict(
      color = '#ab63fa'
    ),
    text = "Points + Fills",
    hoverinfo = 'text'
)

trace1 = go.Scatter(
    x=[3,3.5,4,4.5,5],
    y=[0,1,2,1,0],
    fill='toself',
    fillcolor = '#e763fa',
    hoveron = 'points',
    line = dict(
      color = '#e763fa'
    ),
    text = "Points only",
    hoverinfo = 'text'
)

data = [trace0, trace1]

layout = go.Layout(
    title = "hover on <i>points</i> or <i>fill</i>",
    xaxis = dict(
      range = [0,5.2]
    ),
    yaxis = dict(
      range = [0,3]
    )
)

fig = go.Figure(data=data,layout=layout)
py.iplot(data, filename='select-hover-points')
```

#### Reference
See https://plot.ly/python/reference/#scatter-line
and https://plot.ly/python/reference/#scatter-fill 
for more information and attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'area.ipynb', 'python/filled-area-plots/', 'Filled Area Plots | plotly',
    'How to make filled area plots in Python with Plotly.',
    title = 'Filled Area Plots | plotly',
    name = 'Filled Area Plots',
    thumbnail='thumbnail/area.jpg', language='python',
    has_thumbnail='true', display_as='basic', order=3.5,
    ipynb='~notebook_demo/8')
```

```python

```