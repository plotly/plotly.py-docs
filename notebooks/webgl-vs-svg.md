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
    description: Implement WebGL for increased speed, improved interactivity, and
      the ability to plot even more data!
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/44
    language: python
    layout: user-guide
    name: WebGL vs SVG
    order: 0.5
    permalink: python/webgl-vs-svg/
    thumbnail: thumbnail/webgl.jpg
    title: Python WebGL vs SVG | plotly
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Compare WebGL and SVG
Checkout [this notebook](https://plot.ly/python/compare-webgl-svg) to compare WebGL and SVG scatter plots with 75,000 random data points
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### WebGL with 100,000  points
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

N = 100000
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
py.iplot(data, filename='WebGL100000')
```

<!-- #region {"deletable": true, "editable": true} -->
#### WebGL with 1 Million Points
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

N = 1000000
trace = go.Scattergl(
    x = np.random.randn(N),
    y = np.random.randn(N),
    mode = 'markers',
    marker = dict(
        color = 'rgb(152, 0, 0)',
        line = dict(
            width = 1,
            color = 'rgb(0,0,0)')
    )
)
data = [trace]
py.iplot(data, filename='WebGLmillion')
```

<!-- #region {"deletable": true, "editable": true} -->
#### WebGL with many traces
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

data = []
trace_num = 10
point_num = 5000
for i in range(trace_num):
    data.append(go.Scattergl(
        x = np.linspace(0, 1, point_num),
        y = np.random.randn(point_num)+(i*5)
    )
)
layout = dict(showlegend=False)
fig=dict(data=data, layout=layout)
py.iplot(fig, filename='WebGL_line')
```

<!-- #region {"deletable": true, "editable": true} -->
### Reference
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
See https://plot.ly/python/reference/#scattergl for more information and chart attribute options!
<!-- #endregion -->

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'webgl.ipynb', 'python/webgl-vs-svg/', 'Python WebGL vs SVG | plotly',
    'Implement WebGL for increased speed, improved interactivity, and the ability to plot even more data!',
    title = 'Python WebGL vs SVG | plotly',
    name = 'WebGL vs SVG',
    has_thumbnail='true', thumbnail='thumbnail/webgl.jpg',
    language='python',
    display_as='basic', order=0.5,
    ipynb= '~notebook_demo/44')
```

```python deletable=true editable=true

```
