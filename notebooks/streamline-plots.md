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
    description: How to make a streamline plot in Python. A streamline plot displays
      vector field data.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/43
    language: python
    layout: user-guide
    name: Streamline Plots
    order: 13
    permalink: python/streamline-plots/
    thumbnail: thumbnail/streamline.jpg
    title: Python Streamline Plots | plotly
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
#### Basic Streamline Plot
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
Y, X = np.meshgrid(x, y)
u = -1 - X**2 + Y
v = 1 + X - Y**2

# Create streamline figure
fig = ff.create_streamline(x, y, u, v, arrow_scale=.1)
py.iplot(fig, filename='Streamline Plot Example')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Streamline and Source Point Plot
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go

import numpy as np

N = 50
x_start, x_end = -2.0, 2.0
y_start, y_end = -1.0, 1.0
x = np.linspace(x_start, x_end, N)
y = np.linspace(y_start, y_end, N)
X, Y = np.meshgrid(x, y)
source_strength = 5.0
x_source, y_source = -1.0, 0.0

# Compute the velocity field on the mesh grid
u = (source_strength/(2*np.pi) *
     (X-x_source)/((X-x_source)**2 + (Y-y_source)**2))
v = (source_strength/(2*np.pi) *
     (Y-y_source)/((X-x_source)**2 + (Y-y_source)**2))

# Create streamline figure
fig = ff.create_streamline(x, y, u, v,
                           name='streamline')

# Add source point
source_point = go.Scatter(x=[x_source], y=[y_source],
                          mode='markers',
                          marker=go.Marker(size=14),
                          name='source point')

# Add source point to figure
fig['data'].append(source_point)
py.iplot(fig, filename='streamline_source')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
<!-- #endregion -->

```python deletable=true editable=true
help(ff.create_streamline)
```

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'streamline.ipynb', 'python/streamline-plots/', 'Python Streamline Plots | plotly',
    'How to make a streamline plot in Python. A streamline plot displays vector field data. ',
    title = 'Python Streamline Plots | plotly',
    name = 'Streamline Plots',
    has_thumbnail='true', thumbnail='thumbnail/streamline.jpg',
    language='python',
    display_as='scientific', order=13,
    ipynb= '~notebook_demo/43')
```

```python deletable=true editable=true

```