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
    description: How to make subplots in python. Examples of stacked, custom-sized,
      gridded, and annotated subplts.
    display_as: multiple_axes
    has_thumbnail: true
    ipynb: ~notebook_demo/269
    language: python
    layout: user-guide
    name: Subplots
    order: 2
    page_type: example_index
    permalink: python/subplots/
    redirect_from: ipython-notebooks/subplots/
    thumbnail: thumbnail/subplots.jpg
    title: Python Subplots | Examples | Plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Simple Subplot

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    mode='markers+text',
    text=['Text A', 'Text B', 'Text C'],
    textposition='bottom center'
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
    mode='markers+text',
    text=['Text D', 'Text E', 'Text F'],
    textposition='bottom center'
)

fig = tools.make_subplots(rows=1, cols=2)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)

fig['layout'].update(height=600, width=800, title='i <3 annotations and subplots')
py.iplot(fig, filename='simple-subplot-with-annotations')
```

#### Multiple Subplots

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
    xaxis='x2',
    yaxis='y2'
)
trace3 = go.Scatter(
    x=[300, 400, 500],
    y=[600, 700, 800],
    xaxis='x3',
    yaxis='y3'
)
trace4 = go.Scatter(
    x=[4000, 5000, 6000],
    y=[7000, 8000, 9000],
    xaxis='x4',
    yaxis='y4'
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis3=dict(
        domain=[0, 0.45],
        anchor='y3'
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis2=dict(
        domain=[0, 0.45],
        anchor='x2'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor='x4'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='multiple-subplots')
```

#### Multiple Subplots with Titles

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])

fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2',
                                                          'Plot 3', 'Plot 4'))

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)

fig['layout'].update(height=600, width=600, title='Multiple Subplots' +
                                                  ' with Titles')

py.iplot(fig, filename='make-subplots-multiple-with-titles')
```

#### Simple Subplot with Annotations

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    mode='markers+text',
    text=['Text A', 'Text B', 'Text C'],
    textposition='bottom center'
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
    mode='markers+text',
    text=['Text D', 'Text E', 'Text F'],
    textposition='bottom center'
)

fig = tools.make_subplots(rows=1, cols=2)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)

fig['layout'].update(height=600, width=800, title='i <3 annotations and subplots')
py.iplot(fig, filename='simple-subplot-with-annotations')
```

#### Side by Side Subplot

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
    xaxis='x2',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.7]
    ),
    xaxis2=dict(
        domain=[0.8, 1]
    ),
    yaxis2=dict(
        anchor='x2'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='side-by-side-subplot')
```

#### Customizing Subplot Axes

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])

fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2',
                                                          'Plot 3', 'Plot 4'))
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)

fig['layout']['xaxis1'].update(title='xaxis 1 title')
fig['layout']['xaxis2'].update(title='xaxis 2 title', range=[10, 50])
fig['layout']['xaxis3'].update(title='xaxis 3 title', showgrid=False)
fig['layout']['xaxis4'].update(title='xaxis 4 title', type='log')

fig['layout']['yaxis1'].update(title='yaxis 1 title')
fig['layout']['yaxis2'].update(title='yaxis 2 title', range=[40, 80])
fig['layout']['yaxis3'].update(title='yaxis 3 title', showgrid=False)
fig['layout']['yaxis4'].update(title='yaxis 4 title')

fig['layout'].update(title='Customizing Subplot Axes')

py.iplot(fig, filename='customizing-subplot-axes')
```

#### Subplots with Shared X-Axes

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[10, 11, 12]
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
)
trace3 = go.Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
)
fig = tools.make_subplots(rows=3, cols=1, specs=[[{}], [{}], [{}]],
                          shared_xaxes=True, shared_yaxes=True,
                          vertical_spacing=0.001)
fig.append_trace(trace1, 3, 1)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 1, 1)

