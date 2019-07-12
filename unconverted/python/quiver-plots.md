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
    description: How to make a quiver plot in Python. A quiver plot displays velocity
      vectors a arrows.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/42
    language: python
    layout: user-guide
    name: Quiver Plots
    order: 12
    permalink: python/quiver-plots/
    thumbnail: thumbnail/quiver-plot.jpg
    title: Python Quiver Plots | plotly
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Plotly's python API is updated frequesntly. Run pip install plotly --upgrade to update your Plotly version.
<!-- #endregion -->

```python deletable=true editable=true
import plotly
plotly.__version__
```

<!-- #region {"deletable": true, "editable": true} -->
#### Basic Quiver Plot
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u = np.cos(x)*y
v = np.sin(x)*y

fig = ff.create_quiver(x, y, u, v)
py.iplot(fig, filename='Quiver Plot Example')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Quiver Plot with Points
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go

import numpy as np

x,y = np.meshgrid(np.arange(-2, 2, .2),
                  np.arange(-2, 2, .25))
z = x*np.exp(-x**2 - y**2)
v, u = np.gradient(z, .2, .2)

# Create quiver figure
fig = ff.create_quiver(x, y, u, v,
                       scale=.25,
                       arrow_scale=.4,
                       name='quiver',
                       line=dict(width=1))

# Create points
points = go.Scatter(x=[-.7, .75], y=[0,0],
                    mode='markers',
                    marker=dict(size=12),
                    name='points')

# Add points to figure
fig['data'].append(points)

py.iplot(fig, filename='Quiver with Points')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
<!-- #endregion -->

```python deletable=true editable=true
help(ff.create_quiver)
```

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'quiver.ipynb', 'python/quiver-plots/', 'Python Quiver Plots | plotly',
    'How to make a quiver plot in Python. A quiver plot displays velocity vectors a arrows. ',
    title = 'Python Quiver Plots | plotly',
    name = 'Quiver Plots',
    has_thumbnail='true', thumbnail='thumbnail/quiver-plot.jpg',
    language='python',
    display_as='scientific', order=12,
    ipynb= '~notebook_demo/42')
```

```python deletable=true editable=true

```
