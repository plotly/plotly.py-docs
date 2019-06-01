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
    description: How to make Histograms in Python with Plotly.
    display_as: statistical
    has_thumbnail: true
    ipynb: ~notebook_demo/22
    language: python
    layout: user-guide
    name: Histograms
    order: 4
    page_type: example_index
    permalink: python/histograms/
    redirect_from: /python/histogram-tutorial/
    thumbnail: thumbnail/histogram.jpg
    title: Python Histograms | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



#### Version Check
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

### Basic Histogram ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(500)
data = [go.Histogram(x=x)]

py.iplot(data, filename='basic histogram')
```

### Normalized Histogram

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(500)
data = [go.Histogram(x=x,
                     histnorm='probability')]

py.iplot(data, filename='normalized histogram')
```

### Horizontal Histogram ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

y = np.random.randn(500)
data = [go.Histogram(y=y)]

py.iplot(data, filename='horizontal histogram')
```

### Overlaid Histogram ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x0 = np.random.randn(500)
x1 = np.random.randn(500)+1

trace1 = go.Histogram(
    x=x0,
    opacity=0.75
)
trace2 = go.Histogram(
    x=x1,
    opacity=0.75
)

data = [trace1, trace2]
layout = go.Layout(barmode='overlay')
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='overlaid histogram')
```

### Stacked Histograms 

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x0 = np.random.randn(500)
x1 = np.random.randn(500)

trace0 = go.Histogram(
    x=x0
)
trace1 = go.Histogram(
    x=x1
)
data = [trace0, trace1]
layout = go.Layout(barmode='stack')
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='stacked histogram')
```

### Styled Histogram

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
x0 = np.random.randn(500)
x1 = np.random.randn(500)+1

trace1 = go.Histogram(
    x=x0,
    histnorm='percent',
    name='control',
    xbins=dict(
        start=-4.0,
        end=3.0,
        size=0.5
    ),
    marker=dict(
        color='#FFD7E9',
    ),
    opacity=0.75
)
trace2 = go.Histogram(
    x=x1,
    name='experimental',
    xbins=dict(
        start=-3.0,
        end=4,
        size=0.5
    ),
    marker=dict(
        color='#EB89B5'
    ),
    opacity=0.75
)
data = [trace1, trace2]

layout = go.Layout(
    title='Sampled Results',
    xaxis=dict(
        title='Value'
    ),
    yaxis=dict(
        title='Count'
    ),
    bargap=0.2,
    bargroupgap=0.1
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='styled histogram')
```

### Cumulative Histogram 

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(500)
data = [go.Histogram(x=x,
                     cumulative=dict(enabled=True))]

py.iplot(data, filename='cumulative histogram')
```

### Specify Binning Function

```python
import plotly.plotly as py
import plotly.graph_objs as go

x = ["Apples","Apples","Apples","Oranges", "Bananas"]
y = ["5","10","3","10","5"]

data = [
  go.Histogram(
    histfunc = "count",
    y = y,
    x = x,
    name = "count"
  ),
  go.Histogram(
    histfunc = "sum",
    y = y,
    x = x,
    name = "sum"
  )
]

py.iplot(data, filename='binning function')
```

### Custom Binning
For custom binning along x-axis, use the attribute [`nbinsx`](https://plot.ly/python/reference/#histogram-nbinsx). Please note that the autobin algorithm will choose a 'nice' round bin size that may result in somewhat fewer than `nbinsx` total bins. Alternatively, you can set the exact values for [`xbins`](https://plot.ly/python/reference/#histogram-xbins) along with `autobinx = False`.

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

x = ['1970-01-01', '1970-01-01', '1970-02-01', '1970-04-01', '1970-01-02', '1972-01-31', '1970-02-13', '1971-04-19']


trace0 = go.Histogram(
    x=x,
    nbinsx = 4,         
  )
trace1 = go.Histogram(
    x=x,
    nbinsx = 8,   
  )
trace2 = go.Histogram(
    x=x,
    nbinsx = 10,     
  )
trace3 = go.Histogram(
    x=x,
    xbins=dict(
        start='1969-11-15',
        end='1972-03-31',
        size= 'M18'),
    autobinx = False
)
trace4 = go.Histogram(
    x=x,
    xbins=dict(
        start='1969-11-15',
        end='1972-03-31',
        size= 'M4'),
    autobinx = False
)
trace5 = go.Histogram(
    x=x,
    xbins=dict(
        start='1969-11-15',
        end='1972-03-31',
        size= 'M2'),
    autobinx = False
)
  
fig = tools.make_subplots(rows=3, cols=2)
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 2)
fig.append_trace(trace4, 3, 1)
fig.append_trace(trace5, 3, 2)

py.iplot(fig, filename='custom binning')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-histogramplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-histogramplot/", width="100%", height="650px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-histogramplot/code", width="100%", height=500, frameBorder="0")

```

#### Reference
See https://plot.ly/python/reference/#histogram for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/csshref="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'histograms.ipynb', 'python/histograms/', 'Python Histograms | plotly',
    'How to make Histograms in Python with Plotly.',
    title = 'Python Histograms | plotly',
    name = 'Histograms',
    has_thumbnail='true', thumbnail='thumbnail/histogram.jpg', 
    language='python', page_type='example_index',
    display_as='statistical', order=4, redirect_from='/python/histogram-tutorial/',
    ipynb= '~notebook_demo/22')  

```

```python

```