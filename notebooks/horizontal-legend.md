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
    description: How to add images to charts as background images or logos.
    display_as: layout_opt
    has_thumbnail: false
    ipynb: ~notebook_demo/94
    language: python
    layout: user-guide
    name: Horizontal Legends
    order: 12
    page_type: example_index
    permalink: python/horizontal-legend/
    thumbnail: thumbnail/your-tutorial-chart.jpg
    title: Horizontal legend | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



###  Horizontal Legend

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

trace1 = go.Scatter(
                x=np.random.randn(75),
                mode='markers',
                name="Plot1",
                marker=dict(
                size=16,
                color='rgba(152, 0, 0, .8)'
                ))
trace2 = go.Scatter(
                x=np.random.randn(75),
                mode='markers',
                name="Plot2",
                marker=dict(
                size=16,
                color='rgba(0, 152, 0, .8)'
                ))
trace3 = go.Scatter(
                x=np.random.randn(75),
                mode='markers',
                name="Plot3",
                marker=dict(
                size=16,
                color='rgba(0, 0, 152, .8)'
                ))

data = [trace1, trace2, trace3]
layout = go.Layout(
                legend=dict(
                orientation="h")
                )
figure=go.Figure(data=data, layout=layout)

py.iplot(figure)
```

#### Reference
See https://plot.ly/python/reference/#layout-legend-orientation for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/csshref="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'horizontal-legends.ipynb', 'python/horizontal-legend/', 'Horizontal legend | plotly',
    'How to add images to charts as background images or logos.',
    title = 'Horizontal legend | plotly',
    name = 'Horizontal Legends',
    has_thumbnail='false', thumbnail='thumbnail/your-tutorial-chart.jpg',
    language='python', page_type='example_index',
    display_as='layout_opt', order=12,
    ipynb= '~notebook_demo/94')

```

```python

```
