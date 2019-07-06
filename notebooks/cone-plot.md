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
    description: How to make 3D Cone plots in Python with Plotly.
    display_as: 3d_charts
    has_thumbnail: true
    ipynb: ~notebook_demo/206
    language: python
    layout: user-guide
    name: 3D Cone Plots
    order: 20
    page_type: u-guide
    permalink: python/cone-plot/
    redirect_from: python/3d-cone/
    thumbnail: thumbnail/3dcone.png
    title: 3D Cone Plots | Plotly
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

### Basic 3D Cone

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [{
    'type': 'cone',
    'x': [1], 'y': [1], 'z': [1],
    'u': [1], 'v': [1], 'w': [0]
}]

layout = {
    'scene': {
      'camera': {
        'eye': {'x': -0.76, 'y': 1.8, 'z': 0.92}
      }
    }
}

fig = {"data": data, "layout": layout}
py.iplot(fig, filename='cone-basic', validate=False)
```

### Multiple 3D Cones

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [{
    "type": "cone",
    "x": [1, 2, 3],
    "y": [1, 2, 3],
    "z": [1, 2, 3],
    "u": [1, 0, 0],
    "v": [0, 3, 0],
    "w": [0, 0, 2],
    "sizemode": "absolute",
    "sizeref": 2,
    "anchor": "tip",
    "colorbar": {
    "x": 0,
    "xanchor": "right",
    "side": "left"
    }
}]

layout = {
    "scene": {
      "domain": {"x": [0, 1]},
      "camera": {
        "eye": {"x": -1.57, "y": 1.36, "z": 0.58}
      }
    }
}

fig = {"data": data, "layout": layout}
py.iplot(fig, filename="cone-mulitple", validate=False)
```

### 3D Cone Lighting

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [{
      "type": "cone",
      "name": "base",
      "x": [1, 1, 1],
      "y": [1, 2, 3],
      "z": [1, 1, 1],
      "u": [1, 2, 3],
      "v": [1, 1, 2],
      "w": [4, 4, 1],
      "hoverinfo": "u+v+w+name",
      "showscale": False
    },{
      "type": "cone",
      "name": "opacity:0.3",
      "x": [2, 2, 2],
      "y": [1, 2, 3],
      "z": [1, 1, 1],
      "u": [1, 2, 3],
      "v": [1, 1, 2],
      "w": [4, 4, 1],
      "hoverinfo": "u+v+w+name",
      "showscale": False,
      "opacity": 0.3
    },{
      "type": "cone",
      "name": "lighting.ambient:0.3",
      "x": [3, 3, 3],
      "y": [1, 2, 3],
      "z": [1, 1, 1],
      "u": [1, 2, 3],
      "v": [1, 1, 2],
      "w": [4, 4, 1],
      "hoverinfo": "u+v+w+name",
      "showscale": False,
      "lighting": {"ambient": 0.3}
    },{
      "type": "cone",
      "name": "lighting.diffuse:0.3",
      "x": [4, 4, 4],
      "y": [1, 2, 3],
      "z": [1, 1, 1],
      "u": [1, 2, 3],
      "v": [1, 1, 2],
      "w": [4, 4, 1],
      "hoverinfo": "u+v+w+name",
      "showscale": False,
      "lighting": {"diffuse": 0.3}
    },{
      "type": "cone",
      "name": "lighting.specular:2",
      "x": [5, 5, 5],
      "y": [1, 2, 3],
      "z": [1, 1, 1],
      "u": [1, 2, 3],
      "v": [1, 1, 2],
      "w": [4, 4, 1],
      "hoverinfo": "u+v+w+name",
      "showscale": False,
      "lighting": {"specular": 2}
    },{
      "type": "cone",
      "name": "lighting.roughness:1",
      "x": [6, 6, 6],
      "y": [1, 2, 3],
      "z": [1, 1, 1],
      "u": [1, 2, 3],
      "v": [1, 1, 2],
      "w": [4, 4, 1],
      "hoverinfo": "u+v+w+name",
      "showscale": False,
      "lighting": {"roughness": 1}
    },{
      "type": "cone",
      "name": "lighting.fresnel:2",
      "x": [7, 7, 7],
      "y": [1, 2, 3],
      "z": [1, 1, 1],
      "u": [1, 2, 3],
      "v": [1, 1, 2],
      "w": [4, 4, 1],
      "hoverinfo": "u+v+w+name",
      "showscale": False,
      "lighting": {"fresnel": 2}
    },{
      "type": "cone",
      "name": "lighting.position x:0,y:0,z:1e5",
      "x": [8, 8, 8],
      "y": [1, 2, 3],
      "z": [1, 1, 1],
      "u": [1, 2, 3],
      "v": [1, 1, 2],
      "w": [4, 4, 1],
      "hoverinfo": "u+v+w+name",
      "showscale": False,
      "lightposition": {"x": 0, "y": 0, "z": 1e5}
    }
]

layout = {
    "scene": {
      "aspectmode": "data",
      "camera": {
        "eye": {"x": 0.05, "y": -2.6, "z": 2}
      }
    },
    "margin": {"t": 0, "b": 0, "l": 0, "r": 0}
}

fig = {"data": data, "layout": layout}
py.iplot(fig, filename="cone-lighting", validate=False)
```

### 3D Cone Vortex

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/vortex.csv")

data = [{
    "type": "cone",
    "x": df['x'],
    "y": df['y'],
    "z": df['z'],
    "u": df['u'],
    "v": df['v'],
    "w": df['w'],
    "colorscale": 'Blues',
    "sizemode": "absolute",
    "sizeref": 40
}]

layout = {
    "scene": {
        "aspectratio": {"x": 1, "y": 1, "z": 0.8},
        "camera": {
            "eye": {"x": 1.2, "y": 1.2, "z": 0.6}
        }
    }
}

fig = {"data": data, "layout": layout}
py.iplot(fig, filename="cone-vortex", validate=False)
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'cones.ipynb', 'python/cone-plot/', '3D Cone Plots',
    'How to make 3D Cone plots in Python with Plotly.',
    title = '3D Cone Plots | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/3dcone.png',
    language='python',
    # page_type='example_index', // note this is only if you want the tutorial to appear on the main page: plot.ly/python
    display_as='3d_charts', order=20, ipynb='~notebook_demo/206',
    redirect_from='python/3d-cone/',
    uses_plotly_offline=False)
```

```python

```