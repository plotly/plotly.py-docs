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
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to use multiple transforms (filter, group by, and aggregates)
      in Python with Plotly.
    display_as: transforms
    has_thumbnail: true
    ipynb: ~notebook_demo/193
    language: python
    layout: user-guide
    name: Multiple Transforms
    order: 4
    page_type: example_index
    permalink: python/multiple-transforms/
    thumbnail: thumbnail/multiple-transforms.jpg
    title: Multiple Transforms | Plotly
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

#### Filter and Group By

```python
import plotly.offline as off

import pandas as pd

off.init_notebook_mode(connected=False)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

colors = ['blue', 'orange', 'green', 'red', 'purple']

opt = []
opts = []
for i in range(0, len(colors)):
    opt = dict(
        target = df['continent'][[i]].unique(), value = dict(marker = dict(color = colors[i]))
    )
    opts.append(opt)

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'groupby',
        groups = df['continent'],
        styles = opts
    )]
)]

layout = dict(
    yaxis = dict(
        type = 'log'
    )
)


off.iplot({'data': data, 'layout': layout}, validate=False)
```

#### Filter and Aggregate

```python
import plotly.offline as off

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'aggregate',
        groups = df['continent'],
        aggregations = [
            dict(target = 'x', func = 'avg'),
            dict(target = 'y', func = 'avg'),
            dict(target = 'marker.size', func = 'sum')
        ]
      )]
)]

layout = dict(
    yaxis = dict(
        type = 'log'
    )
)


off.iplot({'data': data, 'layout': layout}, validate=False)
```

#### All Transforms

```python
import plotly.offline as off

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

colors = ['blue', 'orange', 'green', 'red', 'purple']

opt = []
opts = []
for i in range(0, len(colors)):
    opt = dict(
        target = df['continent'][[i]].unique(), value = dict(marker = dict(color = colors[i]))
    )
    opts.append(opt)

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'groupby',
        groups = df['continent'],
        styles = opts
      ),
      dict(
        type = 'aggregate',
        groups = df['continent'],
        aggregations = [
            dict(target = 'x', func = 'avg'),
            dict(target = 'y', func = 'avg'),
            dict(target = 'marker.size', func = 'sum')
        ]
      )]
)]

layout = dict(
    title = '<b>Gapminder</b><br>2007 Average GDP Per Cap & Life Exp. by Continent',
    yaxis = dict(
        type = 'log'
    )
)


off.iplot({'data': data, 'layout': layout}, validate=False)
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
    'multiple-transforms.ipynb', 'python/multiple-transforms/', 'Multiple Transforms',
    'How to use multiple transforms (filter, group by, and aggregates) in Python with Plotly.',
    title = 'Multiple Transforms | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/multiple-transforms.jpg',
    language='python', uses_plotly_offline=True,
    page_type='example_index',
    display_as='transforms', order=4,
    ipynb= '~notebook_demo/193')
```

```python

```
