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
    description: How to make waterfall plots in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: /~notebook_demo/276
    language: python
    layout: user-guide
    name: Waterfall Charts
    order: 6.2
    page_type: u-guide
    permalink: python/waterfall-charts/
    thumbnail: thumbnail/waterfall-charts.jpg
    title: Python Waterfall Chart | Plotly
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

### Simple Waterfall Chart

```python
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected = False)

trace = go.Waterfall(
    name = "20", orientation = "v",
    measure = ["relative", "relative", "total", "relative", "relative", "total"],
    x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
    textposition = "outside",
    text = ["+60", "+80", "", "-40", "-20", "Total"],
    y = [60, 80, 0, -40, -20, 0],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
)

layout = go.Layout(
        title = "Profit and loss statement 2018",
        showlegend = True
)

py.iplot(go.Figure([trace], layout), filename = "basic_waterfall_chart")


```

### Multi Category Waterfall Chart
This example uses the [waterfallgroupgap attribute](https://plot.ly/python/reference/#layout-waterfallgroupgap), which sets a gap between bars.

```python
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected = False)

trace1 = go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
        ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [1, 2, 3, -1, None, 1, 2, -4, None],
    base = 1000
)
trace2 = go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
        ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [1.1, 2.2, 3.3, -1.1, None, 1.1, 2.2, -4.4, None],
    base = 1000
)

layout = go.Layout(
    waterfallgroupgap = 0.5,
    xaxis = {"title":"MULTI-CATEGORY","tickfont":{"size":16},"ticks":"outside"}
)

data = [trace1,trace2]
fig = go.Figure(data, layout)
py.iplot(fig,filename = "mutli_category_waterfall")
```

### Setting Marker Size and Color
This example uses [decreasing, increasing, and total](https://plot.ly/python/reference/#waterfall-increasing) attributes to customize the bars.

```python
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected = False)

trace = go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
       ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [10, 20, 30, -10, None, 10, 20, -40, None], base = 300,
    decreasing = {"marker":{"color":"Maroon", "line":{"color":"red", "width":2}}},
    increasing = {"marker":{"color":"Teal"}},
    totals = {"marker":{"color":"deep sky blue", "line":{"color":'blue', "width":3}}}
)

layout = go.Layout(
    title = "Profit and loss statement",
    waterfallgap = 0.3,
    xaxis = {"title":"", "tickfont":{"size":15}, "ticks":"outside"}
)

py.iplot(go.Figure([trace], layout), filename = "Style_waterfall")


```

### Horizontal Waterfall Chart

```python
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected = False)

trace = go.Waterfall(
    name = "2018", orientation = "h", measure = ["relative", "relative", "relative", "relative", "total", "relative",
                                              "relative", "relative", "relative", "total", "relative", "relative", "total", "relative", "total"],
    y = ["Sales", "Consulting", "Maintenance", "Other revenue", "Net revenue", "Purchases", "Material expenses",
       "Personnel expenses", "Other expenses", "Operating profit", "Investment income", "Financial income",
       "Profit before tax", "Income tax (15%)", "Profit after tax"],
    x = [375, 128, 78, 27, None, -327, -12, -78, -12, None, 32, 89, None, -45, None],
    connector = {"mode":"between", "line":{"width":4, "color":"rgb(0, 0, 0)", "dash":"solid"}}
)

layout = go.Layout(
    title = "Profit and loss statement 2018<br>waterfall chart displaying positive and negative",
        yaxis = {"type":"category", "autorange":"reversed"},
        xaxis = {"type":"linear"},
        margin = {"l":150},
        showlegend = True
)

py.iplot(go.Figure([trace], layout), filename = "horizontal_waterfall")

```

#### Reference
See https://plot.ly/python/reference/#waterfall for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href= "//fonts.googleapis.com/css?family= Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel= "stylesheet" type= "text/css" />'))
display(HTML('<link rel= "stylesheet" type= "text/css" href= "http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'waterfall-charts.ipynb', 'python/waterfall-charts/', 'Waterfall Charts',
    'How to make waterfall plots in Python with Plotly.',
    title= 'Python Waterfall Chart | Plotly',
    has_thumbnail= 'true', thumbnail= 'thumbnail/waterfall-charts.jpg',
    language= 'python',
    # page_type= 'example_index', // note this is only if you want the tutorial to appear on the main page: plot.ly/python
    display_as= 'basic', order= 6.2, ipynb= '/~notebook_demo/276',uses_plotly_offline= True)
```

```python

```
