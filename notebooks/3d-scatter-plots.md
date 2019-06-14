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
    description: How to make 3D scatter plots in Python with Plotly.
    display_as: 3d_charts
    has_thumbnail: true
    ipynb: ~notebook_demo/61
    language: python
    layout: user-guide
    name: 3D Scatter Plots
    order: 1
    page_type: example_index
    permalink: python/3d-scatter-plots/
    thumbnail: thumbnail/3d-scatter.jpg
    title: 3D Python Scatter Plots | plotly
    v4upgrade: true
---

#### Basic 3D Scatter Plot

Like the [2D scatter plot](https://plot.ly/python/line-and-scatter/) `go.Scatter`, the 3D function `go.Scatter3d` plots individual data in three-dimensional space. 

```python
import plotly.graph_objs as go
import numpy as np

x0, y0, z0 = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 100).transpose()
trace0 = go.Scatter3d(
    x=x0,
    y=y0,
    z=z0,
    mode='markers',
    marker=dict(
        size=12,
        line_color='rgba(217, 217, 217, 0.14)',
        line_width=0.5,
        opacity=0.8
    )
)

x1, y1, z1 = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 100).transpose()
trace1 = go.Scatter3d(
    x=x1,
    y=y1,
    z=z1,
    mode='markers',
    marker=dict(
        color='gray',
        size=12,
        symbol='circle',
        line_color='lightgray',
        line_width=1,
        opacity=0.9
    )
)


fig = go.Figure(data=[trace0, trace1])
# tight layout
fig.update(layout_margin=dict(l=0, r=0, b=0, t=0))
fig.show()
```

#### 3D Scatter Plot with Colorscaling

```python
import plotly.graph_objs as go

import numpy as np

x, y, z = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 400).transpose()

trace = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        color=z,                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    )
)

fig = go.Figure(data=[trace])
# tight layout
fig.update(layout_margin=dict(l=0, r=0, b=0, t=0))
fig.show()
```

### Dash App


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-3dscatterplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-3dscatterplot/", width="100%", height="950px",frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-3dscatterplot/code", width="100%", height="500px",frameBorder="0")
```

#### Reference
See https://plot.ly/python/reference/#scatter3d for more information and chart attribute options!

