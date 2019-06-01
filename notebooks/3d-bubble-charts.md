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
    description: How to make 3D Bubble Charts in Python with Plotly. Three examples
      of 3D Bubble Charts.
    display_as: 3d_charts
    has_thumbnail: true
    ipynb: ~notebook_demo/62
    language: python
    layout: user-guide
    name: 3D Bubble Charts
    order: 2
    page_type: u-guide
    permalink: python/3d-bubble-charts/
    thumbnail: thumbnail/3dbubble.jpg
    title: Python 3D Bubble Charts | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Simple Bubble Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

# Get Data: this ex will only use part of it (i.e. rows 750-1500)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

trace1 = go.Scatter3d(
    x=df['year'][750:1500],
    y=df['continent'][750:1500],
    z=df['pop'][750:1500],
    text=df['country'][750:1500],
    mode='markers',
    marker=dict(
        sizemode='diameter',
        sizeref=750,
        size=df['gdpPercap'][750:1500],
        color = df['lifeExp'][750:1500],
        colorscale = 'Viridis',
        colorbar = dict(title = 'Life<br>Expectancy'),
        line=dict(color='rgb(140, 140, 170)')
    )
)

data=[trace1]

layout=go.Layout(height=800, width=800, title='Examining Population and Life Expectancy Over Time')

fig=go.Figure(data=data, layout=layout)
py.iplot(fig, filename='3DBubble')
```

#### Bubble Chart Sized by a Variable
Plot planets' distance from sun, density, and gravity with bubble size based on planet size

```python
import plotly.plotly as py
import plotly.graph_objs as go

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planet_colors = ['rgb(135, 135, 125)', 'rgb(210, 50, 0)', 'rgb(50, 90, 255)',
                 'rgb(178, 0, 0)', 'rgb(235, 235, 210)', 'rgb(235, 205, 130)',
                 'rgb(55, 255, 217)', 'rgb(38, 0, 171)', 'rgb(255, 255, 255)']
distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
density = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638, 2095]
gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
planet_diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]

# Create trace, sizing bubbles by planet diameter
trace1 = go.Scatter3d(
    x = distance_from_sun,
    y = density,
    z = gravity,
    text = planets,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 750, # info on sizeref: https://plot.ly/python/reference/#scatter-marker-sizeref
        size = planet_diameter,
        color = planet_colors,
        )  
)
data=[trace1]

layout=go.Layout(width=800, height=800, title = 'Planets!',
              scene = dict(xaxis=dict(title='Distance from Sun',
                                      titlefont=dict(color='Orange')),
                            yaxis=dict(title='Density',
                                       titlefont=dict(color='rgb(220, 220, 220)')),
                            zaxis=dict(title='Gravity',
                                       titlefont=dict(color='rgb(220, 220, 220)')),
                            bgcolor = 'rgb(20, 24, 54)'
                           )
             )

fig=go.Figure(data=data, layout=layout)
py.iplot(fig, filename='solar_system_planet_size')
```

#### Edit the Colorbar
Plot planets' distance from sun, density, and gravity with bubble size based on planet size

```python
import plotly.plotly as py
import plotly.graph_objs as go

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
temperatures = [167, 464, 15, -20, -65, -110, -140, -195, -200, -225]
distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
density = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638, 2095]
gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
planet_diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]

# Create trace, sizing bubbles by planet diameter
trace1 = go.Scatter3d(
    x = distance_from_sun,
    y = density,
    z = gravity,
    text = planets,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 750, # info on sizeref: https://plot.ly/python/reference/#scatter-marker-sizeref
        size = planet_diameter,
        color = temperatures,
        colorbar = dict(title = 'Mean<br>Temperature'),
        colorscale=[[0, 'rgb(5, 10, 172)'], [.3, 'rgb(255, 255, 255)'], [1, 'rgb(178, 10, 28)']]
        )  
)
data=[trace1]

layout=go.Layout(width=800, height=800, title = 'Planets!!',
            scene = dict(xaxis=dict(title='Distance from Sun',
                                    titlefont=dict(color='Orange')),
                            yaxis=dict(title='Density',
                                       titlefont=dict(color='rgb(220, 220, 220)')),
                            zaxis=dict(title='Gravity',
                                       titlefont=dict(color='rgb(220, 220, 220)')),
                            bgcolor = 'rgb(20, 24, 54)'
                           )
             )

fig=go.Figure(data=data, layout=layout)
py.iplot(fig, filename='solar_system_planet_temp')
```

#### Reference
See https://plot.ly/python/reference/#scatter3d and https://plot.ly/python/reference/#scatter-marker-sizeref <br>for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
    
import publisher
publisher.publish(
    '3dbubble.ipynb', 'python/3d-bubble-charts/', 'Python 3D Bubble Charts',
    'How to make 3D Bubble Charts in Python with Plotly. '
    'Three examples of 3D Bubble Charts.',
    title = 'Python 3D Bubble Charts | plotly',
    name = '3D Bubble Charts',
    has_thumbnail='true', thumbnail='thumbnail/3dbubble.jpg', 
    language='python', display_as='3d_charts', order=2,
    ipynb= '~notebook_demo/62')
```

```python

```