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
    description: Learn how to perform smoothing using various methods in Python.
    display_as: signal-analysis
    has_thumbnail: false
    language: python
    layout: user-guide
    name: Smoothing
    order: 1
    page_type: example_index
    permalink: python/smoothing/
    thumbnail: /images/static-image
    title: Smoothing in Python | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/) and [Plotly](https://plot.ly/python/getting-started/).

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import scipy

from scipy import signal
```

#### Savitzky-Golay Filter
`Smoothing` is a technique that is used to eliminate noise from a dataset. There are many algorithms and methods to accomplish this but all have the same general purpose of 'roughing out the edges' or 'smoothing' some data.

There is reason to smooth data if there is little to no small-scale structure in the data. The danger to this thinking is that one may skew the representation of the data enough to change its percieved meaning, so for the sake of scientific honesty it is an imperative to at the very minimum explain one's reason's for using a smoothing algorithm to their dataset.

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
y_noise = [y_item + np.random.choice([-1, 1])*np.random.random() for y_item in y]

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(
        size=2,
        color='rgb(0, 0, 0)',
    ),
    name='Sine'
)

trace2 = go.Scatter(
    x=x,
    y=y_noise,
    mode='markers',
    marker=dict(
        size=6,
        color='#5E88FC',
        symbol='circle-open'
    ),
    name='Noisy Sine'
)

trace3 = go.Scatter(
    x=x,
    y=signal.savgol_filter(y, 53, 3),
    mode='markers',
    marker=dict(
        size=6,
        color='#C190F0',
        symbol='triangle-up'
    ),
    name='Savitzky-Golay'
)

layout = go.Layout(
    showlegend=True
)

data = [trace1, trace2, trace3]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='smoothing-savitzky-golay-filter')
```

#### Triangular Moving Average

Another method for smoothing is a moving average. There are various forms of this, but the idea is to take a window of points in your dataset, compute an average of the points, then shift the window over by one point and repeat. This will generate a bunch of points which will result in the `smoothed` data.

Let us look at the common `Simple Moving Average` first. In the 1D case we have a data set of $N$ points with y-values $y_1, y_2, ..., y_N$. Setting our window size to $n < N$, the new $i^{th}$ y-value after smoothing is computed as:

$$
\begin{align*}
SMA_i = \frac{y_i + ... + y_{i+n}}{n}
\end{align*}
$$

In the `Triangular Moving Average`, two simple moving averages are computed on top of each other. This means that our $SMA_i$ are computed then a Triangular Moving Average $TMA_i$ is computed as:

$$
\begin{align*}
TMA_i = \frac{SMA_i + ... + SMA_{i+n}}{n}
\end{align*}
$$

```python
np.array(list(range(5)) + [5] + list(range(5)[::-1]))
```

```python
def smoothTriangle(data, degree, dropVals=False):
    triangle=np.array(list(range(degree)) + [degree] + list(range(degree)[::-1])) + 1
    smoothed=[]

    for i in range(degree, len(data) - degree * 2):
        point=data[i:i + len(triangle)] * triangle
        smoothed.append(sum(point)/sum(triangle))
    if dropVals:
        return smoothed
    smoothed=[smoothed[0]]*int(degree + degree/2) + smoothed
    while len(smoothed) < len(data):
        smoothed.append(smoothed[-1])
    return smoothed

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(
        size=2,
        color='rgb(0, 0, 0)',
    ),
    name='Sine'
)

trace2 = go.Scatter(
    x=x,
    y=y_noise,
    mode='markers',
    marker=dict(
        size=6,
        color='#5E88FC',
        symbol='circle-open'
    ),
    name='Noisy Sine'
)

trace3 = go.Scatter(
    x=x,
    y=smoothTriangle(y_noise, 10),  # setting degree to 10
    mode='markers',
    marker=dict(
        size=6,
        color='#C190F0',
        symbol='triangle-up'
    ),
    name='Moving Triangle - Degree 10'
)

layout = go.Layout(
    showlegend=True
)

data = [trace1, trace2, trace3]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='smoothing-triangular-moving-average-degree-10')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Smoothing.ipynb', 'python/smoothing/', 'Smoothing | plotly',
    'Learn how to perform smoothing using various methods in Python.',
    title='Smoothing in Python | plotly',
    name='Smoothing',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='signal-analysis', order=1)
```

```python

```
