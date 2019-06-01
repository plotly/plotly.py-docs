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
    description: How to use hover text and formatting in Python with Plotly.
    display_as: layout_opt
    has_thumbnail: false
    ipynb: ~notebook_demo/198
    language: python
    layout: user-guide
    name: Hover Text and Formatting
    order: 20
    page_type: example_index
    permalink: python/hover-text-and-formatting/
    thumbnail: thumbnail/hover-text.jpg
    title: Hover Text and Formatting | Plotly
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

#### Add Hover Text

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x = [1,2,3,4,5],
        y = [2,1,6,4,4],
        text = ["Text A", "Text B", "Text C", "Text D", "Text E"],
        hoverinfo = 'text',
        marker = dict(
            color = 'green'
        ),
        showlegend = False
    )
]

py.iplot(data, filename = "add-hover-text")
```

#### Format Hover Text

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x = [1,2,3,4,5],
        y = [2.02825,1.63728,6.83839,4.8485,4.73463],
        hoverinfo = 'y',
        marker = dict(
            color = 'green'
        ),
        showlegend = False
    )
]

layout = go.Layout(
    title = "Set hover text formatting<br><a href= https://github.com/d3/d3-time-format/blob/master/README.md#locale_format>https://github.com/d3/d3-time-format/blob/master/README.md#locale_format</a>",
    titlefont = dict(
        size = 10
    ),
    xaxis = dict(
        zeroline = False
    ),
    yaxis = dict(
        hoverformat = '.2f'
    )
)

fig = go.Figure(data=data,layout=layout)
py.iplot(fig, filename = "format-hover-text")
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-hoverplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-hoverplot/", width="100%", height="920px", frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-hoverplot/code", width="100%", height=500, frameBorder="0")
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'hover-text-and-formatting.ipynb', 'python/hover-text-and-formatting/', 'Hover Text and Formatting',
    'How to use hover text and formatting in Python with Plotly.',
    title = 'Hover Text and Formatting | Plotly',
    has_thumbnail='false', thumbnail='thumbnail/hover-text.jpg', 
    language='python', 
    page_type='example_index',
    display_as='layout_opt', order=20, ipynb='~notebook_demo/198',
    uses_plotly_offline=False)
```