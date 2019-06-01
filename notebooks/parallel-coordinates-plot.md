---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernel_info:
    name: python2
  kernelspec:
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to make parallel coorindates plots in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/142
    language: python
    layout: user-guide
    name: Parallel Coordinates Plot
    order: 11.5
    page_type: u-guide
    permalink: python/parallel-coordinates-plot/
    thumbnail: thumbnail/parcoords.jpg
    title: Parallel Coordinates Plot | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Parallel Coordinates Plots are available in version <b>2.0.6+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

### Adding Dimensions

```python inputHidden=false outputHidden=false
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Parcoords(
        line = dict(color = 'blue'),
        dimensions = list([
            dict(range = [1,5],
                 constraintrange = [1,2],
                 label = 'A', values = [1,4]),
            dict(range = [1.5,5],
                 tickvals = [1.5,3,4.5],
                 label = 'B', values = [3,1.5]),
            dict(range = [1,5],
                 tickvals = [1,2,4,5],
                 label = 'C', values = [2,4],
                 ticktext = ['text 1', 'text 2', 'text 3', 'text 4']),
            dict(range = [1,5],
                 label = 'D', values = [4,2])
        ])
    )
]

py.iplot(data, filename = 'parcoord-dimensions')
```

Parallel coordinates are richly interactive by default. Drag the lines along the axes to filter regions and drag the axis names across the plot to rearrange variables.


![IPython terminal](https://s3-us-west-1.amazonaws.com/plotly-tutorials/plotly-documentation/images/python_parcoords_ex1.gif)


### Basic Parallel Coordinates Plot

```python inputHidden=false outputHidden=false
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/bcdunbar/datasets/master/iris.csv")

data = [
    go.Parcoords(
        line = dict(color = df['species_id'],
                   colorscale = [[0,'#D7C16B'],[0.5,'#23D8C3'],[1,'#F3F10F']]),
        dimensions = list([
            dict(range = [0,8],
                constraintrange = [4,8],
                label = 'Sepal Length', values = df['sepal_length']),
            dict(range = [0,8],
                label = 'Sepal Width', values = df['sepal_width']),
            dict(range = [0,8],
                label = 'Petal Length', values = df['petal_length']),
            dict(range = [0,8],
                label = 'Petal Width', values = df['petal_width'])
        ])
    )
]

layout = go.Layout(
    plot_bgcolor = '#E5E5E5',
    paper_bgcolor = '#E5E5E5'
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename = 'parcoords-basic')
```

### Advanced Parallel Coordinates Plot

```python inputHidden=false outputHidden=false
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/bcdunbar/datasets/master/parcoords_data.csv")

data = [
    go.Parcoords(
        line = dict(color = df['colorVal'],
                   colorscale = 'Jet',
                   showscale = True,
                   reversescale = True,
                   cmin = -4000,
                   cmax = -100),
        dimensions = list([
            dict(range = [32000,227900],
                 constraintrange = [100000,150000],
                 label = 'Block Height', values = df['blockHeight']),
            dict(range = [0,700000],
                 label = 'Block Width', values = df['blockWidth']),
            dict(tickvals = [0,0.5,1,2,3],
                 ticktext = ['A','AB','B','Y','Z'],
                 label = 'Cyclinder Material', values = df['cycMaterial']),
            dict(range = [-1,4],
                 tickvals = [0,1,2,3],
                 label = 'Block Material', values = df['blockMaterial']),
            dict(range = [134,3154],
                 visible = True,
                 label = 'Total Weight', values = df['totalWeight']),
            dict(range = [9,19984],
                 label = 'Assembly Penalty Weight', values = df['assemblyPW']),
            dict(range = [49000,568000],
                 label = 'Height st Width', values = df['HstW']),
            dict(range = [-28000,196430],
                 label = 'Min Height Width', values = df['minHW']),
            dict(range = [98453,501789],
                 label = 'Min Width Diameter', values = df['minWD']),
            dict(range = [1417,107154],
                 label = 'RF Block', values = df['rfBlock'])
        ])
    )
]

py.iplot(data, filename = 'parcoords-advanced')
```

#### Reference
See https://plot.ly/python/reference/#parcoords for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'parcoords.ipynb', 'python/parallel-coordinates-plot/', 'Parallel Coordinates Plot | plotly',
    'How to make parallel coorindates plots in Python with Plotly.',
    title = 'Parallel Coordinates Plot | plotly',
    name = 'Parallel Coordinates Plot',
    has_thumbnail='true', thumbnail='thumbnail/parcoords.jpg', 
    language='python', 
    # page_type='example_index', // note this is only if you want the tutorial to appear on the main page: plot.ly/python
    display_as='scientific', order=11.5,
    ipynb= '~notebook_demo/142')
```

```python

```