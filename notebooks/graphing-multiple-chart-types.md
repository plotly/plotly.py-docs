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
    description: How to design figures with multiple chart types in python.
    display_as: basic
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Multiple Chart Types
    order: 13
    page_type: u-guide
    permalink: python/graphing-multiple-chart-types/
    thumbnail: thumbnail/multiple-chart-type.jpg
    title: Python Mulitple Chart Types | plotly
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Line Chart and a Bar Chart
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5],
    y=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
)
trace2 = go.Bar(
    x=[0, 1, 2, 3, 4, 5],
    y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
)

data = [trace1, trace2]
py.iplot(data, filename='bar-line')
```

<!-- #region {"deletable": true, "editable": true} -->
#### A Contour and Scatter Plot of the Method of Steepest Descent
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import json
import six.moves.urllib

response = six.moves.urllib.request.urlopen('https://raw.githubusercontent.com/plotly/datasets/master/steepest.json')
data = json.load(response)

trace1 = go.Contour(
    z=data['contour_z'][0],
    y=data['contour_y'][0],
    x=data['contour_x'][0],
    ncontours=30,
    showscale=False
)
trace2 = go.Scatter(
    x=data['trace_x'],
    y=data['trace_y'],
    mode='markers+lines',
    name='steepest',
    line=dict(
        color='black'
    )
)

data = [trace1, trace2]
py.iplot(data, filename='contour-scatter')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
See https://plot.ly/python/reference/ for more information and attribute options!
<!-- #endregion -->

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'mixed.ipynb', 'python/graphing-multiple-chart-types/', 'Python Mulitple Chart Types | plotly',
    'How to design figures with multiple chart types in python.',
    title = 'Python Mulitple Chart Types | plotly',
    name = 'Multiple Chart Types',
    thumbnail='thumbnail/mixed.jpg', language='python',
    has_thumbnail='true', display_as='basic', order=13)
```

```python deletable=true editable=true

```