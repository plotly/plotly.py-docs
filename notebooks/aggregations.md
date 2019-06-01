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
    description: How to use aggregates in Python with Plotly.
    display_as: transforms
    has_thumbnail: true
    ipynb: ~notebook_demo/192
    language: python
    layout: user-guide
    name: Aggregations
    order: 3
    page_type: example_index
    permalink: python/aggregations/
    thumbnail: thumbnail/aggregations.jpg
    title: Aggregations | Plotly
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

#### Introduction


Aggregates are a type of transform that can be applied to values in a given expression. Available aggregations are:

Function | Description
------------- | -------------
`count` | Returns the quantity of items for each group.
`sum` | Returns the summation of all numeric values.
`avg` | Returns the average of all numeric values.
`median` | Returns the median of all numeric values.
`mode` | Returns the mode of all numeric values.
`rms` | Returns the rms of all numeric values.
`stddev` | Returns the standard deviation of all numeric values.
`min` | Returns the minimum numeric value for each group.
`max` | Returns the maximum numeric value for each group.
`first` | Returns the first numeric value for each group.
`last` | Returns the last numeric value for each group.


#### Basic Example

```python
import plotly.offline as off

off.init_notebook_mode(connected=False)

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly']
score = [1,6,2,8,2,9,4,5,1,5,2,8]

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = subject,
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True),
    ]
  )]
)]


off.iplot({'data': data}, validate=False)
```

#### Aggregate Functions

```python
import plotly.offline as off

off.init_notebook_mode(connected=False)

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly']
score = [1,6,2,8,2,9,4,5,1,5,2,8]

aggs = ["count","sum","avg","median","mode","rms","stddev","min","max","first","last"]

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)


data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = subject,
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True)
    ]
  )]
)]

layout = dict(
  title = '<b>Plotly Aggregations</b><br>use dropdown to change aggregation',
  xaxis = dict(title = 'Subject'),
  yaxis = dict(title = 'Score', range = [0,22]),
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func
  )]
)

off.iplot({'data': data,'layout': layout}, validate=False)
```

#### Histogram Binning

```python
import plotly.offline as off

import pandas as pd

off.init_notebook_mode(connected=False)

df = pd.read_csv("https://plot.ly/~public.health/17.csv")

data = [dict(
  x = df['date'],
  autobinx = False,
  autobiny = True,
  marker = dict(color = 'rgb(68, 68, 68)'),
  name = 'date',
  type = 'histogram',
  xbins = dict(
    end = '2016-12-31 12:00',
    size = 'M1',
    start = '1983-12-31 12:00'
  )
)]

layout = dict(
  paper_bgcolor = 'rgb(240, 240, 240)',
  plot_bgcolor = 'rgb(240, 240, 240)',
  title = '<b>Shooting Incidents</b>',
  xaxis = dict(
    title = '',
    type = 'date'
  ),
  yaxis = dict(
    title = 'Shootings Incidents',
    type = 'linear'
  ),
  updatemenus = [dict(
        x = 0.1,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = True,
        buttons = [
        dict(
            args = ['xbins.size', 'D1'],
            label = 'Day',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M1'],
            label = 'Month',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M3'],
            label = 'Quater',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M6'],
            label = 'Half Year',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M12'],
            label = 'Year',
            method = 'restyle',
        )]
  )]
)

off.iplot({'data': data,'layout': layout}, validate=False)
```

#### Mapping with Aggregates 

```python
import plotly.offline as off

import pandas as pd

off.init_notebook_mode(connected=False)

df = pd.read_csv("https://raw.githubusercontent.com/bcdunbar/datasets/master/worldhappiness.csv")

aggs = ["count","sum","avg","median","mode","rms","stddev","min","max","first","last"]

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)

data = [dict(
  type = 'choropleth',
  locationmode = 'country names',
  locations = df['Country'],
  z = df['HappinessScore'],
  autocolorscale = False,
  colorscale = 'Portland',
  reversescale = True,
  transforms = [dict(
    type = 'aggregate',
    groups = df['Country'],
    aggregations = [dict(
        target = 'z', func = 'sum', enabled = True)
    ]
  )]
)]

layout = dict(
  title = '<b>Plotly Aggregations</b><br>use dropdown to change aggregation',
  xaxis = dict(title = 'Subject'),
  yaxis = dict(title = 'Score', range = [0,22]),
  height = 600,
  width = 900,
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func
  )]
)

off.iplot({'data': data,'layout': layout}, validate=False)
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
    'aggregations.ipynb', 'python/aggregations/', 'Aggregations',
    'How to use aggregates in Python with Plotly.',
    title = 'Aggregations | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/aggregations.jpg', 
    language='python', uses_plotly_offline=True,
    page_type='example_index',
    display_as='transforms', order=3,
    ipynb= '~notebook_demo/192')
```

```python

```