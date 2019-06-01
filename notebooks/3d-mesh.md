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
    description: How to make 3D Mesh Plots
    display_as: 3d_charts
    has_thumbnail: true
    ipynb: ~notebook_demo/67
    language: python
    layout: user-guide
    name: 3D Mesh Plots
    order: 7
    page_type: u-guide
    permalink: python/3d-mesh/
    thumbnail: thumbnail/3d-mesh.jpg
    title: 3D Mesh Plots in Python | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



#### Version Check
Note: 3D Mesh are available in version <b>1.10.0+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

### Simple 3D Mesh example ###


We are using data present in a separate text file. The file can be downloaded from [Plotly's dataset repo](https://raw.githubusercontent.com/plotly/datasets/master/mesh_dataset.txt).

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

pts=np.loadtxt('mesh_dataset.txt')
x,y,z=zip(*pts)

trace = go.Mesh3d(x=x,y=y,z=z,color='#FFB6C1',opacity=0.50)
py.iplot([trace])
```

### 3D Mesh example with Alphahull


Alphahull sets shape of mesh. If the value is -1 then Delaunay triangulation is used. If >0 then the alpha-shape algorithm is used. The default value is -1.

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

pts=np.loadtxt('mesh_dataset.txt')
x,y,z=zip(*pts)

trace = go.Mesh3d(x=x,y=y,z=z,
                   alphahull=5,
                   opacity=0.4,
                   color='#00FFFF')
py.iplot([trace])
```

### Mesh Tetrahedron

```python
data = [
    go.Mesh3d(
        x = [0, 1, 2, 0],
        y = [0, 0, 1, 2],
        z = [0, 2, 0, 1],
        colorbar = go.ColorBar(
            title='z'
        ),
        colorscale = [[0, 'rgb(255, 0, 0)'], 
                      [0.5, 'rgb(0, 255, 0)'], 
                      [1, 'rgb(0, 0, 255)']],
        intensity = [0, 0.33, 0.66, 1],
        i = [0, 0, 0, 1],
        j = [1, 2, 3, 2],
        k = [2, 3, 1, 3],
        name = 'y',
        showscale = True
    )
]
layout = go.Layout(
    xaxis=go.XAxis(
        title='x'
    ),
    yaxis=go.YAxis(
        title='y'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='3d-mesh-tetrahedron-python')
```

### Mesh Cube

```python
data = [
    go.Mesh3d(
        x = [0, 0, 1, 1, 0, 0, 1, 1],
        y = [0, 1, 1, 0, 0, 1, 1, 0],
        z = [0, 0, 0, 0, 1, 1, 1, 1],
        colorbar = go.ColorBar(
            title='z'
        ),
        colorscale = [[0, 'rgb(255, 0, 255)'],
                    [0.5, 'rgb(0, 255, 0)'], 
                      [1, 'rgb(0, 0, 255)']],
        intensity = [0, 0.142857142857143, 0.285714285714286, 
                     0.428571428571429, 0.571428571428571, 
                     0.714285714285714, 0.857142857142857, 1],
        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        name='y',
        showscale=True
    )
]
layout = go.Layout(
    xaxis=go.XAxis(
        title='x'
    ),
    yaxis=go.YAxis(
        title='y'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='3d-mesh-cube-python')
```

## Reference
See https://plot.ly/python/reference/#mesh3d for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher

publisher.publish(
    'mesh-3d.ipynb', 'python/3d-mesh/', 'Python 3D Mesh Plots | Plotly',
    'How to make 3D Mesh Plots',
    title= '3D Mesh Plots in Python | plotly',
    name = '3D Mesh Plots',
    has_thumbnail='true', thumbnail='thumbnail/3d-mesh.jpg', 
    language='python',
    display_as='3d_charts', order=7,
    ipynb= '~notebook_demo/67') 
```

```python

```