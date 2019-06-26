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
    description: How to style markers in Python with Plotly.
    display_as: style_opt
    has_thumbnail: false
    ipynb: ~notebook_demo/203
    language: python
    layout: user-guide
    name: Styling Markers
    order: 8
    page_type: example_index
    permalink: python/marker-style/
    thumbnail: thumbnail/marker-style.gif
    title: Styling Markers | Plotly
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

### Add Marker Border


In order to make markers distinct, you can add a border to the markers. This can be achieved by adding the line dict to the marker dict. For example, `marker:{..., line: {...}}`.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))

data = [
    go.Scatter(
        mode = 'markers',
        x = x,
        y = y,
        marker = dict(
          color = 'rgb(17, 157, 255)',
          size = 20,
          line = dict(
            color = 'rgb(231, 99, 250)',
            width = 2
          )
        ),
        showlegend = False
  ),
  go.Scatter(
      mode = 'markers',
      x = [2],
      y = [4.5],
      marker = dict(
        color = 'rgb(17, 157, 255)',
        size = 120,
        line = dict(
          color = 'rgb(231, 99, 250)',
          width = 12
        )
      ),
      showlegend = False
  )]

py.iplot(data, filename = "style-add-border")
```

### Fully Opaque


Fully opaque, the default setting, is useful for non-overlapping markers. When many points overlap it can be hard to observe density.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))

data = [
    go.Scatter(
        mode = 'markers',
        x = x,
        y = y,
        marker = dict(
          color = 'rgb(17, 157, 255)',
          size = 20,
          line = dict(
            color = 'rgb(231, 99, 250)',
            width = 2
          )
        ),
        showlegend = False
      ),
      go.Scatter(
          mode = 'markers',
          x = [2,2],
          y = [4.25,4.75],
          marker = dict(
            color = 'rgb(17, 157, 255)',
            size = 80,
            line = dict(
              color = 'rgb(231, 99, 250)',
              width = 8
            )
          ),
          showlegend = False
    )]

py.iplot(data, filename = "style-full-opaque")
```

### Opacity


Setting opacity outside the marker will set the opacity of the trace. Thus, it will allow greater visbility of additional traces but like fully opaque it is hard to distinguish density.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=4.5, size=(500,))
x2 = np.random.uniform(low=3, high=6, size=(500,))
y2 = np.random.uniform(low=4.5, high=6, size=(500,))

data = [
    go.Scatter(
        mode = 'markers',
        x = x,
        y = y,
        opacity = 0.5,
        marker = dict(
          color = 'rgb(17, 157, 255)',
          size = 20,
          line = dict(
            color = 'rgb(231, 99, 250)',
            width = 2
          )
        ),
        name = 'Opacity 0.5'
      ),
     go.Scatter(
       mode = 'markers',
       x = x2,
       y = y2,
       marker = dict(
         color = 'rgb(17, 157, 255)',
         size = 20,
         line = dict(
           color = 'rgb(231, 99, 250)',
           width = 2
         )
       ),
       name = 'Opacity 1.0'
     ),
     go.Scatter(
        mode = 'markers',
        x = [2,2],
        y = [4.25,4.75],
        opacity = 0.5,
        marker = dict(
           color = 'rgb(17, 157, 255)',
           size = 80,
           line = dict(
              color = 'rgb(231, 99, 250)',
              width = 8
           )
        ),
        showlegend = False
    )]

py.iplot(data, filename = "style-opacity")
```

### Marker Opacity


To maximise visibility of density, it is recommended to set the opacity inside the marker `marker:{opacity:0.5}`. If mulitple traces exist with high density, consider using marker opacity in conjunction with trace opacity.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))

data = [
    go.Scatter(
        mode = 'markers',
        x = x,
        y = y,
        marker = dict(
          color = 'rgb(17, 157, 255)',
          size = 20,
          opacity = 0.5,
          line = dict(
            color = 'rgb(231, 99, 250)',
            width = 2
          )
        ),
        showlegend = False
      ),
      go.Scatter(
          mode = 'markers',
          x = [2,2],
          y = [4.25,4.75],
          marker = dict(
            color = 'rgb(17, 157, 255)',
            size = 80,
            opacity = 0.5,
            line = dict(
              color = 'rgb(231, 99, 250)',
              width = 8
            )
          ),
          showlegend = False
    )]

py.iplot(data, filename = "style-marker-opacity")
```

### Color Opacity


To maximise visibility of each point, set the color opacity by using alpha: `marker:{color: 'rgba(0,0,0,0.5)'}`. Here, the marker line will remain opaque.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))

data = [
    go.Scatter(
        mode = 'markers',
        x = x,
        y = y,
        marker = dict(
          color = 'rgba(17, 157, 255, 0.5)',
          size = 20,
          line = dict(
            color = 'rgb(231, 99, 250)',
            width = 2
          )
        ),
        showlegend = False
      ),
      go.Scatter(
          mode = 'markers',
          x = [2,2],
          y = [4.25,4.75],
          marker = dict(
            color = 'rgba(17, 157, 255, 0.5)',
            size = 80,
            line = dict(
              color = 'rgb(231, 99, 250)',
              width = 8
            )
          ),
          showlegend = False
    )]

py.iplot(data, filename = "style-color-opacity")
```

### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'marker-style.ipynb', 'python/marker-style/', 'Styling Markers',
    'How to style markers in Python with Plotly.',
    title = 'Styling Markers | Plotly',
    has_thumbnail='false', thumbnail='thumbnail/marker-style.gif',
    language='python',
    page_type='example_index',
    display_as='style_opt', order=8, ipynb='~notebook_demo/203')
```

```python

```
