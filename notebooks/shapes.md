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
    description: How to make SVG shapes in python. Examples of lines, circle, rectangle,
      and path.
    display_as: style_opt
    has_thumbnail: true
    ipynb: ~notebook_demo/14
    language: python
    layout: user-guide
    name: Shapes
    order: 5
    page_type: example_index
    permalink: python/shapes/
    thumbnail: thumbnail/shape.jpg
    title: Shapes | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Vertical and Horizontal Lines Positioned Relative to the Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[2, 3.5, 6],
    y=[1, 1.5, 1],
    text=['Vertical Line', 'Horizontal Dashed Line', 'Diagonal dotted Line'],
    mode='text',
)
data = [trace0]
layout = {
    'xaxis': {
        'range': [0, 7]
    },
    'yaxis': {
        'range': [0, 2.5]
    },
    'shapes': [
        # Line Vertical
        {
            'type': 'line',
            'x0': 1,
            'y0': 0,
            'x1': 1,
            'y1': 2,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line Horizontal
        {
            'type': 'line',
            'x0': 2,
            'y0': 2,
            'x1': 5,
            'y1': 2,
            'line': {
                'color': 'rgb(50, 171, 96)',
                'width': 4,
                'dash': 'dashdot',
            },
        },
        # Line Diagonal
        {
            'type': 'line',
            'x0': 4,
            'y0': 0,
            'x1': 6,
            'y1': 2,
            'line': {
                'color': 'rgb(128, 0, 128)',
                'width': 4,
                'dash': 'dot',
            },
        },
    ]
}

fig = {
    'data': data,
    'layout': layout,
}

py.iplot(fig, filename='shapes-lines')
```

#### Lines Positioned Relative to the Plot & to the Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[2, 6],
    y=[1, 1],
    text=['Line positioned relative to the plot', 
          'Line positioned relative to the axes'],
    mode='text',
)
data = [trace0]
layout = {
    'xaxis': {
        'range': [0, 8]
    },
    'yaxis': {
        'range': [0, 2]
    },
    'shapes': [
        # Line reference to the axes
        {
            'type': 'line',
            'xref': 'x',
            'yref': 'y',
            'x0': 4,
            'y0': 0,
            'x1': 8,
            'y1': 1,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line reference to the plot
        {
            'type': 'line',
            'xref': 'paper',
            'yref': 'paper',
            'x0': 0,
            'y0': 0,
            'x1': 0.5,
            'y1': 0.5,
            'line': {
                'color': 'rgb(50, 171, 96)',
                'width': 3,
            },
        },
    ]
}
fig = {
    'data': data,
    'layout': layout,
}
py.iplot(fig, filename='shapes-line-ref')
```

#### Creating Tangent Lines with Shapes

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x0 = np.linspace(1, 3, 200)
y0 = x0 * np.sin(np.power(x0, 2)) + 1

trace0 = go.Scatter(
    x=x0,
    y=y0,
)
data = [trace0]
layout = {
    'title': "$f(x)=x\\sin(x^2)+1\\\\ f\'(x)=\\sin(x^2)+2x^2\\cos(x^2)$",
    'shapes': [
        {
            'type': 'line',
            'x0': 1,
            'y0': 2.30756,
            'x1': 1.75,
            'y1': 2.30756,
            'opacity': 0.7,
            'line': {
                'color': 'red',
                'width': 2.5,
            },
        },
        {
            'type': 'line',
            'x0': 2.5,
            'y0': 3.80796,
            'x1': 3.05,
            'y1': 3.80796,
            'opacity': 0.7,
            'line': {
                'color': 'red',
                'width': 2.5,
            },
        },
        {
            'type': 'line',
            'x0': 1.90,
            'y0': -1.1827,
            'x1': 2.50,
            'y1': -1.1827,
            'opacity': 0.7,
            'line': {
                'color': 'red',
                'width': 2.5,
            },
        },
    ]
}
fig = {
    'data': data,
    'layout': layout,
}
py.iplot(fig, filename='tangent-line')
```

#### Rectangles Positioned Relative to the Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1.5, 4.5],
    y=[0.75, 0.75],
    text=['Unfilled Rectangle', 'Filled Rectangle'],
    mode='text',
)
data = [trace0]
layout = {
    'xaxis': {
        'range': [0, 7],
        'showgrid': False,
    },
    'yaxis': {
        'range': [0, 3.5]
    },
    'shapes': [
        # unfilled Rectangle
        {
            'type': 'rect',
            'x0': 1,
            'y0': 1,
            'x1': 2,
            'y1': 3,
            'line': {
                'color': 'rgba(128, 0, 128, 1)',
            },
        },
        # filled Rectangle
        {
            'type': 'rect',
            'x0': 3,
            'y0': 1,
            'x1': 6,
            'y1': 2,
            'line': {
                'color': 'rgba(128, 0, 128, 1)',
                'width': 2,
            },
            'fillcolor': 'rgba(128, 0, 128, 0.7)',
        },
    ]
}
fig = {
    'data': data,
    'layout': layout,
}
py.iplot(fig, filename='shapes-rectangle')
```

#### Rectangle Positioned Relative to the Plot & to the Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1.5, 3],
    y=[2.5, 2.5],
    text=['Rectangle reference to the plot',
          'Rectangle reference to the axes'],
    mode='text',
)
data = [trace0]
layout = {
    'xaxis': {
        'range': [0, 4],
        'showgrid': False,
    },
    'yaxis': {
        'range': [0, 4]
    },
    'shapes': [
        # Rectangle reference to the axes
        {
            'type': 'rect',
            'xref': 'x',
            'yref': 'y',
            'x0': 2.5,
            'y0': 0,
            'x1': 3.5,
            'y1': 2,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
            'fillcolor': 'rgba(55, 128, 191, 0.6)',
        },
        # Rectangle reference to the plot
        {
            'type': 'rect',
            'xref': 'paper',
            'yref': 'paper',
            'x0': 0.25,
            'y0': 0,
            'x1': 0.5,
            'y1': 0.5,
            'line': {
                'color': 'rgb(50, 171, 96)',
                'width': 3,
            },
            'fillcolor': 'rgba(50, 171, 96, 0.6)',
        },
    ]
}
fig = {
    'data': data,
    'layout': layout,
}
py.iplot(fig, filename='shapes-rectangle-ref')
```

#### Highlighting Time Series Regions with Rectangle Shapes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=['2015-02-01', '2015-02-02', '2015-02-03', '2015-02-04', '2015-02-05',
        '2015-02-06', '2015-02-07', '2015-02-08', '2015-02-09', '2015-02-10',
        '2015-02-11', '2015-02-12', '2015-02-13', '2015-02-14', '2015-02-15',
        '2015-02-16', '2015-02-17', '2015-02-18', '2015-02-19', '2015-02-20',
        '2015-02-21', '2015-02-22', '2015-02-23', '2015-02-24', '2015-02-25',
        '2015-02-26', '2015-02-27', '2015-02-28'],
    y=[-14, -17, -8, -4, -7, -10, -12, -14, -12, -7, -11, -7, -18, -14, -14,
        -16, -13, -7, -8, -14, -8, -3, -9, -9, -4, -13, -9, -6],
    mode='lines',
    name='temperature'
)
data = [trace0]
layout = {
    # to highlight the timestamp we use shapes and create a rectangular
    'shapes': [
        # 1st highlight during Feb 4 - Feb 6
        {
            'type': 'rect',
            # x-reference is assigned to the x-values
            'xref': 'x',
            # y-reference is assigned to the plot paper [0,1]
            'yref': 'paper',
            'x0': '2015-02-04',
            'y0': 0,
            'x1': '2015-02-06',
            'y1': 1,
            'fillcolor': '#d3d3d3',
            'opacity': 0.2,
            'line': {
                'width': 0,
            }
        },
        # 2nd highlight during Feb 20 - Feb 23
        {
            'type': 'rect',
            'xref': 'x',
            'yref': 'paper',
            'x0': '2015-02-20',
            'y0': 0,
            'x1': '2015-02-22',
            'y1': 1,
            'fillcolor': '#d3d3d3',
            'opacity': 0.2,
            'line': {
                'width': 0,
            }
        }
    ]
}
py.iplot({'data': data, 'layout': layout}, filename='timestamp-highlight')
```

