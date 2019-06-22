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
    display_name: Python 3
    language: python
    name: python3
  plotly:
    description: How to make scatter plots in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/2
    language: python
    layout: user-guide
    name: Scatter Plots
    order: 2
    page_type: example_index
    permalink: python/line-and-scatter/
    redirect_from: python/line-and-scatter-plots-tutorial/
    thumbnail: thumbnail/line-and-scatter.jpg
    title: Python Scatter Plots | plotly
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

#### Simple Scatter Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')

# or plot with: plot_url = py.plot(data, filename='basic-line')
```

#### Line and Scatter Plots

```python
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

# Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'markers'
)
trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines',
    name = 'lines'
)

data = [trace0, trace1, trace2]
py.iplot(data, filename='scatter-mode')
```

#### Style Scatter Plots

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

N = 500

trace0 = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)+2,
    name = 'Above',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(152, 0, 0, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)-2,
    name = 'Below',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(255, 182, 193, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = 'Styled Scatter',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False)
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-scatter')
```

#### Data Labels on Hover

```python
import plotly.plotly as py
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd

l= []
y= []
data= pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
# Setting colors for plot.
N= 53
c= ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

for i in range(int(N)):
    y.append((2000+i))
    trace0= go.Scatter(
        x= data['Rank'],
        y= data['Population']+(i*1000000),
        mode= 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= c[i],
                    opacity= 0.3
                   ),name= y[i],
        text= data['State']) # The hover text goes here...
    l.append(trace0);

layout= go.Layout(
    title= 'Stats of USA States',
    hovermode= 'closest',
    xaxis= dict(
        title= 'Population',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Rank',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)
fig= go.Figure(data=l, layout=layout)
py.iplot(fig)
```

#### Scatter with a Color Dimension

```python
import plotly.graph_objs as go
import plotly.plotly as py

import numpy as np

trace1 = go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color = np.random.randn(500), #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    )
)
data = [trace1]

py.iplot(data, filename='scatter-plot-with-colorscale')
```

#### Large Data Sets

Now in Ploty you can implement WebGL with `Scattergl()` in place of `Scatter()` <br>
for increased speed, improved interactivity, and the ability to plot even more data!

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

N = 100000
trace = go.Scattergl(
    x = np.random.randn(N),
    y = np.random.randn(N),
    mode = 'markers',
    marker = dict(
        color = '#FFBAD2',
        line = dict(width = 1)
    )
)
data = [trace]
py.iplot(data, filename='compare_webgl')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-linescatterplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-linescatterplot/", width="100%",height="750px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-linescatterplot/code", width="100%",height=500, frameBorder="0")
```

### Reference
See https://plot.ly/python/reference/#scatter or https://plot.ly/python/reference/#scattergl for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'scatter.ipynb', 'python/line-and-scatter/', 'Python Scatter Plots | plotly',
    'How to make scatter plots in Python with Plotly.',
    title = 'Python Scatter Plots | plotly',
    name = 'Scatter Plots',
    has_thumbnail='true', thumbnail='thumbnail/line-and-scatter.jpg',
    language='python', page_type='example_index',
    display_as='basic', order=2,
    redirect_from='python/line-and-scatter-plots-tutorial/',
    ipynb= '~notebook_demo/2')
```
