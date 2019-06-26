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
    description: How to Color 3D Surface Plots in Python with Plotly.
    display_as: style_opt
    has_thumbnail: true
    ipynb: ~notebook_demo/76
    language: python
    layout: user-guide
    name: 3D Surface Coloring
    order: 7
    page_type: example_index
    permalink: python/3d-surface-coloring/
    thumbnail: thumbnail/3d-surface-color.jpg
    title: 3D Surface Coloring in Python | plotly
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

#### Color by Variable
By default, surface plots are colored by the `z` variable. Now, users have the option of setting the attribute `surfacecolor` to a variable to color by an independed variable.

```python
import plotly.plotly as py
from plotly import tools

import copy
import json
import math
import urllib2

# load ring cyclide data
response = urllib2.urlopen('https://plot.ly/~empet/2381.json')
data_file = response.read()
fig = json.loads(data_file)

data_original = fig['data'][0]        # trace0
data = copy.deepcopy(fig['data'])[0]  # trace1

lx = len(data['z'])
ly = len(data['z'][0])
out = []

def dist_origin(x, y, z):
    return math.sqrt((1.0 * x)**2 + (1.0 * y)**2 + (1.0 * z)**2)

for i in xrange(lx):
    temp = []
    for j in xrange(ly):
        temp.append(
            dist_origin(data['x'][i][j], data['y'][i][j], data['z'][i][j]))
    out.append(temp)

data['surfacecolor'] = out     # sets surface-color to distance from the origin

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
    ),
    cameraposition=[[0.2, 0.5, 0.5, 0.2], [0, 0, 0], 4.8]
)

fig = tools.make_subplots(rows=1, cols=2,
                          specs=[[{'is_3d': True}, {'is_3d': True}]])

# adding surfaces to subplots.
data_original['scene'] = 'scene1'
data_original['colorbar'] = dict(x=-0.07)

data['scene'] = 'scene2'
fig.append_trace(data_original, 1, 1)
fig.append_trace(data, 1, 2)

fig['layout'].update(title='Ring Cyclide',
                     height=800, width=950)
fig['layout']['scene1'].update(scene)
fig['layout']['scene2'].update(scene)
fig['layout']['annotations'] = [
    dict(x=0.1859205, y=0.95,
         xref='x', yref='y',
         text='4th Dim Prop. to z',
         showarrow=False),
    dict(x=0.858, y=0.95,
         xref='x', yref='y',
         text='4th Dim Prop. to Distance from Origin',
         showarrow=False)
]

py.iplot(fig, filename='surface-coloring')
```

#### Reference


See https://plot.ly/python/reference/#surface-surfacecolor for more information!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher

publisher.publish(
    '3d_surface_coloring.ipynb', 'python/3d-surface-coloring/', '3D Python Surface Coloring | plotly',
    'How to Color 3D Surface Plots in Python with Plotly.',
    title = '3D Surface Coloring in Python | plotly',
    name = '3D Surface Coloring',
    has_thumbnail='true', thumbnail='thumbnail/3d-surface-color.jpg',
    language='python', page_type='example_index',
    display_as='style_opt', order=7,
    ipynb= '~notebook_demo/76')
```

```python

```