#### Circles Positioned Relative to the Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1.5, 3.5],
    y=[0.75, 2.5],
    text=['Unfilled Circle', 
          'Filled Circle'],
    mode='text',
)
data = [trace0]

layout = {
    'xaxis': {
        'range': [0, 4.5],
        'zeroline': False,
    },
    'yaxis': {
        'range': [0, 4.5]
    },
    'width': 800,
    'height': 800,
    'shapes': [
        # unfilled circle
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': 1,
            'y0': 1,
            'x1': 3,
            'y1': 3,
            'line': {
                'color': 'rgba(50, 171, 96, 1)',
            },
        },
        # filled circle
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'fillcolor': 'rgba(50, 171, 96, 0.7)',
            'x0': 3,
            'y0': 3,
            'x1': 4,
            'y1': 4,
            'line': {
                'color': 'rgba(50, 171, 96, 1)',
            },
        },
    ]
}
fig = {
    'data': data,
    'layout': layout,
}
py.iplot(fig, filename='shapes-circle')
```

#### Highlighting Clusters of Scatter Points with Circle Shapes

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x0 = np.random.normal(2, 0.45, 300)
y0 = np.random.normal(2, 0.45, 300)

x1 = np.random.normal(6, 0.4, 200)
y1 = np.random.normal(6, 0.4, 200)

x2 = np.random.normal(4, 0.3, 200)
y2 = np.random.normal(4, 0.3, 200)

trace0 = go.Scatter(
    x=x0,
    y=y0,
    mode='markers',
)
trace1 = go.Scatter(
    x=x1,
    y=y1,
    mode='markers'
)
trace2 = go.Scatter(
    x=x2,
    y=y2,
    mode='markers'
)
trace3 = go.Scatter(
    x=x1,
    y=y0,
    mode='markers'
)
layout = {
    'shapes': [
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': min(x0),
            'y0': min(y0),
            'x1': max(x0),
            'y1': max(y0),
            'opacity': 0.2,
            'fillcolor': 'blue',
            'line': {
                'color': 'blue',
            },
        },
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': min(x1),
            'y0': min(y1),
            'x1': max(x1),
            'y1': max(y1),
            'opacity': 0.2,
            'fillcolor': 'orange',
            'line': {
                'color': 'orange',
            },
        },
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': min(x2),
            'y0': min(y2),
            'x1': max(x2),
            'y1': max(y2),
            'opacity': 0.2,
            'fillcolor': 'green',
            'line': {
                'color': 'green',
            },
        },
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': min(x1),
            'y0': min(y0),
            'x1': max(x1),
            'y1': max(y0),
            'opacity': 0.2,
            'fillcolor': 'red',
            'line': {
                'color': 'red',
            },
        },
    ],
    'showlegend': False,
}
data = [trace0, trace1, trace2, trace3]
fig = {
    'data': data,
    'layout': layout,
}
py.iplot(fig, filename='clusters')
```

