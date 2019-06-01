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
    description: How to add error-bars to charts in Python with Plotly.
    display_as: statistical
    has_thumbnail: true
    ipynb: ~notebook_demo/18
    language: python
    layout: user-guide
    name: Error Bars
    order: 1
    page_type: example_index
    permalink: python/error-bars/
    thumbnail: thumbnail/error-bar.jpg
    title: Error Bars | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Basic Symmetric Error Bars

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[0, 1, 2],
        y=[6, 10, 2],
        error_y=dict(
            type='data',
            array=[1, 2, 3],
            visible=True
        )
    )
]

py.iplot(data, filename='basic-error-bar')
```

#### Asymmetric Error Bars

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2, 3, 4],
        y=[2, 1, 3, 4],
        error_y=dict(
            type='data',
            symmetric=False,
            array=[0.1, 0.2, 0.1, 0.1],
            arrayminus=[0.2, 0.4, 1, 0.2]
        )
    )
]
py.iplot(data, filename='error-bar-asymmetric-array')
```

#### Error Bars as a Percentage of the y Value

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[0, 1, 2],
        y=[6, 10, 2],
        error_y=dict(
            type='percent',
            value=50,
            visible=True
        )
    )
]
py.iplot(data, filename='percent-error-bar')
```

#### Asymmetric Error Bars with a Constant Offset

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2, 3, 4],
        y=[2, 1, 3, 4],
        error_y=dict(
            type='percent',
            symmetric=False,
            value=15,
            valueminus=25
        )
    )
]
py.iplot(data, filename='error-bar-asymmetric-constant')
```

#### Horizontal Error Bars

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2, 3, 4],
        y=[2, 1, 3, 4],
        error_x=dict(
            type='percent',
            value=10
        )
    )
]
py.iplot(data, filename='error-bar-horizontal')
```

#### Bar Chart with Error Bars

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['Trial 1', 'Trial 2', 'Trial 3'],
    y=[3, 6, 4],
    name='Control',
    error_y=dict(
        type='data',
        array=[1, 0.5, 1.5],
        visible=True
    )
)
trace2 = go.Bar(
    x=['Trial 1', 'Trial 2', 'Trial 3'],
    y=[4, 7, 3],
    name='Experimental',
    error_y=dict(
        type='data',
        array=[0.5, 1, 2],
        visible=True
    )
)
data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='error-bar-bar')
```

#### Colored and Styled Error Bars

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x_theo = np.linspace(-4, 4, 100)
sincx = np.sinc(x_theo)
x = [-3.8, -3.03, -1.91, -1.46, -0.89, -0.24, -0.0, 0.41, 0.89, 1.01, 1.91, 2.28, 2.79, 3.56]
y = [-0.02, 0.04, -0.01, -0.27, 0.36, 0.75, 1.03, 0.65, 0.28, 0.02, -0.11, 0.16, 0.04, -0.15]

trace1 = go.Scatter(
    x=x_theo,
    y=sincx,
    name='sinc(x)'
)
trace2 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='measured',
    error_y=dict(
        type='constant',
        value=0.1,
        color='#85144B',
        thickness=1.5,
        width=3,
    ),
    error_x=dict(
        type='constant',
        value=0.2,
        color='#85144B',
        thickness=1.5,
        width=3,
    ),
    marker=dict(
        color='#85144B',
        size=8
    )
)
data = [trace1, trace2]
py.iplot(data, filename='error-bar-style')
```

#### Reference
See https://plot.ly/python/reference/#scatter for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'error-bars.ipynb', 'python/error-bars/', 'Error Bars | plotly',
    'How to add error-bars to charts in Python with Plotly.',
    title = 'Error Bars | plotly',
    name = 'Error Bars',
    thumbnail='thumbnail/error-bar.jpg', language='python',
    page_type='example_index', has_thumbnail='true', display_as='statistical', order=1,
    ipynb='~notebook_demo/18')
```

```python

```