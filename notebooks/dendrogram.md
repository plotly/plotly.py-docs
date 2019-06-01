---
jupyter:
  jupytext:
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
    description: How to make a dendrogram in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/262
    language: python
    layout: user-guide
    name: Dendrograms
    order: 6
    page_type: u-guide
    permalink: python/dendrogram/
    thumbnail: thumbnail/dendrogram.jpg
    title: Dendrograms | Plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Note: Dendrograms are available in version 1.8.7+.
Run `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

##### Basic Dendrogram

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

X = np.random.rand(15, 15)
dendro = ff.create_dendrogram(X)
dendro['layout'].update({'width':800, 'height':500})
py.iplot(dendro, filename='simple_dendrogram')
```

##### Set Color Threshold

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

X = np.random.rand(15, 15)
dendro = ff.create_dendrogram(X, color_threshold=1.5)
dendro['layout'].update({'width':800, 'height':500})
py.iplot(dendro, filename='simple_dendrogram_with_color_threshold')
```

##### Set Orientation and Add Labels

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

X = np.random.rand(10, 10)
names = ['Jack', 'Oxana', 'John', 'Chelsea', 'Mark', 'Alice', 'Charlie', 'Rob', 'Lisa', 'Lily']
fig = ff.create_dendrogram(X, orientation='left', labels=names)
fig['layout'].update({'width':800, 'height':800})
py.iplot(fig, filename='dendrogram_with_labels')
```

##### Plot a Dendrogram with a Heatmap

```python
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np
from scipy.spatial.distance import pdist, squareform


# get data
data = np.genfromtxt("http://files.figshare.com/2133304/ExpRawData_E_TABM_84_A_AFFY_44.tab",
                     names=True,usecols=tuple(range(1,30)),dtype=float, delimiter="\t")
data_array = data.view((np.float, len(data.dtype.names)))
data_array = data_array.transpose()
labels = data.dtype.names

# Initialize figure by creating upper dendrogram
figure = ff.create_dendrogram(data_array, orientation='bottom', labels=labels)
for i in range(len(figure['data'])):
    figure['data'][i]['yaxis'] = 'y2'

# Create Side Dendrogram
dendro_side = ff.create_dendrogram(data_array, orientation='right')
for i in range(len(dendro_side['data'])):
    dendro_side['data'][i]['xaxis'] = 'x2'

# Add Side Dendrogram Data to Figure
for data in dendro_side['data']:
    figure.add_trace(data)

# Create Heatmap
dendro_leaves = dendro_side['layout']['yaxis']['ticktext']
dendro_leaves = list(map(int, dendro_leaves))
data_dist = pdist(data_array)
heat_data = squareform(data_dist)
heat_data = heat_data[dendro_leaves,:]
heat_data = heat_data[:,dendro_leaves]

heatmap = [
    go.Heatmap(
        x = dendro_leaves, 
        y = dendro_leaves,
        z = heat_data,    
        colorscale = 'Blues'
    )
]

heatmap[0]['x'] = figure['layout']['xaxis']['tickvals']
heatmap[0]['y'] = dendro_side['layout']['yaxis']['tickvals']

# Add Heatmap Data to Figure
for data in heatmap:
    figure.add_trace(data)

# Edit Layout
figure['layout'].update({'width':800, 'height':800,
                         'showlegend':False, 'hovermode': 'closest',
                         })
# Edit xaxis
figure['layout']['xaxis'].update({'domain': [.15, 1],
                                  'mirror': False,
                                  'showgrid': False,
                                  'showline': False,
                                  'zeroline': False,
                                  'ticks':""})
# Edit xaxis2
figure['layout'].update({'xaxis2': {'domain': [0, .15],
                                   'mirror': False,
                                   'showgrid': False,
                                   'showline': False,
                                   'zeroline': False,
                                   'showticklabels': False,
                                   'ticks':""}})

# Edit yaxis
figure['layout']['yaxis'].update({'domain': [0, .85],
                                  'mirror': False,
                                  'showgrid': False,
                                  'showline': False,
                                  'zeroline': False,
                                  'showticklabels': False,
                                  'ticks': ""})
# Edit yaxis2
figure['layout'].update({'yaxis2':{'domain':[.825, .975],
                                   'mirror': False,
                                   'showgrid': False,
                                   'showline': False,
                                   'zeroline': False,
                                   'showticklabels': False,
                                   'ticks':""}})

# Plot!
py.iplot(figure, filename='dendrogram_with_heatmap')
```

```python
dendro_side['layout']['xaxis']
```

### Reference

```python
help(ff.create_dendrogram)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'dendrograms.ipynb', 'python/dendrogram/', 'Python Dendrograms',
    'How to make a dendrogram in Python with Plotly. ',
    name = 'Dendrograms',
    title = "Dendrograms | Plotly",
    thumbnail='thumbnail/dendrogram.jpg', language='python',
    has_thumbnail='true', display_as='scientific', order=6,
    ipynb= '~notebook_demo/262')
```

```python

```