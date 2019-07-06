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
    description: Learn how to find peaks and valleys on datasets in Python
    display_as: peak-analysis
    has_thumbnail: false
    ipynb: ~notebook_demo/120
    language: python
    layout: user-guide
    name: Peak Finding
    order: 3
    page_type: example_index
    permalink: python/peak-finding/
    thumbnail: /images/static-image
    title: Peak Finding in Python | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/) and [PeakUtils](http://pythonhosted.org/PeakUtils/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
import peakutils
```

#### Import Data
To start detecting peaks, we will import some data on milk production by month:

```python
milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']
time_series = time_series.tolist()

df = milk_data[0:15]

table = FF.create_table(df)
py.iplot(table, filename='milk-production-dataframe')
```

#### Original Plot

```python
trace = go.Scatter(
    x = [j for j in range(len(time_series))],
    y = time_series,
    mode = 'lines'
)

data = [trace]
py.iplot(data, filename='milk-production-plot')
```

#### With Peak Detection
We need to find the x-axis indices for the peaks in order to determine where the peaks are located.

```python
cb = np.array(time_series)
indices = peakutils.indexes(cb, thres=0.02/max(cb), min_dist=0.1)

trace = go.Scatter(
    x=[j for j in range(len(time_series))],
    y=time_series,
    mode='lines',
    name='Original Plot'
)

trace2 = go.Scatter(
    x=indices,
    y=[time_series[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='rgb(255,0,0)',
        symbol='cross'
    ),
    name='Detected Peaks'
)

data = [trace, trace2]
py.iplot(data, filename='milk-production-plot-with-peaks')
```

#### Only Highest Peaks
We can attempt to set our threshold so that we identify as many of the _highest peaks_ that we can.

```python
cb = np.array(time_series)
indices = peakutils.indexes(cb, thres=0.678, min_dist=0.1)

trace = go.Scatter(
    x=[j for j in range(len(time_series))],
    y=time_series,
    mode='lines',
    name='Original Plot'
)

trace2 = go.Scatter(
    x=indices,
    y=[time_series[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='rgb(255,0,0)',
        symbol='cross'
    ),
    name='Detected Peaks'
)

data = [trace, trace2]
py.iplot(data, filename='milk-production-plot-with-higher-peaks')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Peak-Finding.ipynb', 'python/peak-finding/', 'Peak Finding | plotly',
    'Learn how to find peaks and valleys on datasets in Python',
    title='Peak Finding in Python | plotly',
    name='Peak Finding',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='peak-analysis', order=3,
    ipynb= '~notebook_demo/120')
```

```python

```