fig['layout'].update(height=600, width=600, title='Stacked Subplots with Shared X-Axes')
py.iplot(fig, filename='stacked-subplots-shared-xaxes')
```

#### Subplots with Shared Y-Axes

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 3, 4]
)
trace1 = go.Scatter(
    x=[20, 30, 40],
    y=[5, 5, 5],
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[600, 700, 800],
)
trace3 = go.Scatter(
    x=[4000, 5000, 6000],
    y=[7000, 8000, 9000],
)

fig = tools.make_subplots(rows=2, cols=2, shared_yaxes=True)

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 2)

fig['layout'].update(height=600, width=600,
                     title='Multiple Subplots with Shared Y-Axes')
py.iplot(fig, filename='multiple-subplots-shared-yaxes')
```

#### Subplots with Shared Axes

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 3, 4]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[5, 5, 5],
    xaxis='x2',
    yaxis='y'
)
trace3 = go.Scatter(
    x=[2, 3, 4],
    y=[600, 700, 800],
    xaxis='x',
    yaxis='y3'
)
trace4 = go.Scatter(
    x=[4000, 5000, 6000],
    y=[7000, 8000, 9000],
    xaxis='x4',
    yaxis='y4'
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor='x4'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='shared-axes-subplots')
```

#### Stacked Subplots

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[10, 11, 12]
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
)
trace3 = go.Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
)

fig = tools.make_subplots(rows=3, cols=1)

fig.append_trace(trace3, 1, 1)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace1, 3, 1)


fig['layout'].update(height=600, width=600, title='Stacked subplots')
py.iplot(fig, filename='stacked-subplots')
```

#### Stacked Subplots with a Shared X-Axis

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[10, 11, 12]
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
    yaxis='y2'
)
trace3 = go.Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
    yaxis='y3'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    yaxis=dict(
        domain=[0, 0.33]
    ),
    legend=dict(
        traceorder='reversed'
    ),
    yaxis2=dict(
        domain=[0.33, 0.66]
    ),
    yaxis3=dict(
        domain=[0.66, 1]
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='stacked-subplots-shared-x-axis')
```

#### Custom Sized Subplot with Subplot Titles

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2],
    y=[1, 2]
)
trace1 = go.Scatter(
    x=[1, 2],
    y=[1, 2]
)
trace2 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 1, 2]
)
fig = tools.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2}, None]],
                          subplot_titles=('First Subplot','Second Subplot', 'Third Subplot'))

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)

fig['layout'].update(showlegend=False, title='Specs with Subplot Title')
py.iplot(fig, filename='custom-sized-subplot-with-subplot-titles')
```

#### Multiple Custom Sized Subplots

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(x=[1, 2], y=[1, 2], name='(1,1)')
trace2 = go.Scatter(x=[1, 2], y=[1, 2], name='(1,2)')
trace3 = go.Scatter(x=[1, 2], y=[1, 2], name='(2,1)')
trace4 = go.Scatter(x=[1, 2], y=[1, 2], name='(3,1)')
trace5 = go.Scatter(x=[1, 2], y=[1, 2], name='(5,1)')
trace6 = go.Scatter(x=[1, 2], y=[1, 2], name='(5,2)')

fig = tools.make_subplots(rows=5, cols=2,
                          specs=[[{}, {'rowspan': 2}],
                                 [{}, None],
                                 [{'rowspan': 2, 'colspan': 2}, None],
                                 [None, None],
                                 [{}, {}]],
                          print_grid=True)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 3, 1)
fig.append_trace(trace5, 5, 1)
fig.append_trace(trace6, 5, 2)

fig['layout'].update(height=600, width=600, title='specs examples')
py.iplot(fig, filename='multiple-custom-sized-subplots')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-multiplesubplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-multiplesubplot/", width="100%", height="950px", frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-multiplesubplot/code", width="100%", height=500, frameBorder="0")
```

#### Reference
All of the x-axis properties are found here: https://plot.ly/python/reference/#XAxis
All of the y-axis properties are found here: https://plot.ly/python/reference/#YAxis

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'subplots.ipynb', 'python/subplots/', 'Subplots | plotly',
    'How to make subplots in python. Examples of stacked, custom-sized, gridded, and annotated subplts.',
    title = 'Python Subplots | Examples | Plotly',
    name = 'Subplots', has_thumbnail='true', thumbnail='thumbnail/subplots.jpg', 
    language='python', page_type='example_index', redirect_from='ipython-notebooks/subplots/', 
    display_as='multiple_axes', order=2,
    ipynb='~notebook_demo/269')
```