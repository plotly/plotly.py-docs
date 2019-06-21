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
    description: How to make Heatmaps in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/33
    language: python
    layout: user-guide
    name: Heatmaps
    order: 3
    page_type: example_index
    permalink: python/heatmaps/
    redirect_from: python/heatmap/
    thumbnail: thumbnail/heatmap.jpg
    title: Python Heatmaps | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Plotly's python package is updated frequently. Run pip install plotly --upgrade to use the latest version.

```python
import plotly
plotly.__version__
```

### Basic Heatmap

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Heatmap(z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]])
data=[trace]
py.iplot(data, filename='basic-heatmap')
```

### Heatmap with Categorical Axis Labels

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening'])
data=[trace]
py.iplot(data, filename='labelled-heatmap')
```

### Heatmap with Unequal Block Sizes


```python
import numpy as np
import plotly.plotly as py

def spiral(th):
    a = 1.120529
    b = 0.306349
    r = a*np.exp(-b*th)
    return (r*np.cos(th), r*np.sin(th))

nspiral = 2 # number of spiral loops

th = np.linspace(-np.pi/13,2*np.pi*nspiral,1000); # angle
(x,y) = spiral(th)

# shift the spiral north so that it is centered
yshift = (1.6 - (max(y)-min(y)))/2

s = dict(x= -x+x[0], y= y-y[0]+yshift,
     line =dict(color='white',width=3))

# Build the rectangles as a heatmap
# specify the edges of the heatmap squares
phi = ( 1+np.sqrt(5) )/2.
xe = [0, 1, 1+(1/(phi**4)), 1+(1/(phi**3)), phi]
ye = [0, 1/(phi**3),1/phi**3+1/phi**4,1/(phi**2),1]

z = [ [13,3,3,5],
      [13,2,1,5],
      [13,10,11,12],
      [13,8,8,8]
    ]

hm = dict(x = np.sort(xe),
          y = np.sort(ye)+yshift,
          z = z,
          type = 'heatmap',
          colorscale = 'Viridis')

axis_template = dict(range = [0,1.6], autorange = False,
             showgrid = False, zeroline = False,
             linecolor = 'black', showticklabels = False,
             ticks = '' )

layout = dict( margin = dict(t=200,r=200,b=200,l=200),
    xaxis = axis_template,
    yaxis = axis_template,
    showlegend = False,
    width = 700, height = 700,
    autosize = False )

figure = dict(data=[s, hm],layout=layout)

py.iplot(figure, filename='golden spiral', height=750)

```

### Heatmap with Datetime Axis

```python

import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, 180)]

z = []

for prgmr in programmers:
    new_row = []
    for date in date_list:
        new_row.append( np.random.poisson() )
    z.append(list(new_row))

data = [
    go.Heatmap(
        z=z,
        x=date_list,
        y=programmers,
        colorscale='Viridis',
    )
]

layout = go.Layout(
    title='GitHub commits per day',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='datetime-heatmap')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its source code can be found [here](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-heatmapplot) and can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-heatmapplot/", width="120%", height="650px", frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-heatmapplot/code", width="120%", height=500, frameBorder="0")
```

#### Reference
See https://plot.ly/python/reference/#heatmap for more information and chart attribute options!


```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/csshref="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'heatmaps.ipynb', ' python/heatmaps/', 'Heatmaps | plotly',
    'How to make Heatmaps in Python with Plotly.',
    title = 'Python Heatmaps | plotly',
    name = 'Heatmaps',
    has_thumbnail='true', thumbnail='thumbnail/heatmap.jpg',
    language='python', page_type='example_index',
    display_as='scientific',order=3,
    ipynb= '~notebook_demo/33', redirect_from='python/heatmap/')
```

```python

```
