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
    description: How to add text labels and annotations to plots in python.
    display_as: style_opt
    has_thumbnail: false
    ipynb: ~notebook_demo/204
    language: python
    layout: user-guide
    name: Text and Annotations
    order: 1
    page_type: example_index
    permalink: python/text-and-annotations/
    thumbnail: thumbnail/annotations.jpg
    title: Text and Annotations | plotly
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

### Adding Text to Data in Line and Scatter Plots

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode='lines+markers+text',
    name='Lines, Markers and Text',
    text=['Text A', 'Text B', 'Text C'],
    textposition='top center'
)

trace2 = go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode='markers+text',
    name='Markers and Text',
    text=['Text D', 'Text E', 'Text F'],
    textposition='bottom center'
)

trace3 = go.Scatter(
    x=[0, 1, 2],
    y=[3, 3, 3],
    mode='lines+text',
    name='Lines and Text',
    text=['Text G', 'Text H', 'Text I'],
    textposition='bottom center'
)

data = [trace1, trace2, trace3]

layout = go.Layout(
    showlegend=False
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='text-chart-basic')
```

### Adding Hover Text to Data in Line and Scatter Plots

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[0, 1, 2],
        y=[1, 3, 2],
        mode='markers',
        text=['Text A', 'Text B', 'Text C']
    )
]

layout = go.Layout(
    title='Hover over the points to see the text'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='hover-chart-basic')
```

### Simple Annotation

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
)

trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
)

data = [trace1, trace2]

layout = go.Layout(
    showlegend=False,
    annotations=[
        dict(
            x=2,
            y=5,
            xref='x',
            yref='y',
            text='dict Text',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='simple-annotation')
```

### Multiple Annotations

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
)

trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
)

data = [trace1, trace2]

layout = go.Layout(
    showlegend=False,
    annotations=[
        dict(
            x=2,
            y=5,
            xref='x',
            yref='y',
            text='dict Text',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        dict(
            x=4,
            y=4,
            xref='x',
            yref='y',
            text='dict Text 2',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='multiple-annotation')
```

### 3D Annotations

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Scatter3d(
  x = ["2017-01-01", "2017-02-10", "2017-03-20"],
  y = ["A", "B", "C"],
  z = [1, 1000, 100000],
  name = "z",
)]

layout = go.Layout(
   scene = dict(
    aspectratio = dict(
      x = 1,
      y = 1,
      z = 1
    ),
    camera = dict(
      center = dict(
        x = 0,
        y = 0,
        z = 0
      ),
      eye = dict(
        x = 1.96903462608,
        y = -1.09022831971,
        z = 0.405345349304
      ),
      up = dict(
        x = 0,
        y = 0,
        z = 1
      )
    ),
    dragmode = "turntable",
    xaxis = dict(
      title = "",
      type = "date"
    ),
    yaxis = dict(
      title = "",
      type = "category"
    ),
    zaxis = dict(
      title = "",
      type = "log"
    ),
    annotations = [dict(
        showarrow = False,
        x = "2017-01-01",
        y = "A",
        z = 0,
        text = "Point 1",
        xanchor = "left",
        xshift = 10,
        opacity = 0.7
      ), dict(
        x = "2017-02-10",
        y = "B",
        z = 4,
        text = "Point 2",
        textangle = 0,
        ax = 0,
        ay = -75,
        font = dict(
          color = "black",
          size = 12
        ),
        arrowcolor = "black",
        arrowsize = 3,
        arrowwidth = 1,
        arrowhead = 1
      ), dict(
        x = "2017-03-20",
        y = "C",
        z = 5,
        ax = 50,
        ay = 0,
        text = "Point 3",
        arrowhead = 1,
        xanchor = "left",
        yanchor = "bottom"
      )]
  ),
  xaxis = dict(title = "x"),
  yaxis = dict(title = "y")
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename = "3d annotations")
```

### Custom Text Color and Styling

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode='lines+markers+text',
    name='Lines, Markers and Text',
    text=['Text A', 'Text B', 'Text C'],
    textposition='top right',
    textfont=dict(
        family='sans serif',
        size=18,
        color='#1f77b4'
    )
)

trace2 = go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode='lines+markers+text',
    name='Lines and Text',
    text=['Text G', 'Text H', 'Text I'],
    textposition='bottom center',
    textfont=dict(
        family='sans serif',
        size=18,
        color='#ff7f0e'
    )
)

data = [trace1, trace2]

layout = go.Layout(
    showlegend=False
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='text-chart-styling')
```

### Styling and Coloring Annotations

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
)

trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
)

data = [trace1, trace2]

layout = go.Layout(
    showlegend=False,
    annotations=[
        dict(
            x=2,
            y=5,
            xref='x',
            yref='y',
            text='max=5',
            showarrow=True,
            font=dict(
                family='Courier New, monospace',
                size=16,
                color='#ffffff'
            ),
            align='center',
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='#636363',
            ax=20,
            ay=-30,
            bordercolor='#c7c7c7',
            borderwidth=2,
            borderpad=4,
            bgcolor='#ff7f0e',
            opacity=0.8
        )
    ]
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='style-annotation')
```

### Disabling Hover Text

```python
import plotly.plotly as py

trace = dict(
    x=[1, 2, 3,],
    y=[10, 30, 15],
    type='scatter',
    name='first trace',
    hoverinfo='none'
)

py.iplot([trace], filename='hoverinfo=none')
```

### Text Font as an Array - Styling Each Text Element

```python
import plotly.plotly as py
import plotly.graph_objs as go

fig = go.Figure(
    data=[
        go.Scattergeo(
            lat=[45.5,43.4,49.13,51.1,53.34,45.24,44.64,48.25,49.89,50.45],
            lon=[-73.57,-79.24,-123.06,-114.1,-113.28,-75.43,-63.57,-123.21,-97.13,-104.6],
            marker={
                "color": ["#bebada","#fdb462","#fb8072","#d9d9d9","#bc80bd","#b3de69","#8dd3c7","#80b1d3","#fccde5","#ffffb3"],
                "line": {
                    "width": 1
                },
                "size": 10
            },
            mode="markers+text",
            name="",
            text=["Montreal","Toronto","Vancouver","Calgary","Edmonton","Ottawa","Halifax","Victoria","Winnepeg","Regina"],
            textfont={
                "color": ["#bebada","#fdb462","#fb8072","#d9d9d9","#bc80bd","#b3de69","#8dd3c7","#80b1d3","#fccde5","#ffffb3"],
                "family": ["Arial, sans-serif","Balto, sans-serif","Courier New, monospace","Droid Sans, sans-serif","Droid Serif, serif","Droid Sans Mono, sans-serif","Gravitas One, cursive","Old Standard TT, serif","Open Sans, sans-serif","PT Sans Narrow, sans-serif","Raleway, sans-serif","Times New Roman, Times, serif"],
                "size": [22,21,20,19,18,17,16,15,14,13]
            },
            textposition=["top center","middle left","top center","bottom center","top right","middle left","bottom right","bottom left","top right","top right"]
        )
    ],
    layout={
        "title": "Canadian cities",
        "geo": {
            "lataxis": {
                "range": [40, 70]
            },
            "lonaxis": {
                "range": [-130, -55]
            },
            "scope": "north america"
        }
    }
)

py.iplot(fig, filename='Canadian Cities')
```

### Adding Annotations with xref and yref as Paper

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 2, 3],
        name='y',
    )
]

layout = go.Layout(
    annotations=[
        dict(
            x=0.5004254919715793,
            y=-0.16191064079952971,
            showarrow=False,
            text='Custom x-axis title',
            xref='paper',
            yref='paper'
        ),
        dict(
            x=-0.04944728761514841,
            y=0.4714285714285711,
            showarrow=False,
            text='Custom y-axis title',
            textangle=-90,
            xref='paper',
            yref='paper'
        )
    ],
    autosize=True,
    margin=dict(
        b=100
    ),
    title='Plot Title',
    xaxis=dict(
        autorange=False,
        range=[-0.05674507980728292, -0.0527310420933204],
        type='linear'
    ),
    yaxis=dict(
        autorange=False,
        range=[1.2876210047544652, 1.2977732997811402],
        type='linear'
    ),
    height=550,
    width=1137
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-text-annotationsplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-text-annotationsplot/", width="100%", height="750px", frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-text-annotationsplot/code", width="100%", height=500, frameBorder="0")
```

#### Reference
See https://plot.ly/python/reference/#layout-annotations for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'text-and-annotations.ipynb', 'python/text-and-annotations/', 'Text and Annotations',
    'How to add text labels and annotations to plots in python.',
    title = 'Text and Annotations | plotly',
    thumbnail='thumbnail/annotations.jpg', language='python',
    page_type='example_index', has_thumbnail='false', display_as='style_opt', order=1, 
    ipynb='~notebook_demo/204', uses_plotly_offline=False)
```