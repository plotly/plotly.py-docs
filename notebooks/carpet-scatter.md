---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernel_info:
    name: python3
  kernelspec:
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to make carpet scatter plots in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/146
    language: python
    layout: user-guide
    name: Carpet Scatter Plot
    order: 28
    page_type: u-guide
    permalink: python/carpet-scatter/
    thumbnail: thumbnail/scattercarpet.jpg
    title: Carpet Scatter Plots | Plotly
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

```python inputHidden=false outputHidden=false
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
    aaxis = dict(
      tickprefix = 'a = ',
      ticksuffix = 'm',
      smoothing = 1,
      minorgridcount = 9
      ),
    baxis = dict(
      tickprefix = 'b = ',
      ticksuffix = 'Pa',
      smoothing = 1,
      minorgridcount = 9
      )
    )

data = [trace1]

fig = go.Figure(data = data)
py.iplot(fig, filename = "scattercarpet/basic")
```

### Add Carpet Scatter Trace

```python inputHidden=false outputHidden=false
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
    aaxis = dict(
      tickprefix = 'a = ',
      ticksuffix = 'm',
      smoothing = 1,
      minorgridcount = 9
      ),
    baxis = dict(
      tickprefix = 'b = ',
      ticksuffix = 'Pa',
      smoothing = 1,
      minorgridcount = 9
      )
    )

trace2 = go.Scattercarpet(
    a = [4, 4.5, 5, 6],
    b = [2.5, 2.5, 2.5, 2.5],
    line = dict(
      shape = 'spline',
      smoothing = 1,
      color = 'blue'
    )
  )

data = [trace1,trace2]

fig = go.Figure(data = data)
py.iplot(fig, filename = "scattercarpet/add-scattercarpet")
```

### Add Multiple Scatter Traces

```python inputHidden=false outputHidden=false
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [0.1,0.2,0.3],
    b = [1,2,3],
    y = [[1,2.2,3],[1.5,2.7,3.5],[1.7,2.9,3.7]],
    cheaterslope = 1,
    aaxis = dict(
        title = "a",
        tickmode = "linear",
        dtick = 0.05
    ),
    baxis = dict(
        title = "b",
        tickmode = "linear",
        dtick = 0.05
    )
)

trace2 = go.Scattercarpet(
    name = "b = 1.5",
    a = [0.05, 0.15, 0.25, 0.35],
    b = [1.5, 1.5, 1.5, 1.5]
)

trace3 = go.Scattercarpet(
    name = "b = 2",
    a = [0.05, 0.15, 0.25, 0.35],
    b = [2, 2, 2, 2]
)

trace4 = go.Scattercarpet(
    name = "b = 2.5",
    a = [0.05, 0.15, 0.25, 0.35],
    b = [2.5, 2.5, 2.5, 2.5]
)

trace5 = go.Scattercarpet(
    name = "a = 0.15",
    a = [0.15, 0.15, 0.15, 0.15],
    b = [0.5, 1.5, 2.5, 3.5],
    line = dict(
        smoothing = 1,
        shape = "spline"
    )
)

trace6 = go.Scattercarpet(
    name = "a = 0.2",
    a = [0.2, 0.2, 0.2, 0.2],
    b = [0.5, 1.5, 2.5, 3.5],
    line = dict(
        smoothing = 1,
        shape = "spline"
    ),
      marker = dict(
        size = [10, 20, 30, 40],
        color = ["#000", "#f00", "#ff0", "#fff"]
      )
)

trace7 = go.Scattercarpet(
    name = "a = 0.25",
    a = [0.25, 0.25, 0.25, 0.25],
    b = [0.5, 1.5, 2.5, 3.5],
    line = dict(
        smoothing = 1,
        shape = "spline"
    )
)

layout = go.Layout(
    title = "scattercarpet extrapolation, clipping, and smoothing",
    hovermode = "closest"
)

data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7]

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename = "scattercarpet/multiple")
```

### Reference


See https://plot.ly/python/reference/#scattercarpet for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'scattercarpet.ipynb', 'python/carpet-scatter/', 'Carpet Scatter Plot',
    'How to make carpet scatter plots in Python with Plotly.',
    title = 'Carpet Scatter Plots | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/scattercarpet.jpg',
    language='python',
    # page_type='example_index', // note this is only if you want the tutorial to appear on the main page: plot.ly/python
    display_as='scientific', order=28,
    ipynb= '~notebook_demo/146')
```

```python

```