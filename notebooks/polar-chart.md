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
    description: How to makepolar charts in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/200
    language: python
    layout: user-guide
    name: Polar Charts
    order: 29
    page_type: u-guide
    permalink: python/polar-chart/
    thumbnail: thumbnail/polar.gif
    title: Polar Charts | Plotly
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

#### Legacy Plots


Looking for the old polar chart docs? See [legacy polar charts](https://plot.ly/python/legacy-polar-chart/)


#### Basic Polar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatterpolar(
        r = [0.5,1,2,2.5,3,4],
        theta = [35,70,120,155,205,240],
        mode = 'markers',
        marker = dict(
            color = 'peru'
        )
    )
]

layout = go.Layout(
    showlegend = False
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename = 'polar-basic')
```

#### Line Polar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/polar_dataset.csv")

data = [
    go.Scatterpolar(
        r = df['x1'],
        theta = df['y'],
        mode = 'lines',
        name = 'Figure8',
        line =  dict(
            color = 'peru'
        )   
    ),
    go.Scatterpolar(
        r = df['x2'],
        theta = df['y'],
        mode = 'lines',
        name = 'Cardioid',
        line =  dict(
            color = 'darkviolet'
        )   
    ),
    go.Scatterpolar(
        r = df['x3'],
        theta = df['y'],
        mode = 'lines',
        name = 'Hypercardioid',
        line =  dict(
            color = 'deepskyblue'
        )   
    ),
    go.Scatterpolar(
        r = df['x4'],
        theta = df['y'],
        mode = 'lines',
        name = 'orangered',
        line =  dict(
            color = 'orangered'
        )   
    ),
    go.Scatterpolar(
        r = df['x5'],
        theta = df['y'],
        mode = 'lines',
        name = 'Supercardioid',
        line =  dict(
            color = 'green'
        )   
    )
]

layout = go.Layout(
    title = 'Mic Patterns',
    font = dict(
        family = 'Arial, sans-serif;',
        size = 12,
        color = '#000'
    ),
    showlegend = False
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename = 'polar-line')
```

#### Area Polar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatterpolar(
        r = [0, 1.5, 1.5, 0, 2.5, 2.5, 0],
        theta = [0, 10, 25, 0, 205, 215, 0],
        mode = 'lines',
        fill = 'toself',
        fillcolor = '#709BFF',
        line =  dict(
            color = 'black'
        )   
    ),
    go.Scatterpolar(
        r = [0, 3.5, 3.5, 0],
        theta = [0, 55, 75, 0],
        mode = 'lines',
        fill = 'toself',
        fillcolor = '#E4FF87',
        line =  dict(
            color = 'black'
        )    
    ),
    go.Scatterpolar(
        r = [0, 4.5, 4.5, 0, 4.5, 4.5, 0],
        theta = [0, 100, 120, 0, 305, 320, 0],
        mode = 'lines',
        fill = 'toself',
        fillcolor = '#FFAA70',
        line =  dict(
            color = 'black'
        )  
    ),
    go.Scatterpolar(
        r = [0, 4, 4, 0],
        theta = [0, 165, 195, 0],
        mode = 'lines',
        fill = 'toself',
        fillcolor = '#FFDF70',
        line =  dict(
            color = 'black'
        )    
    ),
    go.Scatterpolar(
        r = [0, 3, 3, 0],
        theta = [0, 262.5, 277.5, 0],
        mode = 'lines',
        fill = 'toself',
        fillcolor = '#B6FFB4',
        line =  dict(
            color = 'black'
        )    
    )
]

