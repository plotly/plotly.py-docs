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
    description: How to format axes of 3d plots in Python with Plotly.
    display_as: layout_opt
    has_thumbnail: false
    ipynb: ~notebook_demo/96
    language: python
    layout: user-guide
    name: 3D Axes
    order: 1
    page_type: example_index
    permalink: python/3d-axes/
    thumbnail: thumbnail/your-tutorial-chart.jpg
    title: Format 3d Axes | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


### Range of axes

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

N = 70
trace1 = go.Mesh3d(x=(70*np.random.randn(N)),
                   y=(55*np.random.randn(N)),
                   z=(40*np.random.randn(N)),
                   opacity=0.5,
                   color='rgba(244,22,100,0.6)'
                  )

layout = go.Layout(
                    scene = dict(
                    xaxis = dict(
                        nticks=4, range = [-100,100],),
                    yaxis = dict(
                        nticks=4, range = [-50,100],),
                    zaxis = dict(
                        nticks=4, range = [-100,100],),),
                    width=700,
                    margin=dict(
                    r=20, l=10,
                    b=10, t=10)
                  )
fig = go.Figure(data=[trace1], layout=layout)
py.iplot(fig, filename='3d-axis-range')
```

### Fixed Ratio Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import numpy as np

N = 50

fig = tls.make_subplots(
    rows=2, cols=2,
    specs=[
        [{'is_3d': True}, {'is_3d': True}],
        [{'is_3d': True}, {'is_3d': True}]
    ],
    print_grid=False
)
for i in [1,2]:
    for j in [1,2]:
        fig.append_trace(
            go.Mesh3d(
                x=(60*np.random.randn(N)),
                y=(25*np.random.randn(N)),
                z=(40*np.random.randn(N)),
                opacity=0.5,
              ), 
            row=i, col=j)

fig['layout'].update(go.Layout(
                    width=700,
                    margin=dict(
                    r=10, l=10,
                    b=10, t=10)
                  ))

# fix the ratio in the top left subplot to be a cube
fig['layout'][].update(go.Layout(
    go.layout.Scene(aspectmode='cube')),
    

# manually force the z-axis to appear twice as big as the other two
fig['layout']['scene2'].update(go.layout.Scene(
    aspectmode='manual',
    aspectratio=go.layout.scene.Aspectratio(
        x=1, y=1, z=2
    )
))

# draw axes in proportion to the proportion of their ranges
fig['layout']['scene3'].update(go.layout.Scene(aspectmode='data'))

# automatically produce something that is well proportioned using 'data' as the default
fig['layout']['scene4'].update(go.layout.Scene(aspectmode='auto'))

py.iplot(fig, filename='3d-axis-fixed-ratio-axes')

```

### Set Axes Title

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

N = 50
trace1 = go.Mesh3d(x=(60*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(40*np.random.randn(N)),
                   opacity=0.5,
                   color='yellow'
                  )
trace2 = go.Mesh3d(x=(70*np.random.randn(N)),
                   y=(55*np.random.randn(N)),
                   z=(30*np.random.randn(N)),
                   opacity=0.5,
                   color='pink'
                  )
layout = go.Layout(
                    scene = dict(
                    xaxis = dict(
                        title='X AXIS TITLE'),
                    yaxis = dict(
                        title='Y AXIS TITLE'),
                    zaxis = dict(
                        title='Z AXIS TITLE'),),
                    width=700,
                    margin=dict(
                    r=20, b=10,
                    l=10, t=10)
                  )
fig = go.Figure(data=[trace1,trace2], layout=layout)
py.iplot(fig, filename='3d-axis-titles')
```

### Ticks Formatting

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

N = 50
trace1 = go.Mesh3d(x=(60*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(40*np.random.randn(N)),
                   opacity=0.5,
                   color='rgba(100,22,200,0.5)'
                  )

layout = go.Layout(
                    scene = dict(
                    xaxis = dict(
                        ticktext= ['TICKS','MESH','PLOTLY','PYTHON'],
                        tickvals= [0,50,75,-50]),
                    yaxis = dict(
                        nticks=5, tickfont=dict(
                            color='green',
                            size=12,
                            family='Old Standard TT, serif',),
                        ticksuffix='#'),
                    zaxis = dict(
                        nticks=4, ticks='outside',
                        tick0=0, tickwidth=4),),
                    width=700,
                    margin=dict(
                    r=10, l=10,
                    b=10, t=10)
                  )
fig = go.Figure(data=[trace1], layout=layout)
py.iplot(fig, filename='3d-axis-tick-formatting')
```

### Background and Grid Color

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

N = 50
trace1 = go.Mesh3d(x=(30*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(30*np.random.randn(N)),
                   opacity=0.5,)


layout = go.Layout(
                    scene = dict(
                    xaxis = dict(
                         backgroundcolor="rgb(200, 200, 230)",
                         gridcolor="rgb(255, 255, 255)",
                         showbackground=True,
                         zerolinecolor="rgb(255, 255, 255)",),
                    yaxis = dict(
                        backgroundcolor="rgb(230, 200,230)",
                        gridcolor="rgb(255, 255, 255)",
                        showbackground=True,
                        zerolinecolor="rgb(255, 255, 255)"),
                    zaxis = dict(
                        backgroundcolor="rgb(230, 230,200)",
                        gridcolor="rgb(255, 255, 255)",
                        showbackground=True,
                        zerolinecolor="rgb(255, 255, 255)",),),
                    width=700,
                    margin=dict(
                    r=10, l=10,
                    b=10, t=10)
                  )
fig = go.Figure(data=[trace1], layout=layout)
py.iplot(fig, filename='3d-axis-background-and-grid-color')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    '3d-axes.ipynb', 'python/3d-axes/', 'Axes Formatting in 3d Plots | plotly',
    'How to format axes of 3d plots in Python with Plotly.',
    title = 'Format 3d Axes | plotly',
    name = '3D Axes',
    has_thumbnail='false', thumbnail='thumbnail/your-tutorial-chart.jpg', 
    language='python', page_type='example_index',
    display_as='layout_opt', order=1,
    ipynb= '~notebook_demo/96')  
```

```python

```