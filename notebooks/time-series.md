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
    description: How to plot date and time in python.
    display_as: financial
    has_thumbnail: true
    ipynb: ~notebook_demo/213
    language: python
    layout: user-guide
    name: Time Series
    order: 0
    page_type: example_index
    permalink: python/time-series/
    thumbnail: thumbnail/time-series.jpg
    title: Time Series Plots | plotly
---

### Time Series Plot with `datetime` Objects ###

Time series can be represented using either `plotly_express` functions (`px.line`, `px.scatter`) or `plotly.graph_objs` charts objects (`go.Scatter`). For more examples of such charts, see the documentation of [line and scatter plots](https://plot.ly/python/line-and-scatter/).

```python
# Using plotly_express
import plotly_express as px

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High')
fig.show()
```

```python
# Using graph_objs
import plotly.graph_objs as go

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
fig.show()
```

### Time Series Plot with Custom Date Range 

The data range can be set manually using either `datetime.datetime` objects, or date strings.

```python
import plotly.graph_objs as go
import datetime

x = [datetime.datetime(year=2013, month=10, day=4),
     datetime.datetime(year=2013, month=11, day=5),
     datetime.datetime(year=2013, month=12, day=6)]
data = [go.Scatter(x=x, y=[1, 3, 6])]

fig = go.Figure(data=data)
# Use datetime objects to set xaxis range
fig.update(layout_xaxis_range=[datetime.datetime(2013, 10, 17),
                               datetime.datetime(2013, 11, 20)])
```

```python
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

trace_high = go.Scatter(
                x=df.Date,
                y=df['AAPL.High'],
                name="AAPL High",
                line_color='deepskyblue',
                opacity=0.8)

trace_low = go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name="AAPL Low",
                line_color='dimgray',
                opacity=0.8)

fig = go.Figure(data=[trace_high, trace_low])
# Use date string to set xaxis range
fig.update(layout_xaxis_range=['2016-07-01','2016-12-31'],
           layout_title_text="Manually Set Date Range")
fig.show()
```

### Time Series With Rangeslider

```python
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

trace_high = go.Scatter(
    x=df.Date,
    y=df['AAPL.High'],
    name="AAPL High",
    line_color='deepskyblue')

trace_low = go.Scatter(
    x=df.Date,
    y=df['AAPL.Low'],
    name="AAPL Low",
    line_color='dimgray')

fig = go.Figure(data=[trace_high, trace_low])
fig.update(layout_title_text='Time Series with Rangeslider', 
           layout_xaxis_rangeslider_visible=True)
fig.show()
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-timeseriesplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-timeseriesplot/", width="100%", height="750px", frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-timeseriesplot/code", width="100%", height=500, frameBorder="0")
```

#### Reference
See https://plot.ly/python/reference/#layout-xaxis-rangeslider and<br> https://plot.ly/python/reference/#layout-xaxis-rangeselector for more information and chart attribute options!

