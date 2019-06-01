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
    description: How to Control the Camera in your 3D Charts in Python with Plotly.
    display_as: layout_opts
    has_thumbnail: true
    ipynb: ~notebook_demo/78
    language: python
    layout: user-guide
    name: 3D Camera Controls
    order: 18
    permalink: python/3d-camera-controls/
    thumbnail: thumbnail/3d-camera-controls.jpg
    title: Python 3D Camera Controls | plotly
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
```

<!-- #region {"deletable": true, "editable": true} -->
#### Import Data
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

data = [
    go.Surface(
        z=z_data.as_matrix()
    )
]
layout = go.Layout(
    title='Mt Bruno Elevation',
    autosize=False,
    width=600,
    height=600,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Default Params
The camera position is determined by three vectors: *up*, *center*, *eye*.

The up vector determines the up direction on the page. The default is $(x=0, y=0, z=1)$, that is, the z-axis points up.

The center vector determines the translation about the center of the scene. By default, there is no translation: the center vector is $(x=0, y=0, z=0)$.

The eye vector determines the camera view point about the origin. The default is $(x=1.25, y=1.25, z=1.25)$. 
<!-- #endregion -->

```python deletable=true editable=true
name = 'default'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1.25, y=1.25, z=1.25)
)

py.iplot(fig, validate=False, filename=name)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Lower the View Point
<!-- #endregion -->

```python deletable=true editable=true
name = 'eye = (x:2, y:2, z:0.1)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=2, y=2, z=0.1)
)

fig['layout'].update(
    scene=dict(camera=camera),
    title=name
)
py.iplot(fig, validate=False, filename=name)
```

<!-- #region {"deletable": true, "editable": true} -->
#### X-Z plane
<!-- #endregion -->

```python deletable=true editable=true
name = 'eye = (x:0.1, y:2.5, z:0.1)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0.1, y=2.5, z=0.1)
)

fig['layout'].update(
    scene=dict(camera=camera),
    title=name
)
py.iplot(fig, validate=False, filename=name)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Y-Z plane
<!-- #endregion -->

```python deletable=true editable=true
name = 'eye = (x:2.5, y:0.1, z:0.1)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=2.5, y=0.1, z=0.1)
)

fig['layout'].update(
    scene=dict(camera=camera),
    title=name
)
py.iplot(fig, validate=False, filename=name)
```

<!-- #region {"deletable": true, "editable": true} -->
#### View from Above
<!-- #endregion -->

```python deletable=true editable=true
name = 'eye = (x:0.1, y:0.1, z:2.5)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0.1, y=0.1, z=2.5)
)

fig['layout'].update(
    scene=dict(camera=camera),
    title=name
)
py.iplot(fig, validate=False, filename=name)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Zooming In
... by reducing the norm the eye vector.
<!-- #endregion -->

```python deletable=true editable=true
name = 'eye = (x:0.1, y:0.1, z:1)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0.1, y=0.1, z=1)
)

fig['layout'].update(
    scene=dict(camera=camera),
    title=name
)
py.iplot(fig, validate=False, filename=name)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
See https://plot.ly/python/reference/#layout-scene-camera for more information and chart attribute options!
<!-- #endregion -->

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher

publisher.publish(
    '3d-camera-controls.ipynb', 'python/3d-camera-controls/', 'Python 3D Camera Controls | plotly',
    'How to Control the Camera in your 3D Charts in Python with Plotly.',
    title= 'Python 3D Camera Controls | plotly',
    name = '3D Camera Controls',
    has_thumbnail='true', thumbnail='thumbnail/3d-camera-controls.jpg', 
    language='python', 
    display_as='layout_opts', order=18,
    ipynb= '~notebook_demo/78')
```

```python deletable=true editable=true

```