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
    description: How to Control the Camera in your 3D Charts in Python with Plotly.
    display_as: 3d_charts
    has_thumbnail: true
    ipynb: ~notebook_demo/78
    language: python
    layout: user-guide
    name: 3D Camera Controls
    order: 0.108
    permalink: python/3d-camera-controls/
    thumbnail: thumbnail/3d-camera-controls.jpg
    title: Python 3D Camera Controls | plotly
---

#### Import Data

```python
import plotly.graph_objects as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
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

fig.show()
```

#### Default Params
The camera position is determined by three vectors: *up*, *center*, *eye*.

The up vector determines the up direction on the page. The default is $(x=0, y=0, z=1)$, that is, the z-axis points up.

The center vector determines the translation about the center of the scene. By default, there is no translation: the center vector is $(x=0, y=0, z=0)$.

The eye vector determines the camera view point about the origin. The default is $(x=1.25, y=1.25, z=1.25)$.

```python
name = 'default'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1.25, y=1.25, z=1.25)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### Lower the View Point

```python
name = 'eye = (x:2, y:2, z:0.1)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=2, y=2, z=0.1)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### X-Z plane

```python
name = 'eye = (x:0.1, y:2.5, z:0.1)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0.1, y=2.5, z=0.1)
)


fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### X-Z plane, tilt camera

```python
name = 'eye = (x:0.1, y:2.5, z:0.1), point along x'
camera = dict(
    up=dict(x=1, y=0, z=0),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0.1, y=2.5, z=0.1)
)


fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### Y-Z plane

```python
name = 'eye = (x:2.5, y:0.1, z:0.1)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=2.5, y=0.1, z=0.1)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### View from Above

```python
name = 'eye = (x:0.1, y:0.1, z:2.5)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0.1, y=0.1, z=2.5)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### Zooming In
... by reducing the norm the eye vector.

```python
name = 'eye = (x:0.1, y:0.1, z:1)'
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0.1, y=0.1, z=1)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### Reference


See https://plot.ly/python/reference/#layout-scene-camera for more information and chart attribute options!
