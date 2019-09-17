---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.3
  plotly:
    description: How to make 3D streamtube plots in Python with Plotly.
    display_as: 3d_charts
    has_thumbnail: true
    ipynb: ~notebook_demo/207
    language: python
    layout: user-guide
    name: 3D Streamtube Plots
    order: 21
    page_type: u-guide
    permalink: python/streamtube-plot/
    thumbnail: thumbnail/streamtube.jpg
    title: 3D Streamtube Plots | Plotly
---


### Introduction


In streamtube plots, attributes inlcude `x`, `y`, and `z`, which set the coordinates of the vector field, and `u`, `v`, and `w`, which sets the x, y, and z components of the vector field. Additionally, you can use `starts` to determine the streamtube's starting position. Lastly, `maxdisplayed` determines the maximum segments displayed in a streamtube.


### Basic Streamtube Plot

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/streamtube-basic.csv')

fig = go.Figure(data=go.Streamtube(
    x = df['x'],
    y = df['y'],
    z = df['z'],
    u = df['u'],
    v = df['v'],
    w = df['w'],
    sizeref = 0.5,
    colorscale = 'Blues',
    cmin = 0,
    cmax = 3
))


fig.update_layout(
    scene = dict(
      camera = dict(
        eye = dict(
          x = -0.7243612458865182,
          y = 1.9269804254717962,
          z = 0.6704828299861716
        )
      )
    )
)

fig.show()
```

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Streamtube(x=[0, 0, 0], y=[0, 1, 2], z=[0, 0, 0], u=[0, 0, 0], v=[1, 2, 3], w=[0, 0, 0]))
fig.show()
```

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Streamtube(x=[0, 1, 2], y=[0, 0, 0], z=[0, 0, 0], u=[1, 2, 3], v=[0, 0, 0], w=[0, 0, 0],
                                  starts=dict(x=[0],
                             y=[0],
                             z=[0],)))
fig.show()
```

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Streamtube(x=[0, 0, 0], y=[0, 0, 0], z=[0, 1, 2], u=[0, 0, 0], v=[0, 0, 0], w=[1, 2, 3],
                                  starts=dict(x=[0],
                             y=[0],
                             z=[0],)))
fig.show()
```

```python
import numpy as np
import plotly.graph_objects as go

x, y, z = np.mgrid[1:4:10j, 1:4:10j, 1:4:10j] 
u = 0.001 * x
v = 0.001 * y
w = 0.1 * z

sx=np.linspace(1, 4, 10, endpoint=True)
sx, sy=np.meshgrid(sx, sx)
sz=np.ones(sx.shape)


fig = go.Figure(data=go.Streamtube(
    x=x.ravel(), 
    y=y.ravel(), 
    z=z.ravel(), 
    u=u.ravel(), 
    v=v.ravel(), 
    w=w.ravel(), 
    starts=dict(x=sx.flatten(),
                             y=sy.flatten(),
                             z=sz.flatten()),
    hoverinfo='x+y+z+u+v+w+norm',
    #sizeref=0.3
))
fig.show()
```

```python
import numpy as np
import plotly.graph_objects as go

x, y, z = np.mgrid[1:4:10j, 1:4:10j, 1:4:10j] 
u = 0.000 * x**2
v = 0.00 * np.random.random(y.shape)
w = 0.1 * y

sx=np.linspace(1, 4, 10, endpoint=True)
sx, sy=np.meshgrid(sx, sx)
sz=np.ones(sx.shape)


fig = go.Figure(data=go.Streamtube(
    x=x.ravel(), 
    y=y.ravel(), 
    z=z.ravel(), 
    u=u.ravel(), 
    v=v.ravel(), 
    w=w.ravel(), 
    starts=dict(x=sx.flatten(),
                             y=sy.flatten(),
                             z=sz.flatten()),
    hoverinfo='x+y+z+u+v+w+norm',
    sizeref=0.3
))
fig.show()
```

```python
import numpy as np
import plotly.graph_objects as go

x, y, z = np.mgrid[1:2:4j, 1:2:4j, 1:2:4j]
u = np.zeros_like(x)
v = x.copy()
w = np.zeros_like(z)

fig = go.Figure(data=go.Streamtube(x=x.ravel(), y=y.ravel(), z=z.ravel(),
                                   u=u.ravel(), v=v.ravel(), w=w.ravel(),
                                   hoverinfo=['x', 'y']
))
fig.show()
```

```python
x.ravel(), y.ravel(), z.ravel(), v.ravel()
```

```python
v.ravel()
```

```
fig.data

```

```python
import numpy as np
import plotly.graph_objects as go

x, y, z = np.mgrid[-4:4:20j, -4:4:20j, 0:4:20j] 
r = np.sqrt(x ** 2 + y ** 2 + z ** 2 + 0.1) 
#u = 0.1 * y * np.sin(r) / r 
u = 0.005 * np.random.random(x.shape)
v = 0.005 * np.random.random(y.shape)
#v = -0.1 * x * np.sin(r) / r 
w = 0.1 * z

sx=np.linspace(-4, 4, 10)
sx, sy=np.meshgrid(sx, sx)
sz=np.ones(sx.shape)


fig = go.Figure(data=go.Streamtube(
    x=x.ravel(), y=y.ravel(), z=z.ravel(), u=u.ravel(), v=v.ravel(), w=w.ravel(), 
    starts=dict(x=sx.flatten(),
                             y=sy.flatten(),
                             z=sz.flatten()),
))
fig.show()
```

```python
df
```

### Starting Position and Segments

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/streamtube-wind.csv').drop(['Unnamed: 0'],axis=1)

fig = go.Figure(data=go.Streamtube(
    x = df['x'],
    y = df['y'],
    z = df['z'],
    u = df['u'],
    v = df['v'],
    w = df['w'],
    starts = dict(
        x = [80] * 16,
        y = [20,30,40,50] * 4,
        z = [0,0,0,0,5,5,5,5,10,10,10,10,15,15,15,15]
    ),
    sizeref = 0.3,
    colorscale = 'Portland',
    showscale = False,
    maxdisplayed = 3000
))

fig.update_layout(
    scene = dict(
        aspectratio = dict(
            x = 2,
            y = 1,
            z = 0.3
        )
    ),
    margin = dict(
        t = 20,
        b = 20,
        l = 20,
        r = 20
    )
)

fig.show()
```

```python
df
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

