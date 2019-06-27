---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.3
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
from plotly.subplots import make_subplots
import plotly.graph_objs as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    row=1, col=2
)

fig['layout'].update(height=600, width=800, title_text='i <3 subplots')
fig.show()
```

#### Multiple Subplots

```python
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
fig.show()
```

#### Multiple Subplots with Titles

```python
from plotly.subplots import make_subplots
import plotly.graph_objs as go

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Plot 1', 'Plot 2', 'Plot 3', 'Plot 4'))

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
              row=1, col=1)

fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
              row=1, col=2)

fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]),
              row=2, col=1)

fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
              row=2, col=2)

fig.update_layout(height=600, width=600,
                  title_text='Multiple Subplots with Titles')

fig.show()
```

#### Simple Subplot with Annotations

```python
from plotly.subplots import make_subplots
import plotly.graph_objs as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[4, 5, 6],
        mode='markers+text',
        text=['Text A', 'Text B', 'Text C'],
        textposition='bottom center'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=[20, 30, 40],
        y=[50, 60, 70],
        mode='markers+text',
        text=['Text D', 'Text E', 'Text F'],
        textposition='bottom center'
    ),
    row=1, col=2
)

fig.update_layout(height=600, width=800, title_text='i <3 annotations and subplots')

fig.show()
```

#### Side by Side Subplot

```python
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
fig.show()
```

#### Customizing Subplot Axes

```python
from plotly.subplots import make_subplots
import plotly.graph_objs as go

# Initialize figure with subplots
fig = make_subplots(
    rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2', 'Plot 3', 'Plot 4')
)

# Add traces
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]), row=1, col=2)
fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]), row=2, col=1)
fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]), row=2, col=2)

# Update xaxis properties
fig.update_xaxes(title='xaxis 1 title', row=1, col=1)
fig.update_xaxes(title='xaxis 2 title', range=[10, 50], row=1, col=2)
fig.update_xaxes(title='xaxis 3 title', showgrid=False, row=2, col=1)
fig.update_xaxes(title='xaxis 4 title', type='log', row=2, col=2)

# Update yaxis properties
fig.update_yaxes(title='yaxis 1 title', row=1, col=1)
fig.update_yaxes(title='yaxis 2 title', range=[40, 80], row=1, col=2)
fig.update_yaxes(title='yaxis 3 title', showgrid=False, row=2, col=1)
fig.update_yaxes(title='yaxis 4 title', row=2, col=2)

# Update title and height
fig.update_layout(title_text='Customizing Subplot Axes', height=800)

fig.show()
```

#### Subplots with Shared X-Axes

```python
from plotly import tools
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
fig.show()
```

#### Subplots with Shared Y-Axes

```python
from plotly import tools
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
fig.show()
```

#### Subplots with Shared Axes

```python
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
fig.show()
```

#### Stacked Subplots

```python
from plotly import tools
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
fig.show()
```

#### Stacked Subplots with a Shared X-Axis

```python
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
fig.show()
```

#### Custom Sized Subplot with Subplot Titles

```python
from plotly import tools
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
fig.show()
```

#### Multiple Custom Sized Subplots

```python
from plotly import tools
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
fig.show()
```

#### Reference
All of the x-axis properties are found here: https://plot.ly/python/reference/#XAxis
All of the y-axis properties are found here: https://plot.ly/python/reference/#YAxis

```python
from plotly.subplots import make_subplots
help(make_subplots)
```

```python

```