layout = go.Layout(
    polar = dict(
        radialaxis = dict(
            visible = True,
            range = [0,5]
        )
    ),
    showlegend = False
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename = 'polar-area')
```

#### Categorical Polar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go


data = [
    go.Scatterpolar(
      name = "angular categories",
      r = [5, 4, 2, 4, 5],
      theta = ["a", "b", "c", "d", "a"],
      fill = "toself"
    ),
    go.Scatterpolar(
      name = "radial categories",
      r = ["a", "b", "c", "d", "b", "f", "a"],
      theta = [1, 4, 2, 1.5, 1.5, 6, 5],
      thetaunit = "radians",
      fill = "toself",
      subplot = "polar2"
    ),
    go.Scatterpolar(
      name = "angular categories (w/ categoryarray)",
      r = [5, 4, 2, 4, 5],
      theta = ["a", "b", "c", "d", "a"],
      fill = "toself",
      subplot = "polar3"
    ),
    go.Scatterpolar(
      name = "radial categories (w/ category descending)",
      r = ["a", "b", "c", "d", "b", "f", "a", "a"],
      theta = [45, 90, 180, 200, 300, 15, 20, 45],
      fill = "toself",
      subplot = "polar4"
    ),
    go.Scatterpolar(
      name = "angular categories (w/ extra category)",
      r = [5, 4, 2, 4, 5, 5],
      theta = ["b", "c", "d", "e", "a", "b"],
      fill = "toself"
    )
  ]
        
        
layout = go.Layout(
    polar = dict(
      domain = dict(
        x = [0, 0.46],
        y = [0.56, 1]
      ),
      radialaxis = dict(
        angle = 45
      ),
      angularaxis = dict(
        direction = "clockwise",
        period = 6
      )
    ),
    polar2 = dict(
      domain = dict(
        x = [0, 0.46],
        y = [0, 0.44]
      ),
      radialaxis = dict(
        angle = 180,
        tickangle = -180
      )
    ),
    polar3 = dict(
      domain = dict(
        x = [0.54, 1],
        y = [0.56, 1]
      ),
      sector = [150, 400],
      radialaxis = dict(
        angle = -45
      ),
      angularaxis = dict(
        categoryarray = ["d", "a", "c", "b"]
      )
    ),
    polar4 = dict(
      domain = dict(
        x = [0.54, 1],
        y = [0, 0.44]
      ),
      radialaxis = dict(
        categoryorder = "category descending"
      ),
      angularaxis = dict(
        thetaunit = "radians",
        dtick = 0.3141592653589793
      )
    )
)

fig = go.Figure(data=data,layout=layout)
py.iplot(fig, filename='polar-category')
```

#### Polar Chart Sector

```python
import plotly.plotly as py
import plotly.graph_objs as go



data = [
    go.Scatterpolar(
      mode = "lines+markers",
      r = [1,2,3,4,5],
      theta = [0,90,180,360,0],
      line = dict(
        color = "#ff66ab"
      ),
      marker = dict(
        color = "#8090c7",
        symbol = "square",
        size = 8
      ),
      subplot = "polar",
    ),
    go.Scatterpolar(
      mode = "lines+markers",
      r = [1,2,3,4,5],
      theta = [0,90,180,360,0],
      line = dict(
        color = "#ff66ab"
      ),
      marker = dict(
        color = "#8090c7",
        symbol = "square",
        size = 8
      ),
      subplot = "polar2"
    )
  ]


layout = go.Layout(
    showlegend = False,
    polar = dict(
      domain = dict(
        x = [0,0.4],
        y = [0,1]
      ),
      sector = [150,210],
      radialaxis = dict(
        tickfont = dict(
          size = 8
        )
      ),
      angularaxis = dict(
        tickfont = dict(
          size = 8
        )
      )
    ),
    polar2 = dict(
      domain = dict(
        x = [0.6,1],
        y = [0,1]
      ),
      radialaxis = dict(
        tickfont = dict(
          size = 8
        )
      ),
      angularaxis = dict(
        tickfont = dict(
          size = 8
        )
      )
    )
)


fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='polar-sector')
```

#### Polar Chart Directions

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatterpolar(
      mode = "lines+markers",
      r = [1,2,3,4,5],
      theta = [0,90,180,360,0],
      line = dict(
        color = "#ff66ab"
      ),
      marker = dict(
        color = "#8090c7",
        symbol = "square",
        size = 8
      ),
      subplot = "polar",
    ),
    go.Scatterpolar(
      mode = "lines+markers",
      r = [1,2,3,4,5],
      theta = [0,90,180,360,0],
      line = dict(
        color = "#ff66ab"
      ),
      marker = dict(
        color = "#8090c7",
        symbol = "square",
        size = 8
      ),
      subplot = "polar2"
    )
  ]


layout = go.Layout(
    showlegend = False,
    polar = dict(
      domain = dict(
        x = [0,0.4],
        y = [0,1]
      ),
      radialaxis = dict(
        tickfont = dict(
          size = 8
        )
      ),
      angularaxis = dict(
        tickfont = dict(
          size = 8
        ),
        rotation = 90,
        direction = "counterclockwise"
      )
    ),
    polar2 = dict(
      domain = dict(
        x = [0.6,1],
        y = [0,1]
      ),
      radialaxis = dict(
        tickfont = dict(
          size = 8
        )
      ),
      angularaxis = dict(
        tickfont = dict(
          size = 8
        ),
        rotation = 90,
        direction = "clockwise"
      ),
    )
)


fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='polar-directions')
```

#### Webgl Polar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/hobbs-pearson-trials.csv")


data = [
    go.Scatterpolargl(
      r = df.trial_1_r,
      theta = df.trial_1_theta,
      mode = "markers",
      name = "Trial 1",
      marker = dict(
        color = "rgb(27,158,119)",
        size = 15,
        line = dict(
          color = "white"
        ),
        opacity = 0.7
      )
    ),
    go.Scatterpolargl(
      r = df.trial_2_r,
      theta = df.trial_2_theta,
      mode = "markers",
      name = "Trial 2",
      marker = dict(
        color = "rgb(217,95,2)",
        size = 20,
        line = dict(
          color = "white"
        ),
        opacity = 0.7
      )
    ),
    go.Scatterpolargl(
      r = df.trial_3_r,
      theta = df.trial_3_theta,
      mode = "markers",
      name = "Trial 3",
      marker = dict(
        color = "rgb(117,112,179)",
        size = 12,
        line = dict(
          color = "white"
        ),
        opacity = 0.7
      )
    ),
    go.Scatterpolargl(
      r = df.trial_4_r,
      theta = df.trial_4_theta,
      mode = "markers",
      name = "Trial 4",
      marker = dict(
        color = "rgb(231,41,138)",
        size = 22,
        line = dict(
          color = "white"
        ),
        opacity = 0.7
      )
    ),
    go.Scatterpolargl(
      r = df.trial_5_r,
      theta = df.trial_5_theta,
      mode = "markers",
      name = "Trial 5",
      marker = dict(
        color = "rgb(102,166,30)",
        size = 19,
        line = dict(
          color = "white"
        ),
        opacity = 0.7
      )
    ),
    go.Scatterpolargl(
      r = df.trial_6_r,
      theta = df.trial_6_theta,
      mode = "markers",
      name = "Trial 6",
      marker = dict(
        color = "rgb(230,171,2)",
        size = 10,
        line = dict(
          color = "white"
        ),
        opacity = 0.7
      )
    )
]
    
layout = go.Layout(
    title = "Hobbs-Pearson Trials",
    font = dict(
      size = 15
    ),
    showlegend = False,
    polar = dict(
      bgcolor = "rgb(223, 223, 223)",
      angularaxis = dict(
        tickwidth = 2,
        linewidth = 3,
        layer = "below traces"
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = True,
        linewidth = 2,
        tickwidth = 2,
        gridcolor = "white",
        gridwidth = 2
      )
    ),
    paper_bgcolor = "rgb(223, 223, 223)"
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='polar-webgl')
```

#### Polar Chart Subplots

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatterpolar(
        r = [1, 2, 3],
        theta = [50, 100, 200],
        marker = dict(symbol = "square")
    ), 
    go.Scatterpolar(
        r = [1, 2, 3],
        theta = [1, 2, 3],
        thetaunit = "radians"
    ), 
    go.Scatterpolar(
        r = ["a", "b", "c", "b"],
        theta = ["D", "C", "B", "A"],
        subplot = "polar2"
    ), 
    go.Scatterpolar(
        r = [50, 300, 900],
        theta = [0, 90, 180],
        subplot = "polar3"
    ), 
    go.Scatterpolar(
        mode = "lines",
        r = [3, 3, 4, 3],
        theta = [0, 45, 90, 270],
        fill = "toself",
        subplot = "polar4"
    )
]
    
layout = go.Layout(
    polar = dict(
      domain = dict(
        x = [0, 0.46],
        y = [0.56, 1]
      ),
      radialaxis = dict(
        range = [1, 4]
      ),
      angularaxis = dict(
        thetaunit = "radians"
      )
    ),
    polar2 =dict(
      domain = dict(
        x = [0, 0.46],
        y = [0, 0.42]
      )
    ),
    polar3 = dict(
      domain = dict(
        x = [0.54, 1],
        y = [0.56, 1]
      ),
      radialaxis = dict(
        type = "log",
        tickangle = 45
      ),
      sector = [0, 180]
    ),
    polar4 = dict(
      domain = dict(
        x = [0.54, 1],
        y = [0, 0.44]
      ),
      radialaxis = dict(
          visible = False,
          range = [0, 6]
      )
    ),
    showlegend = False
)

fig = go.Figure(data=data,layout=layout)
py.iplot(fig, filename='polar-subplot')
```

#### Reference
See https://plot.ly/python/reference/#scatterpolar for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'polar.ipynb', 'python/polar-chart/', 'Polar Charts',
    'How to makepolar charts in Python with Plotly.',
    title = 'Polar Charts | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/polar.gif', 
    language='python', 
    # page_type='example_index', // note this is only if you want the tutorial to appear on the main page: plot.ly/python
    display_as='scientific', order=29, ipynb='~notebook_demo/200',
    )
```

```python

```