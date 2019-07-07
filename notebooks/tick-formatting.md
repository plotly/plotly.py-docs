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
    description: How to format axes ticks in Python with Plotly.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/1
    language: python
    layout: user-guide
    name: Formatting Ticks
    order: 10
    permalink: python/tick-formatting/
    thumbnail: thumbnail/tick-formatting.gif
    title: Formatting Ticks | Plotly
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

#### Tickmode - Linear


If `"linear"`, the placement of the ticks is determined by a starting position `tick0` and a tick step `dtick`

```python
import plotly.plotly as py
import plotly.graph_objs as go

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]

trace0 = go.Scatter(
    x = x,
    y = y
)

data = [trace0]

layout = go.Layout(
    xaxis = go.layout.XAxis(
        tickmode = 'linear',
        tick0 = 0.5,
        dtick = 0.75
    )
)

fig = go.Figure(
    data = data,
    layout = layout
)

py.iplot(fig, filename='tickformatting-tickmode-linear')
```

#### Tickmode - Array


If `"array"`, the placement of the ticks is set via `tickvals` and the tick text is `ticktext`.

```python
import plotly.plotly as py
import plotly.graph_objs as go

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]

trace0 = go.Scatter(
    x = x,
    y = y
)

data = [trace0]

layout = go.Layout(
    xaxis = go.layout.XAxis(
        tickmode = 'array',
        tickvals = [1, 3, 5, 7, 9, 11],
        ticktext = ['One', 'Three', 'Five', 'Seven', 'Nine', 'Eleven']
    )
)

fig = go.Figure(
    data = data,
    layout = layout
)

py.iplot(fig, filename='tickformatting-tickmode-array')
```

#### Using Tickformat Attribute


For more formatting types, see: https://github.com/d3/d3-format/blob/master/README.md#locale_format

```python
import plotly.plotly as py
import plotly.graph_objs as go

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [0.18, 0.38, 0.56, 0.46, 0.59, 0.4, 0.78, 0.77, 0.74, 0.42, 0.45, 0.39]

trace0 = go.Scatter(
    x = x,
    y = y
)

data = [trace0]

layout = go.Layout(
    yaxis = go.layout.YAxis(
        tickformat = '%'
    )
)

fig = go.Figure(
    data = data,
    layout = layout
)

py.iplot(fig, filename='using-tickformat-attribute')
```

#### Using Tickformat Atttribute - Date/Time


For more date/time formatting types, see: https://github.com/d3/d3-time-format/blob/master/README.md

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace0 = go.Scatter(
    mode = 'lines',
    name = 'AAPL High',
    x = df['Date'],
    y = df['AAPL.High'],
    line = go.scatter.Line(
        color = '#17BECF'
    )
)

trace1 = go.Scatter(
    mode = 'lines',
    name = 'AAPL Low',
    x = df['Date'],
    y = df['AAPL.Low'],
    line = go.scatter.Line(
        color = '#7F7F7F'
    )
)

data = [trace0, trace1]

layout = go.Layout(
    title = 'Time Series with Custom Date-Time Format',
    xaxis = go.layout.XAxis(
        tickformat = '%d %B (%a)<br>%Y'
    )
)

fig = go.Figure(
    data=data,
    layout=layout
)

py.iplot(fig, filename='using-tickformat-attribute-date')
```

#### Using Exponentformat Attribute

```python
import plotly.plotly as py
import plotly.graph_objs as go

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [68000, 52000, 60000, 20000, 95000, 40000, 60000, 79000, 74000, 42000, 20000, 90000]

trace0 = go.Scatter(
    x = x,
    y = y
)

data = [trace0]

layout = go.Layout(
    yaxis = go.layout.YAxis(
        showexponent = 'all',
        exponentformat = 'e'
    )
)

fig = go.Figure(
    data = data,
    layout = layout
)

py.iplot(fig, filename='using-exponentformat')
```

#### Tickformatstops to customize for different zoom levels

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace0 = go.Scatter(
    x = df['Date'],
    y = df['mavg']
)

data = [trace0]

layout = go.Layout(
    xaxis = go.layout.XAxis(
        tickformatstops = [
            go.layout.xaxis.Tickformatstop(
                dtickrange=[None, 1000],
                value="%H:%M:%S.%L ms"
              ),
            go.layout.xaxis.Tickformatstop(
                dtickrange=[1000, 60000],
                value="%H:%M:%S s"
              ),
            go.layout.xaxis.Tickformatstop(
                dtickrange=[60000, 3600000],
                value="%H:%M m"
              ),
            go.layout.xaxis.Tickformatstop(
                dtickrange=[3600000, 86400000],
                value="%H:%M h"
              ),
            go.layout.xaxis.Tickformatstop(
                dtickrange=[86400000, 604800000],
                value="%e. %b d"
              ),
            go.layout.xaxis.Tickformatstop(
                dtickrange=[604800000, "M1"],
                value="%e. %b w"
              ),
            go.layout.xaxis.Tickformatstop(
                dtickrange=["M1", "M12"],
                value="%b '%y M"
              ),
            go.layout.xaxis.Tickformatstop(
                dtickrange=["M12", None],
                value="%Y Y"
              )
        ]
    )
)

fig = go.Figure(
    data = data,
    layout = layout
)

py.iplot(fig, filename='tickformatstops')
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
    'tick-formatting.ipynb', 'python/tick-formatting/', 'Formatting Ticks',
    'How to format axes ticks in Python with Plotly.',
    title = 'Formatting Ticks | Plotly',
    has_thumbnail='false',
    language='python',
    page_type='example_index',
    display_as='layout_opt',
    ipynb='~notebook_demo/1')
```

```python

```