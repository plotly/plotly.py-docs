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
    description: How to make carpet contour plots in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/145
    language: python
    layout: user-guide
    name: Carpet Contour Plot
    order: 27
    page_type: u-guide
    permalink: python/carpet-contour/
    thumbnail: thumbnail/contourcarpet.jpg
    title: Carpet Contour Plots | Plotly
---

<!-- #region {"inputHidden": false, "outputHidden": false} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

#### Version Check
Plotly's python package is updated frequently. Run `pip install plotly --upgrade` to use the latest version.

```python inputHidden=false outputHidden=false
import plotly
plotly.__version__
```

### Basic Carpet Plot

Set the `x` and `y` coorindates, using `x` and `y` attributes. If `x` coorindate values are ommitted a cheater plot will be created. To save parameter values use `a` and `b` attributes. To make changes to the axes, use `aaxis` or `baxis` attributes. For a more detailed list of axes attributes refer to [python reference](https://plot.ly/python/reference/#carpet-aaxis).

```python
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    x = [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
    y = [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
    aaxis = dict(
        tickprefix = 'a = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    ),
    baxis = dict(
        tickprefix = 'b = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    )
)

data = [trace1]

layout = go.Layout(
    margin = dict(
    	t = 40,
        r = 30,
        b = 30,
        l = 30
    ),
    yaxis = dict(
        range = [0.388,4.361]
    ),
    xaxis = dict(
    	range = [0.667,5.932]	
    )
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename = "contourcarpet/basic")
```

### Add Contours

```python inputHidden=false outputHidden=false
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Contourcarpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    z = [1, 1.96, 2.56, 3.0625, 4, 5.0625, 1, 7.5625, 9, 12.25, 15.21, 14.0625],
    autocontour = False,
    contours = dict(
    	start = 1,
        end = 14,
        size = 1
    ),
    line = dict(
    	width = 2,
    	smoothing = 0
    ),
    colorbar = dict(
    	len = 0.4,
        y = 0.25
    )
)

trace2 = go.Carpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    x = [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
    y = [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
    aaxis = dict(
        tickprefix = 'a = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    ),
    baxis = dict(
        tickprefix = 'b = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    )
)

data = [trace1, trace2]

layout = go.Layout(
    margin = dict(
    	t = 40,
        r = 30,
        b = 30,
        l = 30
    ),
    yaxis = dict(
        range = [0.388,4.361]
    ),
    xaxis = dict(
    	range = [0.667,5.932]	
    )
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename = "contourcarpet/add-contours")
```

### Add Multiple Traces

```python inputHidden=false outputHidden=false
import plotly.graph_objs as go
import plotly.plotly as py

import urllib, json

url = "https://raw.githubusercontent.com/bcdunbar/datasets/master/airfoil_data.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
    
trace1 = go.Carpet(
    a = data[0]['a'],
    b = data[0]['b'],
    x = data[0]['x'],
    y = data[0]['y'],
    baxis = dict(
      startline = False,
      endline = False,
      showticklabels = "none",
      smoothing = 0,
      showgrid = False
    ),
    aaxis = dict(
      startlinewidth = 2,
      startline = True,
      showticklabels = "none",
      endline = True,
      showgrid = False,
      endlinewidth = 2,
      smoothing = 0
    )
)

trace2 = go.Contourcarpet(
    z = data[1]['z'],
    autocolorscale = False,
    zmax = 1,
    name = "Pressure",
    colorscale = "Viridis",
    zmin = -8,
    colorbar = dict(
      y = 0,
      yanchor = "bottom",
      titleside = "right",
      len = 0.75,
      title = "Pressure coefficient, c<sub>p</sub>"
    ),
    contours = dict(
      start = -1,
      size = 0.025,
      end = 1.000,
      showlines = False
    ),
    line = dict(
      smoothing = 0
    ),
    autocontour = False,
    zauto = False
)

trace3 = go.Contourcarpet(
    z = data[2]['z'],
    opacity = 0.300,
    showlegend = True,
    name = "Streamlines",
    autocontour = True,
    ncontours = 50,
    contours = dict(
      coloring = "none"
    ),
    line = dict(
      color = "white",
      width = 1
    )
)

trace4 = go.Contourcarpet(
    z = data[3]['z'],
    showlegend = True,
    name = "Pressure<br>contours",
    autocontour = False,
    line = dict(
        color = "rgba(0, 0, 0, 0.5)",
        smoothing = 1
    ),
    contours = dict(
        size = 0.250,
        start = -4,
        coloring = "none",
        end = 1.000,
        showlines = True
      )
)

trace5 = go.Scatter(
    x = data[4]['x'],
    y = data[4]['y'],
    legendgroup = "g1",
    name = "Surface<br>pressure",
    mode = "lines",
    hoverinfo = "skip",
    line = dict(
      color = "rgba(255, 0, 0, 0.5)",
      width = 1,
      shape = "spline",
      smoothing = 1
    ),
    fill = "toself",
    fillcolor = "rgba(255, 0, 0, 0.2)"
)

trace6 = go.Scatter(
    x = data[5]['x'],
    y = data[5]['y'],
    showlegend = False,
    legendgroup = "g1",
    mode = "lines",
    hoverinfo = "skip",
    line = dict(
      color = "rgba(255, 0, 0, 0.3)",
      width = 1
    )
)

trace7 = go.Scatter(
    x = data[6]['x'],
    y = data[6]['y'],
    showlegend = False,
    legendgroup = "g1",
    name = "cp",
    text = data[6]['text'],
    hoverinfo = "text",
    mode = "lines",
    line = dict(
      color = "rgba(255, 0, 0, 0.2)",
      width = 0
    )
)

data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7]

layout = go.Layout(
    yaxis = dict(
      zeroline = False,
      range = [-1.800,1.800],
      showgrid = False
    ),
    dragmode = "pan",
    height = 700,
    xaxis = dict(
      zeroline = False,
      scaleratio = 1,
      scaleanchor = 'y',
      range = [-3.800,3.800],
      showgrid = False
    ),
    title = "Flow over a Karman-Trefftz airfoil",
    hovermode = "closest",
    margin = dict(
      r = 60,
      b = 40,
      l = 40,
      t = 80
    ),
    width = 900
)

fig = go.Figure(data=data,layout=layout)
py.iplot(fig, filename = "contourcarpet/airfoil")
```

### Reference


See https://plot.ly/python/reference/#contourcarpet for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'contourcarpet.ipynb', 'python/carpet-contour/', 'Carpet Contour Plot',
    'How to make carpet contour plots in Python with Plotly.',
    title = 'Carpet Contour Plots | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/contourcarpet.jpg', 
    language='python', 
    # page_type='example_index', // note this is only if you want the tutorial to appear on the main page: plot.ly/python
    display_as='scientific', order=27,
    ipynb= '~notebook_demo/145')

```

```python

```