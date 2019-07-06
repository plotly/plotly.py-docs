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
    description: Create a linear fit / regression in Python and add a line of best
      fit to your chart.
    display_as: statistics
    has_thumbnail: true
    ipynb: ~notebook_demo/139
    language: python
    layout: user-guide
    name: Linear Fit
    order: 10
    page_type: example_index
    permalink: python/linear-fits/
    thumbnail: thumbnail/linear_fit.jpg
    title: Linear Fit
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Linear fits are available in version <b>1.9.2+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

### Linear Fit

```python
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.graph_objs as go

# Scientific libraries
from numpy import arange,array,ones
from scipy import stats


xi = arange(0,9)
A = array([ xi, ones(9)])

# (Almost) linear sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]

# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
line = slope*xi+intercept

# Creating the dataset, and generating the plot
trace1 = go.Scatter(
                  x=xi,
                  y=y,
                  mode='markers',
                  marker=go.Marker(color='rgb(255, 127, 14)'),
                  name='Data'
                  )

trace2 = go.Scatter(
                  x=xi,
                  y=line,
                  mode='lines',
                  marker=go.Marker(color='rgb(31, 119, 180)'),
                  name='Fit'
                  )

annotation = go.Annotation(
                  x=3.5,
                  y=23.5,
                  text='$R^2 = 0.9551,\\Y = 0.716X + 19.18$',
                  showarrow=False,
                  font=go.Font(size=16)
                  )
layout = go.Layout(
                title='Linear Fit in Python',
                plot_bgcolor='rgb(229, 229, 229)',
                  xaxis=go.XAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
                  yaxis=go.YAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
                  annotations=[annotation]
                )

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Linear-Fit-in-python')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'linear-fits.ipynb', 'python/linear-fits/', 'Linear Fit',
    'Create a linear fit / regression in Python and add a line of best fit to your chart.',
    title = 'Linear Fit',
    name = 'Linear Fit',
    has_thumbnail='true', thumbnail='thumbnail/linear_fit.jpg',
    language='python', page_type='example_index',
    display_as='statistics', order=10,
    ipynb= '~notebook_demo/139')
```

```python

```