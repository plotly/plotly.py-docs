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
    description: Comparing WebGL with Scattergl() to SVG with Scatter() in Python
      with Plotly.
    has_thumbnail: false
    language: python
    layout: user-guide
    name: Comparing WebGL vs SVG
    page_type: example_index
    permalink: python/compare-webgl-svg/
    thumbnail: /images/static-image
    title: Comparing WebGL vs SVG | plotly
---

### Comparing Scatter Plots with 75,000 Random Points


Now in Ploty you can implement WebGL with `Scattergl()` in place of `Scatter()` <br>
for increased speed, improved interactivity, and the ability to plot even more data!


### WebGL

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

N = 75000
trace = go.Scattergl(
    x = np.random.randn(N),
    y = np.random.randn(N),
    mode = 'markers',
    marker = dict(
        line = dict(
            width = 1,
            color = '#404040')
    )
)
data = [trace]
layout = dict(title = 'WEBGL')
fig = dict(data=data, layout=layout)
py.iplot(data, filename='webgl75')
```

### SVG

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

N = 75000
trace = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N),
    mode = 'markers',
    marker = dict(
        line = dict(
            width = 1,
            color = '#404040')
    )
)
data = [trace]
layout = dict(title = 'SVG')
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='svg75')
```

### References


For more information see <br>
`Scattergl()` : https://plot.ly/python/reference/#scattergl <br>
`Scatter()` : https://plot.ly/python/reference/#scatter

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'comparewebgl.ipynb', 'python/compare-webgl-svg/', 'Python Comparing WebGL vs SVG | plotly',
    'Comparing WebGL with Scattergl() to SVG with Scatter() in Python with Plotly.',
    title = 'Comparing WebGL vs SVG | plotly',
    name = 'Comparing WebGL vs SVG',
    language='python')

```

```python

```
