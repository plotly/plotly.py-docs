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
    description: How to make a graph with multiple axes in python.
    display_as: multiple_axes
    has_thumbnail: true
    ipynb: ~notebook_demo/270
    language: python
    layout: user-guide
    name: Multiple Axes
    order: 1
    page_type: example_index
    permalink: python/multiple-axes/
    thumbnail: thumbnail/multiple-axes.jpg
    title: Python Mulitple Axes | Examples | Plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Two Y Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis data'
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[4, 5, 6],
    name='yaxis2 data',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    title='Double Y Axis Example',
    yaxis=dict(
        title='yaxis title'
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='multiple-axes-double')
```

#### Multiple Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    name='yaxis1 data'
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[40, 50, 60],
    name='yaxis2 data',
    yaxis='y2'
)
trace3 = go.Scatter(
    x=[4, 5, 6],
    y=[40000, 50000, 60000],
    name='yaxis3 data',
    yaxis='y3'
)
trace4 = go.Scatter(
    x=[5, 6, 7],
    y=[400000, 500000, 600000],
    name='yaxis4 data',
    yaxis='y4'
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    title='multiple y-axes example',
    width=800,
    xaxis=dict(
        domain=[0.3, 0.7]
    ),
    yaxis=dict(
        title='yaxis title',
        titlefont=dict(
            color='#1f77b4'
        ),
        tickfont=dict(
            color='#1f77b4'
        )
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='#ff7f0e'
        ),
        tickfont=dict(
            color='#ff7f0e'
        ),
        anchor='free',
        overlaying='y',
        side='left',
        position=0.15
    ),
    yaxis3=dict(
        title='yaxis4 title',
        titlefont=dict(
            color='#d62728'
        ),
        tickfont=dict(
            color='#d62728'
        ),
        anchor='x',
        overlaying='y',
        side='right'
    ),
    yaxis4=dict(
        title='yaxis5 title',
        titlefont=dict(
            color='#9467bd'
        ),
        tickfont=dict(
            color='#9467bd'
        ),
        anchor='free',
        overlaying='y',
        side='right',
        position=0.85
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='multiple-axes-multiple')
```

#### Muliple Y-Axes Subplots

```python
import plotly.plotly as py
import plotly.graph_objs as go

# Top left
trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 32, 62],
    name='yaxis data',
)
trace2 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis2 data',
    yaxis='y2'
)

# Top right
trace3 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 32, 62],
    name='yaxis3 data',
    xaxis='x2',
    yaxis='y3'
)
trace4 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis4 data',
    xaxis='x2',
    yaxis='y4'
)

# Bottom left
trace5 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 32, 62],
    name='yaxis5 data',
    xaxis='x3',
    yaxis='y5'
)
trace6 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis6 data',
    xaxis='x3',
    yaxis='y6'
)

# Bottom right
trace7 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 32, 62],
    name='yaxis7 data',
    xaxis='x4',
    yaxis='y7'
)
trace8 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis8 data',
    xaxis='x4',
    yaxis='y8'
)


data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
layout = go.Layout(
    title='Double Y Axis Example',
    legend={'x': 1.1},
    width=1000,
    height=500,
    # Top left
    xaxis=dict(
        title='xaxis title',
        domain=[0, 0.4]
    ),
    yaxis=dict(
        title='yaxis title',
        type='log',
        domain=[0.6, 1.0],
        anchor='x'
    ),
    yaxis2=dict(
        title='yaxis2 title',
        overlaying='y',
        side='right'
    ),
    
    # Top right
    xaxis2=dict(
        title='xaxis2 title',
        domain=[0.6, 1.0],
        anchor='y3'
    ),
    yaxis3=dict(
        type='log',
        title='yaxis3 title',
        domain=[0.6, 1.0],
        anchor='x2'
    ),
    yaxis4=dict(
        title='yaxis4 title',
        domain=[0.6, 1.0],
        overlaying='y3',
        side='right',
        anchor='x2'
    ),
    
    # Bottom left
    xaxis3=dict(
        title='xaxis3 title',
        domain=[0, 0.4],
        anchor='y5'
    ),
    yaxis5=dict(
        type='log',
        title='yaxis5 title',
        domain=[0, 0.4],
        anchor='x3'
    ),
    yaxis6=dict(
        title='yaxis6 title',
        domain=[0, 0.4],
        overlaying='y5',
        side='right',
        anchor='x3'
    ),
    
    # Bottom right
    xaxis4=dict(
        title='xaxis4, title',
        domain=[0.6, 1.0],
        anchor='y7'
    ),
    yaxis7=dict(
        type='log',
        title='yaxis7 title',
        domain=[0, 0.4],
        anchor='x4'
    ),
    yaxis8=dict(
        title='yaxis8 title',
        domain=[0, 0.4],
        overlaying='y7',
        side='right',
        anchor='x4'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='multiple-y-axes-subplots')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-multipleaxesplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-multipleaxesplot/", width="100%", height="650px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-multipleaxesplot/code", width="100%", height=500, frameBorder="0")
```

#### Reference
All of the y-axis properties are found here: https://plot.ly/python/reference/#YAxis

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'multiple-axes.ipynb', 'python/multiple-axes/', 'Multiple Axes | Plotly',
    'How to make a graph with multiple axes in python.',
    title = 'Python Mulitple Axes | Examples | Plotly',
    name = 'Multiple Axes', has_thumbnail='true', thumbnail='thumbnail/multiple-axes.jpg', 
    language='python', page_type='example_index',
    display_as='multiple_axes', order=1,
    ipynb='~notebook_demo/270')

```