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
    description: How to make 3D Isosurface Plots in Python with Plotly.
    display_as: 3d_charts
    has_thumbnail: true
    ipynb: ~notebook_demo/272
    language: python
    layout: user-guide
    name: 3D Isosurface Plots
    order: 12.1
    page_type: u-guide
    permalink: python/3d-isosurface-plots/
    redirect_from: python/isosurfaces-with-marching-cubes/
    thumbnail: thumbnail/isosurface.jpg
    title: Python 3D Isosurface Plots | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Basic Isosurface

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Isosurface(
    x=[0,0,0,0,1,1,1,1],
    y=[1,0,1,0,1,0,1,0],
    z=[1,1,0,0,1,1,0,0],
    value=[1,2,3,4,5,6,7,8],
    isomin=2,
    isomax=6
)]

py.iplot(data, filename='basic-isosurface-trace')
```

#### Isosurface with Addtional Slices

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

f = lambda x, y, z:  81*(x**3 + y**3 + z**3) - 189*(x**2*y + x**2*z + y**2*x +y**2*z + z**2*x + z**2*y) +\
                     54*(x*y*z) + 126*(x*y + x*z + y*z) - 9*(x**2 + y**2 + z**2) - 9*(x + y + z) + 1

a = 1
X, Y, Z = np.mgrid[-a:a:25j, -a:a:25j, -a:a:25j]

data = [go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=f(X, Y, Z).flatten(),
    isomin=-100,
    isomax=100,
    surface=dict(show=True,count=1, fill=0.8),
    slices=go.isosurface.Slices(
        z=go.isosurface.slices.Z(
            show = True,
            locations=[-0.3, 0.5])
    ),
    caps=go.isosurface.Caps(
        z=dict(show=False),
        x=dict(show=False),
        y=dict(show=False)
    ),
)]

layout = go.Layout(
    margin=dict(t=0, l=0, b=0),
    scene=dict(
        camera=dict(
            eye=dict(
                x=1.86,
                y=0.61,
                z=0.98
            )
        )
    )
)

fig = go.Figure(data, layout)

py.iplot(fig, config=dict(showSendToCloud=True), filename='isosurface-with-slices')
```

#### Multiple Isosurfaces with Caps

```python
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.io as pio

import numpy as np

f = lambda x, y, z:  81*(x**3 + y**3 + z**3) - 189*(x**2*y + x**2*z + y**2*x +y**2*z + z**2*x + z**2*y) +\
                     54*(x*y*z) + 126*(x*y + x*z + y*z) - 9*(x**2 + y**2 + z**2) - 9*(x + y + z) + 1

a = 1
X, Y, Z = np.mgrid[-a:a:25j, -a:a:25j, -a:a:25j]

data = [go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=f(X, Y, Z).flatten(),
    isomin=-10,
    isomax=10,
    surface=dict(show=True,count=4, fill=0.8, pattern='odd'),
    caps=go.isosurface.Caps(
        z=dict(show=True),
        x=dict(show=True),
        y=dict(show=True)
    ),
)]

layout = go.Layout(
    margin=dict(t=0, l=0, b=0),
    template=pio.templates['plotly'],
    scene=dict(
        camera=dict(
            eye=dict(
                x=1.86,
                y=0.61,
                z=0.98
            )
        )
    )
)

fig = go.Figure(data, layout)

py.iplot(fig, config=dict(showSendToCloud=True), filename='multiple-isosurface-with-caps')
```

#### Reference
See https://plot.ly/python/reference/#isosurface for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'isosurfaces.ipynb', 'python/3d-isosurface-plots/', 'Iso Surface',
    'How to make 3D Isosurface Plots in Python with Plotly.',
    title = 'Python 3D Isosurface Plots | plotly',
    name = '3D Isosurface Plots',
    has_thumbnail='true', thumbnail='thumbnail/isosurface.jpg',
    redirect_from='python/isosurfaces-with-marching-cubes/',
    language='python',
    display_as='3d_charts', order=12.1,
    ipynb= '~notebook_demo/272')
```

```python

```
