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

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



### Time Series Plot with `datetime` Objects ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

data = [go.Scatter(x=df.Date, y=df['AAPL.High'])]

py.iplot(data, filename = 'time-series-simple')
```

### Date Strings

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

data = [go.Scatter(
          x=df.Date,
          y=df['AAPL.Close'])]

py.iplot(data)
```

### Time Series Plot with Custom Date Range 

```python
import plotly.plotly as py
import plotly.graph_objs as go

import datetime

def to_unix_time(dt):
    epoch =  datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

x = [datetime.datetime(year=2013, month=10, day=04),
    datetime.datetime(year=2013, month=11, day=05),
    datetime.datetime(year=2013, month=12, day=06)]
data = [go.Scatter(
            x=x,
            y=[1, 3, 6])]

layout = go.Layout(xaxis = dict(
                   range = [to_unix_time(datetime.datetime(2013, 10, 17)),
                            to_unix_time(datetime.datetime(2013, 11, 20))]
    ))

fig = go.Figure(data = data, layout = layout)
py.iplot(fig)
```

### Manually Set Range

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

trace_high = go.Scatter(
                x=df.Date,
                y=df['AAPL.High'],
                name = "AAPL High",
                line = dict(color = '#17BECF'),
                opacity = 0.8)

trace_low = go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name = "AAPL Low",
                line = dict(color = '#7F7F7F'),
                opacity = 0.8)

data = [trace_high,trace_low]

layout = dict(
    title = "Manually Set Date Range",
    xaxis = dict(
        range = ['2016-07-01','2016-12-31'])
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename = "Manually Set Range")
```

### Time Series With Rangeslider

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

trace_high = go.Scatter(
    x=df.Date,
    y=df['AAPL.High'],
    name = "AAPL High",
    line = dict(color = '#17BECF'),
    opacity = 0.8)

trace_low = go.Scatter(
    x=df.Date,
    y=df['AAPL.Low'],
    name = "AAPL Low",
    line = dict(color = '#7F7F7F'),
    opacity = 0.8)

data = [trace_high,trace_low]

layout = dict(
    title='Time Series with Rangeslider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename = "Time Series with Rangeslider")
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

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'time-series.ipynb', 'python/time-series/', 'Python Time Series | Examples | Plotly',
    'How to plot date and time in python. ',
    title= 'Time Series Plots | plotly',
    name = 'Time Series',
    has_thumbnail='true', thumbnail='thumbnail/time-series.jpg', 
    language='python', page_type='example_index', 
    display_as='financial', order=0,
    ipynb='~notebook_demo/213')
```