#### Venn Diagram with Circle Shapes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 1.75, 2.5],
    y=[1, 1, 1],
    text=['$A$', '$A+B$', '$B$'],
    mode='text',
    textfont=dict(
        color='black',
        size=18,
        family='Arail',
    )
)

data = [trace0]

layout = {
    'xaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'shapes': [
        {
            'opacity': 0.3,
            'xref': 'x',
            'yref': 'y',
            'fillcolor': 'blue',
            'x0': 0,
            'y0': 0,
            'x1': 2,
            'y1': 2,
            'type': 'circle',
            'line': {
                'color': 'blue',
            },
        },
        {
            'opacity': 0.3,
            'xref': 'x',
            'yref': 'y',
            'fillcolor': 'gray',
            'x0': 1.5,
            'y0': 0,
            'x1': 3.5,
            'y1': 2,
            'type': 'circle',
            'line': {
                'color': 'gray',
            },
        }
    ],
    'margin': {
        'l': 20,
        'r': 20,
        'b': 100
    },
    'height': 600,
    'width': 800,
}
fig = {
    'data': data,
    'layout': layout,
}
py.iplot(fig, filename='venn-diagram')
```

#### SVG Paths

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[2, 1, 8, 8],
    y=[0.25, 9, 2, 6],
    text=['Filled Triangle',
          'Filled Polygon',
          'Quadratic Bezier Curves',
          'Cubic Bezier Curves'],
    mode='text',
)
data = [trace0]
layout = {

    'xaxis': {
        'range': [0, 9],
        'zeroline': False,
    },
    'yaxis': {
        'range': [0, 11],
        'showgrid': False,
    },
    'shapes': [
        # Quadratic Bezier Curves
        {
            'type': 'path',
            'path': 'M 4,4 Q 6,0 8,4',
            'line': {
                'color': 'rgb(93, 164, 214)',
            },
        },
        # Cubic Bezier Curves
        {
            'type': 'path',
            'path': 'M 1,4 C 2,8 6,4 8,8',
            'line': {
                'color': 'rgb(207, 114, 255)',
            },
        },
        # filled Triangle
        {
            'type': 'path',
            'path': ' M 1 1 L 1 3 L 4 1 Z',
            'fillcolor': 'rgba(44, 160, 101, 0.5)',
            'line': {
                'color': 'rgb(44, 160, 101)',
            },
        },
        # filled Polygon
        {
            'type': 'path',
            'path': ' M 3,7 L2,8 L2,9 L3,10, L4,10 L5,9 L5,8 L4,7 Z',
            'fillcolor': 'rgba(255, 140, 184, 0.5)',
            'line': {
                'color': 'rgb(255, 140, 184)',
            },
        },

    ]
}
fig = {
    'data': data,
    'layout': layout,
}
py.iplot(fig, filename='shapes-path')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-shapesplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-shapesplot/", width="100%", height="650px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-shapesplot/code", width="100%", height=500, frameBorder="0")

```

#### Reference
See https://plot.ly/python/reference/#layout-shapes for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'shapes.ipynb', 'python/shapes/', 'Shapes | plotly',
    'How to make SVG shapes in python. Examples of lines, circle, rectangle, and path.',
    title = 'Shapes | plotly',
    name = 'Shapes',
    thumbnail='thumbnail/shape.jpg', language='python',
    page_type='example_index', has_thumbnail='true', display_as='style_opt', order=5, 
    ipynb='~notebook_demo/14')
```