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
    description: How to make 2D Histograms in Python with Plotly.
    display_as: statistical
    has_thumbnail: true
    ipynb: ~notebook_demo/24
    language: python
    layout: user-guide
    name: 2D Histograms
    order: 6
    page_type: u-guide
    permalink: python/2D-Histogram/
    thumbnail: thumbnail/histogram2d.jpg
    title: Python 2D Histograms | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



#### Version Check
Note: 2D Histograms are available in version <b>1.9.12+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

### 2D Histogram with Slider Control ###


Add slider controls to 2d histograms with the [postMessage API](https://github.com/plotly/postMessage-API).
                                                                                                                   See the [code on JSFiddle](https://jsfiddle.net/plotlygraphs/y9sdy76h/4/).
                                                                                                                  Watch [the 5 second video](https://raw.githubusercontent.com/plotly/documentation/gh-pages/all_static/images
/flight_conflicts.gif) of how it works.

```python
from IPython.core.display import display,HTML
display(HTML('<iframe height=600 width=950 src="https://jsfiddle.net/plotlygraphs/y9sdy76h/4/embedded/result,js,html/"></iframe>'))
```

### 2D Histogram of a Bivariate Normal Distribution ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(500)
y = np.random.randn(500)+1

data = [
    go.Histogram2d(
        x=x,
        y=y
    )
]
py.iplot(data)
```

### 2D Histogram Binning and Styling Options ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(500)
y = np.random.randn(500)+1

data = [
    go.Histogram2d(x=x, y=y, histnorm='probability',
        autobinx=False,
        xbins=dict(start=-3, end=3, size=0.1),
        autobiny=False,
        ybins=dict(start=-2.5, end=4, size=0.1),
        colorscale=[[0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'], [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'], [1, 'rgb(217,30,30)']]
    )
]
py.iplot(data)
```

### 2D Histogram Overlaid with a Scatter Chart ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x0 = np.random.randn(100)/5. + 0.5  # 5. enforces float division
y0 = np.random.randn(100)/5. + 0.5
x1 = np.random.rand(50)
y1 = np.random.rand(50) + 1.0

x = np.concatenate([x0, x1])
y = np.concatenate([y0, y1])

trace1 = go.Scatter(
    x=x0,
    y=y0,
    mode='markers',
    showlegend=False,
    marker=dict(
        symbol='x',
        opacity=0.7,
        color='white',
        size=8,
        line=dict(width=1),
    )
)
trace2 = go.Scatter(
    x=x1,
    y=y1,
    mode='markers',
    showlegend=False,
    marker=dict(
        symbol='circle',
        opacity=0.7,
        color='white',
        size=8,
        line=dict(width=1),
    )
)
trace3 = go.Histogram2d(
    x=x,
    y=y,
    colorscale='YlGnBu',
    zmax=10,
    nbinsx=14,
    nbinsy=14,
    zauto=False,
)

layout = go.Layout(
    xaxis=dict( ticks='', showgrid=False, zeroline=False, nticks=20 ),
    yaxis=dict( ticks='', showgrid=False, zeroline=False, nticks=20 ),
    autosize=False,
    height=550,
    width=550,
    hovermode='closest',

)
data = [trace1, trace2, trace3]
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)
```

#### Reference
See https://plot.ly/python/reference/#histogram2d for more information and chart attribute options!


```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/csshref="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    '2d-histograms.ipynb', 'python/2D-Histogram/', 'Python 2D Histograms | plotly',
    'How to make 2D Histograms in Python with Plotly.',
    title = 'Python 2D Histograms | plotly',
    name = '2D Histograms',
    has_thumbnail='true', thumbnail='thumbnail/histogram2d.jpg',
    language='python', display_as='statistical', order=6,
    ipynb= '~notebook_demo/24')
```

```python

```