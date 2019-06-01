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
    description: How to make 3D streamtube plots in Python with Plotly.
    display_as: 3d_charts
    has_thumbnail: true
    ipynb: ~notebook_demo/207
    language: python
    layout: user-guide
    name: 3D Streamtube Plots
    order: 21
    page_type: u-guide
    permalink: python/streamtube-plot/
    thumbnail: thumbnail/streamtube.jpg
    title: 3D Streamtube Plots | Plotly
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

### Introduction


In streamtube plots, attributes inlcude `x`, `y`, and `z`, which set the coorindates of the vector field, and `u`, `v`, and `w`, which sets the x, y, and z components of the vector field. Additionally, you can use `starts` to determine the streamtube's starting position. Lastly, `maxdisplayed` determines the maximum segments displayed in a streamtube.   


### Basic Streamtube Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/streamtube-basic.csv')

data = [go.Streamtube(
    x = df['x'],
    y = df['y'],
    z = df['z'],
    u = df['u'],
    v = df['v'],
    w = df['w'],
    sizeref = 0.5,
    colorscale = 'Blues', 
    cmin = 0,
    cmax = 3
    )
]

layout = go.Layout(
    scene = dict(
      camera = dict(
        eye = dict(
          x = -0.7243612458865182,
          y = 1.9269804254717962,
          z = 0.6704828299861716
        )
      )
    )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='streamtube-basic')
```

### Starting Position and Segments

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/streamtube-wind.csv').drop(['Unnamed: 0'],axis=1)

data = [go.Streamtube(
    x = df['x'],
    y = df['y'],
    z = df['z'],
    u = df['u'],
    v = df['v'],
    w = df['w'],
    starts = dict(
        x = [80] * 16,
        y = [20,30,40,50] * 4,
        z = [0,0,0,0,5,5,5,5,10,10,10,10,15,15,15,15]
    ),
    sizeref = 0.3,
    colorscale = 'Portland',
    showscale = False,
    maxdisplayed = 3000
)]

layout = go.Layout(
    scene = dict(
        aspectratio = dict(
            x = 2,
            y = 1,
            z = 0.3
        )
    ),
    margin = dict(
        t = 20,
        b = 20,
        l = 20,
        r = 20
    )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename="streamtube wind")
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
    'streamtube.ipynb', 'python/streamtube-plot/', '3D Streamtube Plots',
    'How to make 3D streamtube plots in Python with Plotly.',
    title = '3D Streamtube Plots | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/streamtube.jpg',
    language='python',
    display_as='3d_charts', order=21, ipynb='~notebook_demo/207',
    uses_plotly_offline=False)
```

```python

```