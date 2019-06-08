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

## Histogram with plotly express

A [histogram](https://en.wikipedia.org/wiki/Histogram) is representation of the distribution of numerical data, where the data are binned and the count for each bin is represented.

Plotly express functions *(TODO here needs link to stable px doc entry)* take as argument a tidy [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html).

```python
import plotly_express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill")
fig.show()      
```

#### Choosing the number of bins

By default, the number of bins is chosen so that this number is comparable to the typical number of samples in a bin. This number can be customized, as well as the range of values.

```python
import plotly_express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill", nbins=20)
fig.show()  
```

#### Type of normalization

The default mode is to represent the count of samples in each bin. With the `histnorm` argument, it is also possible to represent the percentage or fraction of samples in each bin (`histnorm='percent'` or `probability`), or a density histogram (the sum of bars is equal to 100, `density`), or a probability density histogram (sum equal to 1, `probability density`).

```python
import plotly_express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill", histnorm='probability density')
fig.show()  
```

#### Aspect of the histogram plot 

```python
import plotly_express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill",
                   title='Histogram of bills',
                   labels={'total_bill':'total bill'}, # can specify one label per df column
                   opacity=0.6,
                   log_y=True, # represent bars with log scale
                   color_discrete_sequence=['red'] # color of histogram bars
                   )
fig.show()  
```

#### Several histograms for the different values of one column

```python
import plotly_express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill", color="sex")
fig.show()  
```

#### Using histfunc

For each bin of `x`, one can compute a function of data using `histfunc`. The argument of `histfunc` is the dataframe column given as the `y` argument. Below the plot shows that the average tip increases with the total bill.

```python
import plotly_express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill", y="tip", histfunc='avg')
fig.show()  
```

#### Visualizing the distribution

With the `marginal` keyword, a subplot is drawn alongside the histogram, visualizing the distribution.

```python
import plotly_express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill", color="sex", marginal="rug", # can be `box`, `violin`
                         hover_data=tips.columns)
fig.show()
```

## Histograms with go.Histogram

When data are not available as tidy dataframes, it is also possible to use the more generic `go.Histogram` from `plotly.graph_objs`.

### Basic Histogram ###

```python
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(500)
data = [go.Histogram(x=x)]

fig = go.Figure(data=data)
fig.show()
```

### Normalized Histogram

```python
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(500)
data = [go.Histogram(x=x,
                     histnorm='probability')]

fig = go.Figure(data=data)
fig.show()
```

### Horizontal Histogram ###

```python
import plotly.graph_objs as go

import numpy as np

y = np.random.randn(500)
# Use `y` argument instead of `x` for horizontal histogram
data = [go.Histogram(y=y)]

fig = go.Figure(data=data)
fig.show()
```

### Overlaid Histogram ###

```python
import plotly.graph_objs as go

import numpy as np

x0 = np.random.randn(500)
x1 = np.random.randn(500) + 1

trace0 = go.Histogram(x=x0)
trace1 = go.Histogram(x=x1)

fig = go.Figure(data=[trace0, trace1])
# Overlay both histograms
fig.update(layout_barmode='overlay')
# Reduce opacity to see both histograms
fig.update_traces(opacity=0.75)
```

### Stacked Histograms 

```python
import plotly.graph_objs as go

import numpy as np

x0 = np.random.randn(2000)
x1 = np.random.randn(2000) + 1

trace0 = go.Histogram(x=x0)
trace1 = go.Histogram(x=x1)

fig = go.Figure(data=[trace0, trace1])
# The two histograms are drawn on top of another
fig.update(layout_barmode='stack')
```

### Styled Histogram

```python
import plotly.graph_objs as go

import numpy as np
x0 = np.random.randn(500)
x1 = np.random.randn(500) + 1

trace0 = go.Histogram(
    x=x0,
    histnorm='percent',
    name='control', # name used in legend
    xbins=dict( # bins used for histogram
        start=-4.0,
        end=3.0,
        size=0.5
    ),
    marker_color='#EB89B5',
    opacity=0.75
)
trace1 = go.Histogram(
    x=x1,
    histnorm='percent',
    name='experimental',
    xbins=dict(
        start=-3.0,
        end=4,
        size=0.5
    ),
    marker_color='#330C73',
    opacity=0.75
)

layout = go.Layout(
    title='Sampled Results', # title of plot
    xaxis_title='Value', # xaxis label
    yaxis_title='Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)
fig = go.Figure(data=[trace0, trace1], layout=layout)
fig.show()
```

### Cumulative Histogram 

```python
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(500)
data = [go.Histogram(x=x, cumulative_enabled=True)]

fig = go.Figure(data=data)
fig.show()
```

### Specify Binning Function

```python
import plotly.graph_objs as go

x = ["Apples","Apples","Apples","Oranges", "Bananas"]
y = ["5","10","3","10","5"]

data = [
  go.Histogram(
    histfunc = "count",
    y=y,
    x=x,
    name="count"
  ),
  go.Histogram(
    histfunc="sum",
    y=y,
    x=x,
    name="sum"
  )
]

fig = go.Figure(data=data)
fig
```

### Custom Binning
For custom binning along x-axis, use the attribute [`nbinsx`](https://plot.ly/python/reference/#histogram-nbinsx). Please note that the autobin algorithm will choose a 'nice' round bin size that may result in somewhat fewer than `nbinsx` total bins. Alternatively, you can set the exact values for [`xbins`](https://plot.ly/python/reference/#histogram-xbins) along with `autobinx = False`.

```python
import plotly.graph_objs as go
from plotly.subplots import make_subplots

x = ['1970-01-01', '1970-01-01', '1970-02-01', '1970-04-01', '1970-01-02', 
     '1972-01-31', '1970-02-13', '1971-04-19']


trace0 = go.Histogram(x=x, nbinsx=4)
trace1 = go.Histogram(x=x, nbinsx = 8)
trace2 = go.Histogram(x=x, nbinsx=10)
trace3 = go.Histogram(x=x,
                      xbins=dict(
                      start='1969-11-15',
                      end='1972-03-31',
                      size='M18'), # M18 stands for 18 months
                      autobinx=False
                     )
trace4 = go.Histogram(x=x,
                      xbins=dict(
                      start='1969-11-15',
                      end='1972-03-31',
                      size='M4'), # 4 months bin size
                      autobinx=False
                      )
trace5 = go.Histogram(x=x,
                      xbins=dict(
                      start='1969-11-15',
                      end='1972-03-31',
                      size= 'M2'), # 2 months
                      autobinx = False
                      )
  
fig = make_subplots(rows=3, cols=2)
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 2)
fig.append_trace(trace4, 3, 1)
fig.append_trace(trace5, 3, 2)

fig.show()
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

