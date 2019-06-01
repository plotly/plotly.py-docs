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
    description: How to manipulate the graph size in Python with Plotly.
    display_as: layout_opt
    has_thumbnail: true
    ipynb: ~notebook_demo/133
    language: python
    layout: user-guide
    name: Setting Graph Size
    page_type: example_index
    permalink: python/setting-graph-size/
    thumbnail: thumbnail/sizing.jpg
    title: Setting Graph Size
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



#### Version Check
Note: graph size attributes are available in version <b>1.9.2+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

### Adjusting Height, Width, & Margins###

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    )
]
layout = go.Layout(
    autosize=False,
    width=500,
    height=500,
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor='#7f7f7f',
    plot_bgcolor='#c7c7c7'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='size-margins')
```

### Automatically Adjust Margins


Set [automargin](https://plot.ly/python/reference/#layout-xaxis-automargin) to `True` and Plotly will automatically increase the margin size to prevent ticklabels from being cut off or overlapping with axis titles.

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Bar(
        x=['Apples', 'Oranges', 'Watermelon', 'Pears'],
        y=[3, 2, 1, 4]
    )
]
layout = go.Layout(
    autosize=False,
    width=500,
    height=500,
    yaxis=go.layout.YAxis(
        title='Y-axis Title',
        ticktext=['Very long label','long label','3','label'],
        tickvals=[1, 2, 3, 4],
        tickmode='array',
        automargin=True,
        titlefont=dict(size=30),
    ),
    paper_bgcolor='#7f7f7f',
    plot_bgcolor='#c7c7c7'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='automargin')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-graphsizeplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-graphsizeplot/", width="100%", height="650px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-graphsizeplot/code", width="100%", height=500, frameBorder="0")
```

#### Reference
See https://plot.ly/python/reference/#layout for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'sizing.ipynb', 'python/setting-graph-size/', 'Setting Graph Size',
    'How to manipulate the graph size in Python with Plotly.',
    title = 'Setting Graph Size',
    name = 'Setting Graph Size',
    has_thumbnail='true', thumbnail='thumbnail/sizing.jpg', 
    language='python', page_type='example_index',
    display_as='layout_opt',
    ipynb= '~notebook_demo/133')
```