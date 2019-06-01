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
    description: How to make Bar Charts in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/186
    language: python
    layout: user-guide
    name: Bar Charts
    order: 4
    page_type: example_index
    permalink: python/bar-charts/
    thumbnail: thumbnail/bar.jpg
    title: Bar Charts | plotly
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

#### Basic Bar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    )]

py.iplot(data, filename='basic-bar')
```

#### Grouped Bar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='grouped-bar')
```

### Stacked Bar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='stacked-bar')
```

### Bar Chart with Hover Text

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['Product A', 'Product B', 'Product C'],
    y=[20, 14, 23],
    text=['27% market share', '24% market share', '19% market share'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

data = [trace0]
layout = go.Layout(
    title='January 2013 Sales Report',
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='text-hover-bar')
```

### Bar Chart with Direct Labels

```python
import plotly.plotly as py
import plotly.graph_objs as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

data = [go.Bar(
            x=x,
            y=y,
            text=y,
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

py.iplot(data, filename='bar-direct-labels')
```

### Grouped Bar Chart with Direct Labels

```python
import plotly.plotly as py
import plotly.graph_objs as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]
y2 = [16,12,27]

trace1 = go.Bar(
    x=x,
    y=y,
    text=y,
    textposition = 'auto',
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5),
        ),
    opacity=0.6
)

trace2 = go.Bar(
    x=x,
    y=y2,
    text=y2,
    textposition = 'auto',
    marker=dict(
        color='rgb(58,200,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5),
        ),
    opacity=0.6
)

data = [trace1,trace2]

py.iplot(data, filename='grouped-bar-direct-labels')
```

### Rotated Bar Chart Labels

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='Primary Product',
    marker=dict(
        color='rgb(49,130,189)'
    )
)
trace1 = go.Bar(
    x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
    name='Secondary Product',
    marker=dict(
        color='rgb(204,204,204)',
    )
)

data = [trace0, trace1]
layout = go.Layout(
    xaxis=dict(tickangle=-45),
    barmode='group',
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='angled-text-bar')
```

### Customizing Individual Bar Colors

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['Feature A', 'Feature B', 'Feature C',
       'Feature D', 'Feature E'],
    y=[20, 14, 23, 25, 22],
    marker=dict(
        color=['rgba(204,204,204,1)', 'rgba(222,45,38,0.8)',
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)']),
)

data = [trace0]
layout = go.Layout(
    title='Least Used Feature',
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='color-bar')
```

### Customizing Individual Bar Widths

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=[1, 2, 3, 5.5, 10],
    y=[10, 8, 6, 4, 2],
    width = [0.8, 0.8, 0.8, 3.5, 4]
)

data = [trace0]

fig = go.Figure(data=data)
py.iplot(fig, filename='width-bar')
```

### Customizing Individual Bar Base

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Bar(
        x = ['2016','2017','2018'],
        y = [500,600,700],
        base = [-500,-600,-700],
        marker = dict(
          color = 'red'
        ),
        name = 'expenses'
    ),
    go.Bar(
        x = ['2016','2017','2018'],
        y = [300,400,700],
        base = 0,
        marker = dict(
          color = 'blue'
        ),
        name = 'revenue'
    )
]


fig = go.Figure(data=data)
py.iplot(fig, filename='base-bar')
```

### Colored and Styled Bar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
       2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
    y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
       350, 430, 474, 526, 488, 537, 500, 439],
    name='Rest of world',
    marker=dict(
        color='rgb(55, 83, 109)'
    )
)
trace2 = go.Bar(
    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
       2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
    y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
       299, 340, 403, 549, 499],
    name='China',
    marker=dict(
        color='rgb(26, 118, 255)'
    )
)
data = [trace1, trace2]
layout = go.Layout(
    title='US Export of Plastic Scrap',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='USD (millions)',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='style-bar')
```

### Waterfall Bar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

x_data = ['Product<br>Revenue', 'Services<br>Revenue',
          'Total<br>Revenue', 'Fixed<br>Costs',
          'Variable<br>Costs', 'Total<br>Costs', 'Total']
y_data = [400, 660, 660, 590, 400, 400, 340]
text = ['$430K', '$260K', '$690K', '$-120K', '$-200K', '$-320K', '$370K']

# Base
trace0 = go.Bar(
    x=x_data,
    y=[0, 430, 0, 570, 370, 370, 0],
    marker=dict(
        color='rgba(1,1,1, 0.0)',
    )
)
# Revenue
trace1 = go.Bar(
    x=x_data,
    y=[430, 260, 690, 0, 0, 0, 0],
    marker=dict(
        color='rgba(55, 128, 191, 0.7)',
        line=dict(
            color='rgba(55, 128, 191, 1.0)',
            width=2,
        )
    )
)
# Costs
trace2 = go.Bar(
    x=x_data,
    y=[0, 0, 0, 120, 200, 320, 0],
    marker=dict(
        color='rgba(219, 64, 82, 0.7)',
        line=dict(
            color='rgba(219, 64, 82, 1.0)',
            width=2,
        )
    )
)
# Profit
trace3 = go.Bar(
    x=x_data,
    y=[0, 0, 0, 0, 0, 0, 370],
    marker=dict(
        color='rgba(50, 171, 96, 0.7)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=2,
        )
    )
)
data = [trace0, trace1, trace2, trace3]
layout = go.Layout(
    title='Annual Profit- 2015',
    barmode='stack',
    paper_bgcolor='rgba(245, 246, 249, 1)',
    plot_bgcolor='rgba(245, 246, 249, 1)',
    showlegend=False
)

annotations = []

for i in range(0, 7):
    annotations.append(dict(x=x_data[i], y=y_data[i], text=text[i],
                                  font=dict(family='Arial', size=14,
                                  color='rgba(245, 246, 249, 1)'),
                                  showarrow=False,))
    layout['annotations'] = annotations

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='waterfall-bar-profit')
```

### Bar Chart with Relative Barmode

```python
x = [1, 2, 3, 4]

trace1 = {
  'x': x,
  'y': [1, 4, 9, 16],
  'name': 'Trace1',
  'type': 'bar'
};
trace2 = {
  'x': x,
  'y': [6, -8, -4.5, 8],
  'name': 'Trace2',
  'type': 'bar'
};
trace3 = {
  'x': x,
  'y': [-15, -3, 4.5, -8],
  'name': 'Trace3',
  'type': 'bar'
 }
 
trace4 = {
  'x': x,
  'y': [-1, 3, -3, -4],
  'name': 'Trace4',
  'type': 'bar'
 }
 
data = [trace1, trace2, trace3, trace4];
layout = {
  'xaxis': {'title': 'X axis'},
  'yaxis': {'title': 'Y axis'},
  'barmode': 'relative',
  'title': 'Relative Barmode'
};
py.iplot({'data': data, 'layout': layout}, filename='barmode-relative')
```

### Horizontal Bar Charts
See examples of horizontal bar charts [here](https://plot.ly/python/horizontal-bar-charts/).


### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-barplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-barplot/", width="100%", height="650px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-barplot/code", width="80%", height=500, frameBorder="0")
```

### Reference
See https://plot.ly/python/reference/#bar for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'bars.ipynb', 'python/bar-charts/', 'Python Bar Charts | plotly',
    'How to make Bar Charts in Python with Plotly.',
    title = 'Bar Charts | plotly',
    name = 'Bar Charts',
    thumbnail='thumbnail/bar.jpg', language='python',
    page_type='example_index', has_thumbnail='true', display_as='basic', order=4,
    ipynb= '~notebook_demo/186')
```