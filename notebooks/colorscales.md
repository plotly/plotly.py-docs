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
    description: How to set colorscales and heatmap colorscales in Python and Plotly.
      Divergent, sequential, and qualitative colorscales.
    display_as: style_opt
    has_thumbnail: true
    ipynb: ~notebook_demo/187
    language: python
    layout: user-guide
    name: Colorscales
    order: 11
    page_type: example_index
    permalink: python/colorscales/
    thumbnail: thumbnail/heatmap_colorscale.jpg
    title: Colorscales in Python | Plotly
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

### Custom Discretized Heatmap Colorscale

```python
import plotly.plotly as py

py.iplot([{
    'z': [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ],
    'type': 'heatmap',
    'colorscale': [
        # Let first 10% (0.1) of the values have color rgb(0, 0, 0)
        [0, 'rgb(0, 0, 0)'],
        [0.1, 'rgb(0, 0, 0)'],

        # Let values between 10-20% of the min and max of z
        # have color rgb(20, 20, 20)
        [0.1, 'rgb(20, 20, 20)'],
        [0.2, 'rgb(20, 20, 20)'],

        # Values between 20-30% of the min and max of z
        # have color rgb(40, 40, 40)
        [0.2, 'rgb(40, 40, 40)'],
        [0.3, 'rgb(40, 40, 40)'],

        [0.3, 'rgb(60, 60, 60)'],
        [0.4, 'rgb(60, 60, 60)'],

        [0.4, 'rgb(80, 80, 80)'],
        [0.5, 'rgb(80, 80, 80)'],

        [0.5, 'rgb(100, 100, 100)'],
        [0.6, 'rgb(100, 100, 100)'],

        [0.6, 'rgb(120, 120, 120)'],
        [0.7, 'rgb(120, 120, 120)'],

        [0.7, 'rgb(140, 140, 140)'],
        [0.8, 'rgb(140, 140, 140)'],

        [0.8, 'rgb(160, 160, 160)'],
        [0.9, 'rgb(160, 160, 160)'],

        [0.9, 'rgb(180, 180, 180)'],
        [1.0, 'rgb(180, 180, 180)']
    ],
    'colorbar': {
        'tick0': 0,
        'dtick': 1
    }
}], filename='heatmap-discrete-colorscale')
```

### Colorscale for Scatter Plots

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        y=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        marker=dict(
            size=16,
            cmax=39,
            cmin=0,
            color=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
            colorbar=dict(
                title='Colorbar'
            ),
            colorscale='Viridis'
        ),
        mode='markers')
]

fig = go.Figure(data=data)
py.iplot(fig)
```

### Colorscale for Contour Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]],
        colorscale='Jet',
    )
]

py.iplot(data, filename='simple-colorscales-colorscale')
```

### Custom Heatmap Colorscale

```python
import plotly.plotly as py
import plotly.graph_objs as go

import six.moves.urllib
import json

response = six.moves.urllib.request.urlopen('https://raw.githubusercontent.com/plotly/datasets/master/custom_heatmap_colorscale.json')
dataset = json.load(response)

data = [
    go.Heatmap(
        z=dataset['z'],
        colorscale=[[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'], [0.2222222222222222, 'rgb(244,109,67)'], [0.3333333333333333, 'rgb(253,174,97)'], [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'], [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'], [0.8888888888888888, 'rgb(69,117,180)'], [1.0, 'rgb(49,54,149)']]
    )
]
py.iplot(data, filename='custom-colorscale')
```

### Custom Contour Plot Colorscale

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]],
        colorscale=[[0, 'rgb(166,206,227)'], [0.25, 'rgb(31,120,180)'], [0.45, 'rgb(178,223,138)'], [0.65, 'rgb(51,160,44)'], [0.85, 'rgb(251,154,153)'], [1, 'rgb(227,26,28)']],
    )
]

py.iplot(data, filename='colorscales-custom-colorscale')
```

### Custom Colorbar

```python
import plotly.plotly as py
import plotly.graph_objs as go

import six.moves.urllib
import json

response = six.moves.urllib.request.urlopen('https://raw.githubusercontent.com/plotly/datasets/master/custom_heatmap_colorscale.json')
dataset = json.load(response)

data = [
    go.Heatmap(
        z=dataset['z'],
        colorscale=[[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'], [0.2222222222222222, 'rgb(244,109,67)'],
        [0.3333333333333333, 'rgb(253,174,97)'], [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'],
        [0.6666666666666666, 'rgb(171,217,233)'],[0.7777777777777778, 'rgb(116,173,209)'], [0.8888888888888888, 'rgb(69,117,180)'],
        [1.0, 'rgb(49,54,149)']],
        colorbar = dict(
            title = 'Surface Heat',
            titleside = 'top',
            tickmode = 'array',
            tickvals = [2,50,100],
            ticktext = ['Hot','Mild','Cool'],
            ticks = 'outside'
        )
    )
]

py.iplot(data, filename='custom-colorscale-colorbar')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-colorscaleplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-colorscaleplot/" ,width="100%" ,height="650px", frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-colorscaleplot/code" ,width="100%" ,height=500, frameBorder="0")
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
    'colorscales.ipynb', 'python/colorscales/', 'Colorscales',
    'How to set colorscales and heatmap colorscales in Python and Plotly. Divergent, sequential, and qualitative colorscales.',
    title = 'Colorscales in Python | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/heatmap_colorscale.jpg', 
    language='python', 
    page_type='example_index',
    display_as='style_opt', 
    order=11,
    ipynb= '~notebook_demo/187')
```