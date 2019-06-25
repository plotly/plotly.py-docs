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
    description: How to adjust axes properties in python. Seven examples of linear
      and logarithmic axes, axes titles, and styling and coloring axes and grid lines.
    display_as: layout_opt
    has_thumbnail: true
    ipynb: ~notebook_demo/95
    language: python
    layout: user-guide
    name: Axes
    order: 3
    page_type: example_index
    permalink: python/axes/
    thumbnail: thumbnail/your-tutorial-chart.jpg
    title: Axes | plotly
---

#### Toggling Axes Lines, Ticks, Labels, and Autorange

```python
import plotly.graph_objects as go

fig = go.Figure(
#     data=[go.Scatter(y=[8, 7, 6, 5, 4, 3, 2, 1, 0]),
#           go.Scatter(y=[0, 1, 2, 3, 4, 5, 6, 7, 8])],
)


fig.update_xaxes(
    showgrid=False,
    zeroline=False,
    showline=False,
    showticklabels=False,
)
# fig.update_yaxes(
#     showgrid=False,
#     zeroline=False,
#     showline=False,
#     showticklabels=False,
# )
fig.show()
```

#### Tick Placement, Color, and Style

```python
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
)
trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        tickmode='linear',
        ticks='outside',
        tick0=0,
        dtick=0.25,
        ticklen=8,
        tickwidth=4,
        tickcolor='#000'
    ),
    yaxis=dict(
        tickmode='linear',
        ticks='outside',
        tick0=0,
        dtick=0.25,
        ticklen=8,
        tickwidth=4,
        tickcolor='#000'
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Set and Style Axes Title Labels and Ticks

```python
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
)
trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        title='AXIS TITLE',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        tickangle=45,
        tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='all'
    ),
    yaxis=dict(
        title='AXIS TITLE',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        tickangle=45,
        tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='all'
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Styling and Coloring Axes and the Zero-Line

```python
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
)
trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        mirror='ticks',
        gridcolor='#bdbdbd',
        gridwidth=2,
        zerolinecolor='#969696',
        zerolinewidth=4,
        linecolor='#636363',
        linewidth=6
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        mirror='ticks',
        gridcolor='#bdbdbd',
        gridwidth=2,
        zerolinecolor='#969696',
        zerolinewidth=4,
        linecolor='#636363',
        linewidth=6
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Setting the Range of Axes Manually

```python
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
)
trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        range=[2, 5]
    ),
    yaxis=dict(
        range=[2, 5]
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Subcategory Axes

```python
import plotly.graph_objects as go

trace1 = go.Box(
  x = [2, 3, 1, 5],
  y = ["A", "A", "A", "A"],
  line = dict(color = 'gray'),
  name = "A",
  orientation = "h"
)

trace2 = go.Box(
  x = [8, 3, 6, 5],
  y = ["B", "B", "B", "B"],
  line = dict(color = 'gray'),
  name = "B",
  orientation = "h"
)

trace3 = go.Box(
  x = [2, 3, 2, 5],
  y = ["C", "C", "C", "C"],
  line = dict(color = 'gray'),
  name = "C",
  orientation = "h"
)

trace4 = go.Box(
  x = [7.5, 3, 6, 4],
  y = ["D", "D", "D", "D"],
  line = dict(color = 'gray'),
  name = "D",
  orientation = "h"
)

data = [trace1, trace2, trace3, trace4]

layout = go.Layout(
  annotations = [
    dict(
      x = -0.0951769406393,
      y = 1.06972670892,
      showarrow = False,
      text = "Subgroup",
      xref = "paper",
      yref = "paper"
    ),
    dict(
      x = -0.235516552511,
      y = 1.07060587474,
      showarrow = False,
      text = "Group",
      xref = "paper",
      yref = "paper"
    ),
    dict(
      x = -0.235516552511,
      y = 0.922906017856,
      showarrow = False,
      text = "One",
      xref = "paper",
      yref = "paper"
    ),
    dict(
      x = -0.235516552511,
      y = 0.375,
      showarrow = False,
      text = "Two",
      xref = "paper",
      yref = "paper"
    )
  ],
  height = 400,
  hovermode = "closest",
  legend = dict(
    x = 0.986145833333,
    y = 0.936263886049
  ),
  margin = dict(
    r = 10,
    t = 25,
    b = 40,
    l = 110
  ),
  shapes = [
    dict(
      line = dict(
        color = "rgba(68, 68, 68, 0.5)",
        width = 1
      ),
      type = "line",
      x0 = -0.3,
      x1 = 1.2,
      xref = "paper",
      y0 = 0.5,
      y1 = 0.5,
      yref = "paper"
    ),
    dict(
      line = dict(
        color = "rgba(68, 68, 68, 0.63)",
        width = 1
      ),
      type = "line",
      x0 = -0.3,
      x1 = 1.2,
      xref = "paper",
      y0 = 1,
      y1 = 1,
      yref = "paper"
    )
  ],
  showlegend = True,
  title = "",
  width = 600,
  xaxis = dict(
    domain = [0, 1]
  ),
  yaxis = dict(
    autorange = True,
    categoryorder = "category descending",
    domain = [0, 1],
    range = [-0.5, 3.5],
    showline = True,
    title = "",
    type = "category"
  )
)

fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Logarithmic Axes

```python
import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
)
trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        type='log',
        autorange=True
    ),
    yaxis=dict(
        type='log',
        autorange=True
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

### Fixed Ratio Axes

```python
import plotly.graph_objects as go

trace0 = go.Scatter(
  x = [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
  y = [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
)

trace1 = go.Scatter(
  x = [0,1,2,3],
  y = [1,2,4,8],
  yaxis = "y2"
)

trace2 = go.Scatter(
  x = [1,10,100,10,1],
  y = [0,1,2,3,4],
  xaxis = "x2",
  yaxis ="y3",
)

trace3 = go.Scatter(
  x = [1,100,30,80,1],
  y = [1,1.5,2,2.5,3],
  xaxis = "x2",
  yaxis = "y4"
)

data = [trace0,trace1,trace2,trace3]

layout = go.Layout(
    width = 800,
    height = 500,
    title = "fixed-ratio axes",
    xaxis = dict(
      nticks = 10,
      domain = [0, 0.45],
      title = "shared X axis"
    ),
    yaxis = dict(
      scaleanchor = "x",
      domain = [0, 0.45],
      title = "1:1"
    ),
    yaxis2 = dict(
      scaleanchor = "x",
      scaleratio = 0.2,
      domain = [0.55,1],
      title = "1:5"
    ),
    xaxis2 = dict(
      type = "log",
      domain = [0.55, 1],
      anchor = "y3",
      title = "unconstrained log X"
    ),
    yaxis3 = dict(
      domain = [0, 0.45],
      anchor = "x2",
      title = "Scale matches ->"
    ),
    yaxis4 = dict(
      scaleanchor = "y3",
      domain = [0.55, 1],
      anchor = "x2",
      title = "Scale matches <-"
    ),
    showlegend= False
)

fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Reversed Axes

```python
import plotly.graph_objects as go

data = [
    go.Scatter(
        x=[1, 2],
        y=[1, 2]
    )
]
layout = go.Layout(
    xaxis=dict(
        autorange='reversed'
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Reversed Axes with Range ( Min/Max ) Specified

```python
import plotly.graph_objects as go

import numpy as np

x = np.linspace(0, 10, 100)
y = np.random.randint(1, 100, 100)

trace = go.Scatter(x=x, y=y, mode='markers')
data = [trace]
layout = go.Layout(title='Reversed Axis with Min/Max', xaxis=dict(range=[10, 0]))

fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### <code>nonnegative</code>, <code>tozero</code>, and <code>normal</code> Rangemode

```python
import plotly.graph_objects as go

data = [
    go.Scatter(
        x=[2, 4, 6],
        y=[-3, 0, 3]
    )
]
layout = go.Layout(
    showlegend=False,
    xaxis=dict(
        rangemode='tozero',
        autorange=True
    ),
    yaxis=dict(
        rangemode='nonnegative',
        autorange=True
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Enumerated Ticks with Tickvals and Ticktext

```python
import plotly.graph_objects as go

import pandas as pd

# get and filter apple data
apple_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
apple_df_2016 = apple_df[apple_df.Date < '2017'][apple_df.Date > '2016']

# get clean and filter tesla data
tesla_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv')
tesla_df.date = pd.to_datetime(tesla_df.date)
tesla_df_2016 = tesla_df[tesla_df.date < '2017'][tesla_df.date > '2016']

# set x-axis labels and their corresponding data values
labels = ['End of Q1', 'End of Q2', 'End of Q3', 'End of Q4']
tickvals = ['2016-04-01', '2016-07-01', '2016-10-01', apple_df_2016.Date.max()]

data=[
    go.Scatter(
        x = apple_df_2016.Date,
        y=apple_df_2016['AAPL.High'],
        name='Apple',
        marker=dict(color='#851e52'),
    ),
    go.Scatter(
        x=tesla_df_2016.date,
        y=tesla_df_2016.high,
        name='Tesla',
        yaxis='y2',
        marker=dict(color='#d3560e'),
    ),
]

layout = go.Layout(
    title='2016 Quarterly Stock Trends',
    xaxis=go.layout.XAxis(
        ticktext=labels,
        tickvals=tickvals
    ),
    yaxis2= dict(
        overlaying='y',
        side='right',
        showgrid=False,
    )
)
fig = go.Figure(data, layout)
fig.show()
```

#### Reference
See https://plot.ly/python/reference/#layout-xaxis and https://plot.ly/python/reference/#layout-yaxis for more information and chart attribute options!
