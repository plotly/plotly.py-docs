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
    description: How to make Contour plots in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/185
    language: python
    layout: user-guide
    name: Contour Plots
    order: 2
    page_type: example_index
    permalink: python/contour-plots/
    thumbnail: thumbnail/contour.jpg
    title: Contour Plots | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


### Basic Contour Plot  ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]]
    )
]
py.iplot(data)
```

### Setting X and Y Coordinates in a Contour Plot ###

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
        x=[-9, -6, -5 , -3, -1],
        y=[0, 1, 4, 5, 7]
    )]

py.iplot(data)

```

### Colorscale for Contour Plot ###

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
    )]
py.iplot(data)
```

### Customizing Size and Range of a Contour Plot's Contours ###

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
        autocontour=False,
        contours=dict(
            start=0,
            end=8,
            size=2,
        ),
    )
]
py.iplot(data)

```

### Customizing Spacing Between X and Y Axis Ticks ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    {
        'z': [[10, 10.625, 12.5, 15.625, 20],
              [5.625, 6.25, 8.125, 11.25, 15.625],
              [2.5, 3.125, 5., 8.125, 12.5],
              [0.625, 1.25, 3.125, 6.25, 10.625],
              [0, 0.625, 2.5, 5.625, 10]],
        'colorscale':'Jet',
        'type': u'contour',
        'dx': 10,
        'x0': 5,
        'dy': 10,
        'y0':10,
    }
]
py.iplot(data)

```

### Connect the Gaps Between None Values in the Z Matrix ###

```python
import plotly.plotly as py
import plotly.tools as tls

trace0 = {
    'z': [[None, None, None, 12, 13, 14, 15, 16],
          [None, 1, None, 11, None, None, None, 17],
          [None, 2, 6, 7, None, None, None, 18],
          [None, 3, None, 8, None, None, None, 19],
          [5, 4, 10, 9, None, None, None, 20],
          [None, None, None, 27, None, None, None, 21],
          [None, None, None, 26, 25, 24, 23, 22]],
    'type': 'contour',
    'showscale': False
}
trace1 = {
    'z': [[None, None, None, 12, 13, 14, 15, 16],
          [None, 1, None, 11, None, None, None, 17],
          [None, 2, 6, 7, None, None, None, 18],
          [None, 3, None, 8, None, None, None, 19],
          [5, 4, 10, 9, None, None, None, 20],
          [None, None, None, 27, None, None, None, 21],
          [None, None, None, 26, 25, 24, 23, 22]],
    'connectgaps': True,
    'type': 'contour',
    'showscale': False
}
trace2 = {
    'z': [[None, None, None, 12, 13, 14, 15, 16],
          [None, 1, None, 11, None, None, None, 17],
          [None, 2, 6, 7, None, None, None, 18],
          [None, 3, None, 8, None, None, None, 19],
          [5, 4, 10, 9, None, None, None, 20],
          [None, None, None, 27, None, None, None, 21],
          [None, None, None, 26, 25, 24, 23, 22]],
    'type': 'heatmap',
    'zsmooth': 'best',
    'showscale': False
}
trace3 = {
    'z': [[None, None, None, 12, 13, 14, 15, 16],
          [None, 1, None, 11, None, None, None, 17],
          [None, 2, 6, 7, None, None, None, 18],
          [None, 3, None, 8, None, None, None, 19],
          [5, 4, 10, 9, None, None, None, 20],
          [None, None, None, 27, None, None, None, 21],
          [None, None, None, 26, 25, 24, 23, 22]],
    'connectgaps': True,
    'type': 'heatmap',
    'zsmooth': 'best',
    'showscale': False
}

fig = tls.make_subplots(rows=2, cols=2, subplot_titles=('connectgaps = False',
                                                        'connectgaps = True'))

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 2)

fig['layout']['yaxis1'].update(title='Contour map')
fig['layout']['yaxis3'].update(title='Heatmap')

py.iplot(fig)
```

### Smoothing the Contour lines ###

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Contour(
    z=[[2, 4, 7, 12, 13, 14, 15, 16],
       [3, 1, 6, 11, 12, 13, 16, 17],
       [4, 2, 7, 7, 11, 14, 17, 18],
       [5, 3, 8, 8, 13, 15, 18, 19],
       [7, 4, 10, 9, 16, 18, 20, 19],
       [9, 10, 5, 27, 23, 21, 21, 21],
       [11, 14, 17, 26, 25, 24, 23, 22]],
    line=dict(smoothing=0),
)
trace1 = go.Contour(
    z=[[2, 4, 7, 12, 13, 14, 15, 16],
       [3, 1, 6, 11, 12, 13, 16, 17],
       [4, 2, 7, 7, 11, 14, 17, 18],
       [5, 3, 8, 8, 13, 15, 18, 19],
       [7, 4, 10, 9, 16, 18, 20, 19],
       [9, 10, 5, 27, 23, 21, 21, 21],
       [11, 14, 17, 26, 25, 24, 23, 22]],
    line=dict(smoothing=0.85),
)

fig = tools.make_subplots(rows=1, cols=2,
                          subplot_titles=('Without Smoothing', 'With Smoothing'))

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)

py.iplot(fig)
```

### Smooth Contour Coloring ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

data=[
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]],
        contours=dict(
            coloring='heatmap'
        )
    )
]
py.iplot(data)

```

### Contour Line Labels ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

data=[
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]],
        contours=dict(
            coloring ='heatmap',
            showlabels = True,
            labelfont = dict(
                family = 'Raleway',
                size = 12,
                color = 'white',
            )
        )
    )
]

py.iplot(data)
```

### Contour Lines ###

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
        contours=dict(
            coloring='lines',
        ),
    )
]
py.iplot(data)

```

### Custom Contour Plot Colorscale ###

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
py.iplot(data, filename='contour-custom-colorscale')

```

### Color Bar Title ###

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
        colorbar=dict(
            title='Color bar title',
            titleside='right',
            titlefont=dict(
                size=14,
                family='Arial, sans-serif',
            ),
        )
    )
]
py.iplot(data)

```

### Color Bar Size for Contour Plots

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
        colorbar=dict(
            thickness=25,
            thicknessmode='pixels',
            len=0.9,
            lenmode='fraction',
            outlinewidth=0
        )
    )
]
py.iplot(data, filename='contour-custom-colorbar-size')

```

### Styling Color Bar Ticks for Contour Plots

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [{
        'type': u'contour',
        'z': [[10, 10.625, 12.5, 15.625, 20],
              [5.625, 6.25, 8.125, 11.25, 15.625],
              [2.5, 3.125, 5., 8.125, 12.5],
              [0.625, 1.25, 3.125, 6.25, 10.625],
              [0, 0.625, 2.5, 5.625, 10]],
        'colorbar':{
            'nticks': 10,
            'ticks': 'outside',
            'ticklen': 5,
            'tickwidth': 1,
            'showticklabels': True,
            'tickangle': 0,
            'tickfont': {
                'size': 12
            },
        }
        }]
py.iplot(data)

```

#### Reference
See https://plot.ly/python/reference/#contour for more information and chart attribute options!


```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/csshref="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'contour.ipynb', 'python/contour-plots/', 'Contour Plots',
    'How to make Contour plots in Python with Plotly.',
    title = 'Contour Plots | plotly',
    name = 'Contour Plots',
    has_thumbnail='true', thumbnail=' thumbnail/contour.jpg',
    language='python', page_type='example_index',
    display_as='scientific', order=2,
    ipynb= '~notebook_demo/185')
```

```python

```