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
    description: Learn how to use Python to make a Random Walk
    display_as: statistics
    has_thumbnail: false
    ipynb: ~notebook_demo/114
    language: python
    layout: user-guide
    name: Random Walk
    order: 10
    page_type: example_index
    permalink: python/random-walk/
    thumbnail: /images/static-image
    title: Random Walk in Python. | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/), and [Random](https://docs.python.org/2/library/random.html).

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
import random
```

####Tips
A `random walk` can be thought of as a random process in which a tolken or a marker is randomly moved around some space, that is, a space with a metric used to compute distance. It is more commonly conceptualized in one dimension ($\mathbb{Z}$), two dimensions ($\mathbb{Z}^2$) or three dimensions ($\mathbb{Z}^3$) in Cartesian space, where $\mathbb{Z}$ represents the set of integers. In the visualizations below, we will be using [scatter plots](https://plot.ly/python/next/line-and-scatter/) as well as a colorscale to denote the time sequence of the walk.


#### Random Walk in 1D


The jitter in the data points along the x and y axes are meant to illuminate where the points are being drawn and what the tendancy of the random walk is.

```python
x = [0]

for j in range(100):
    step_x = random.randint(0,1)
    if step_x == 1:
        x.append(x[j] + 1 + 0.05*np.random.normal())
    else:
        x.append(x[j] - 1 + 0.05*np.random.normal())

y = [0.05*np.random.normal() for j in range(len(x))]

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Random Walk in 1D',
    marker=dict(
        color=[i for i in range(len(x))],
        size=7,
        colorscale=[[0, 'rgb(178,10,28)'], [0.50, 'rgb(245,160,105)'],
                    [0.66, 'rgb(245,195,157)'], [1, 'rgb(220,220,220)']],
        showscale=True,
    )
)

layout = go.Layout(
    yaxis=dict(
        range=[-1, 1]
    )
)

data = [trace1]
fig= go.Figure(data=data, layout=layout)
py.iplot(fig, filename='random-walk-1d')
```

#### Random Walk in 2D

```python
x = [0]
y = [0]

for j in range(1000):
    step_x = random.randint(0,1)
    if step_x == 1:
        x.append(x[j] + 1 + np.random.normal())
    else:
        x.append(x[j] - 1 + np.random.normal())

    step_y = random.randint(0,1)
    if step_y == 1:
        y.append(y[j] + 1 + np.random.normal())
    else:
        y.append(y[j] - 1 + np.random.normal())

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Random Walk',
    marker=dict(
        color=[i for i in range(len(x))],
        size=8,
        colorscale='Greens',
        showscale=True
    )
)

data = [trace1]
py.iplot(data, filename='random-walk-2d')
```

#### Advanced Tip
We can formally think of a 1D random walk as a point jumping along the integer number line. Let $Z_i$ be a random variable that takes on the values +1 and -1. Let this random variable represent the steps we take in the random walk in 1D (where +1 means right and -1 means left). Also, as with the above visualizations, let us assume that the probability of moving left and right is just $\frac{1}{2}$. Then, consider the sum

$$
\begin{align*}
S_n = \sum_{i=0}^{n}{Z_i}
\end{align*}
$$

where S_n represents the point that the random walk ends up on after n steps have been taken.

To find the `expected value` of $S_n$, we can compute it directly. Since each $Z_i$ is independent, we have

$$
\begin{align*}
\mathbb{E}(S_n) = \sum_{i=0}^{n}{\mathbb{E}(Z_i)}
\end{align*}
$$

but since $Z_i$ takes on the values +1 and -1 then

$$
\begin{align*}
\mathbb{E}(Z_i) = 1 \cdot P(Z_i=1) + -1 \cdot P(Z_i=-1) = \frac{1}{2} - \frac{1}{2} = 0
\end{align*}
$$

Therefore, we expect our random walk to hover around $0$ regardless of how many steps we take in our walk.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Random-Walk.ipynb', 'python/random-walk/', 'Random Walk | plotly',
    'Learn how to use Python to make a Random Walk',
    title='Random Walk in Python. | plotly',
    name='Random Walk',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='statistics', order=10,
    ipynb= '~notebook_demo/114')
```

```python

```
