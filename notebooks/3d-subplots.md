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
    description: 3D Subplots in Plotly
    display_as: multiple_axes
    has_thumbnail: true
    ipynb: ~notebook_demo/75
    language: python
    layout: user-guide
    name: 3D Subplots
    order: 4
    page_type: u-guide
    permalink: python/3d-subplots/
    thumbnail: thumbnail/3d-subplots.jpg
    title: 3D Subplots in Python | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Plotly's python package is updated frequently. Run pip install plotly --upgrade to use the latest version.

```python
import plotly 
plotly.__version__
```

#### 3D Surface Subplots

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

import numpy as np

x = np.linspace(-5, 80, 10)
y = np.linspace(-5, 60, 10)
xGrid, yGrid = np.meshgrid(y, x)
z = xGrid ** 3 + yGrid ** 3

scene = dict(
    xaxis=dict(
        gridcolor='rgb(255, 255, 255)',
        zerolinecolor='rgb(255, 255, 255)',
        showbackground=True,
        backgroundcolor='rgb(230, 230,230)'
    ),
    yaxis=dict(
        gridcolor='rgb(255, 255, 255)',
        zerolinecolor='rgb(255, 255, 255)',
        showbackground=True,
        backgroundcolor='rgb(230, 230,230)'
    ),
    zaxis=dict(
        gridcolor='rgb(255, 255, 255)',
        zerolinecolor='rgb(255, 255, 255)',
        showbackground=True,
        backgroundcolor='rgb(230, 230,230)'
    )
)

fig = tools.make_subplots(rows=2, cols=2,
                          specs=[[{'is_3d': True}, {'is_3d': True}],
                                 [{'is_3d': True}, {'is_3d': True}]])

# adding surfaces to subplots.
fig.append_trace(dict(type='surface', x=x, y=y, z=z, colorscale='Viridis',
                      scene='scene1', showscale=False), 1, 1)
fig.append_trace(dict(type='surface', x=x, y=y, z=z, colorscale='RdBu',
                      scene='scene2', showscale=False), 1, 2)
fig.append_trace(dict(type='surface', x=x, y=y, z=z, colorscale='YlOrRd',
                      scene='scene3', showscale=False), 2, 1)
fig.append_trace(dict(type='surface', x=x, y=y, z=z, colorscale='YlGnBu',
                      scene='scene4', showscale=False), 2, 2)

fig['layout'].update(title='subplots with different colorscales',
                     height=800, width=800)
fig['layout']['scene1'].update(scene)
fig['layout']['scene2'].update(scene)
fig['layout']['scene3'].update(scene)
fig['layout']['scene4'].update(scene)

py.iplot(fig, file_name='multiple_plots')
```

#### Reference


See https://plot.ly/python/subplots/ for more information regarding subplots!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#!pip install git+https://github.com/plotly/publisher.git --upgrade
    
import publisher
publisher.publish(
    '3d-subplots.ipynb', 'python/3d-subplots/', 'Python 3D Subplots | plotly',
    '3D Subplots in Plotly',
    title= '3D Subplots in Python | plotly',
    name = '3D Subplots',
    has_thumbnail='true', thumbnail='thumbnail/3d-subplots.jpg', 
    language='python', 
    display_as='multiple_axes', order=4,
    ipynb= '~notebook_demo/75')
```

```python

```