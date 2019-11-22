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
    version: 3.6.8
  plotly:
    description: How to make Bar Charts in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Bar Charts
    order: 3
    page_type: example_index
    permalink: python/bar-charts/
    thumbnail: thumbnail/bar.jpg
---

### Bar chart with Plotly Express


[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](/python/px-arguments/).

With `px.bar`, each row of the DataFrame is represented as a rectangular mark.

```python
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.show()
```

```python
data_canada
```

### Customize bar chart with Plotly Express

The bar plot can be customized using keyword arguments.

```python
import plotly.express as px
data = px.data.gapminder()

data_canada = data[data.country == 'Canada']
fig = px.bar(data_canada, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=400)
fig.show()
```

When several rows share the same value of `x` (here Female or Male), the rectangles are stacked on top of one another by default.

```python
import plotly.express as px
tips = px.data.tips()
fig = px.bar(tips, x="sex", y="total_bill", color='time')
fig.show()
```

```python
# Change the default stacking
import plotly.express as px
fig = px.bar(tips, x="sex", y="total_bill", color='smoker', barmode='group',
             height=400)
fig.show()
```

#### Facetted subplots

Use the keyword arguments `facet_row` (resp. `facet_col`) to create facetted subplots, where different rows (resp. columns) correspond to different values of the dataframe column specified in `facet_row`.

```python
import plotly.express as px
fig = px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group",
             facet_row="time", facet_col="day",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "time": ["Lunch", "Dinner"]})
fig.show()
```

To learn more, see the *link to px.bar reference page*.


#### Basic Bar Chart with plotly.graph_objects

If Plotly Express does not provide a good starting point, it is also possible to use the more generic `go.Bar` function from `plotly.graph_objects`.

```python
import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
fig.show()
```

#### Grouped Bar Chart

Customize the figure using `fig.update`.

```python
import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()
```

### Stacked Bar Chart

```python
import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='stack')
fig.show()
```

### Bar Chart with Hover Text

```python
import plotly.graph_objects as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

# Use the hovertext kw argument for hover text
fig = go.Figure(data=[go.Bar(x=x, y=y,
            hovertext=['27% market share', '24% market share', '19% market share'])])
# Customize aspect
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text='January 2013 Sales Report')
fig.show()
```

### Bar Chart with Direct Labels

```python
import plotly.graph_objects as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

# Use textposition='auto' for direct text
fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',
        )])

fig.show()
```

### Rotated Bar Chart Labels

```python
import plotly.graph_objects as go

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=months,
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='Primary Product',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=months,
    y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
    name='Secondary Product',
    marker_color='lightsalmon'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()
```

### Customizing Individual Bar Colors

```python
import plotly.graph_objects as go

colors = ['lightslategray',] * 5
colors[1] = 'crimson'

fig = go.Figure(data=[go.Bar(
    x=['Feature A', 'Feature B', 'Feature C',
       'Feature D', 'Feature E'],
    y=[20, 14, 23, 25, 22],
    marker_color=colors # marker color can be a single color value or an iterable
)])
fig.update_layout(title_text='Least Used Feature')
```

### Customizing Individual Bar Widths

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(
    x=[1, 2, 3, 5.5, 10],
    y=[10, 8, 6, 4, 2],
    width=[0.8, 0.8, 0.8, 3.5, 4] # customize width here
)])

fig.show()
```

### Customizing Individual Bar Base


```python
import plotly.graph_objects as go

years = ['2016','2017','2018']

fig = go.Figure()
fig.add_trace(go.Bar(x=years, y=[500, 600, 700],
                base=[-500,-600,-700],
                marker_color='crimson',
                name='expenses'))
fig.add_trace(go.Bar(x=years, y=[300, 400, 700],
                base=0,
                marker_color='lightslategrey',
                name='revenue'
                ))

fig.show()
```

### Colored and Styled Bar Chart

In this example several parameters of the layout as customized, hence it is convenient to use directly the `go.Layout(...)` constructor instead of calling `fig.update`.

```python
import plotly.graph_objects as go

years = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
         2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]

fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=years,
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_layout(
    title='US Export of Plastic Scrap',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='USD (millions)',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()
```

### Control Bar Position in Different Subplots

To control bars positional range among several subplots, set the same axes to the same [alignmentgroup](https://plot.ly/python/reference/#bar-alignmentgroup). In the following example we have two subplots sharing an x axis with two bar traces (trace0, trace1) on the top, and one bar trace (trace2) on the bottom, that all are aligned by setting the same `alignmentgroup`. 
You also can line up bars of the same positional coordinate by setting [offsetgroup](https://plot.ly/python/reference/#bar-offsetgroup).

```python
import plotly.graph_objects as go

fig = go.Figure(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 0,
    x = [1,2,3],
    y = [2,3,4], 
    xaxis = 'x',
    yaxis = 'y2'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 1,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x',
    yaxis = 'y2'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 1,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x',
    yaxis = 'y'))


fig.update_layout(
    xaxis = {
        'anchor': 'y'},
    yaxis2 = {
        'domain': [.55,1],
        'anchor': 'x'},
    yaxis = {
        'domain': [0,.45],
        'anchor': 'x'})

fig.show()
```
Let's compare the impact of `offsetgroup` vs. `alignmentgroup`. 

```python

import plotly.graph_objects as go

fig = go.Figure(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 0,
    x = [1,2,3],
    y = [2,3,4], 
    xaxis = 'x',
    yaxis = 'y2'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 1,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x',
    yaxis = 'y2'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 2,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x',
    yaxis = 'y'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 0,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x2',
    yaxis = 'y3'))

fig.add_trace(go.Bar(
    alignmentgroup = "b",
    offsetgroup = 1,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x2',
    yaxis = 'y4'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 1,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x2',
    yaxis = 'y3'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 0,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x3',
    yaxis = 'y5'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 1,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x3',
    yaxis = 'y6'))

fig.add_trace(go.Bar(
    alignmentgroup = "a",
    offsetgroup = 1,
    x = [1,2,3],
    y = [2,3,4],
    xaxis = 'x3',
    yaxis = 'y5'))

fig.update_layout(
    xaxis = {
        'domain': [0, .35],
        'anchor': 'y',
        'title': "=alignment<br>≠offset"},
    xaxis2 = {
        'domain': [.42, .65],
        'title': "≠alignment<br>=offset",
        'anchor': 'y'
    },
    xaxis3 = {
        'domain': [.72, 1],
        'title': "=alignment<br>=offset",
        'anchor': 'y'
    },
    yaxis2 = {
        'domain': [.55,1],
        'anchor': 'x'},
    yaxis = {
        'domain': [0,.45],
        'anchor': 'x'},
    yaxis3 = {'domain': [.55,1], 'anchor': 'x2'},
    yaxis4 = {'domain': [0, .5], 'anchor': 'x2'},
    yaxis5 = {'domain': [.55, 1], 'anchor': 'x3'},
    yaxis6 = {'domain': [0, .5], 'anchor': 'x3'})

fig.show()
```

### Bar Chart with Relative Barmode

With "relative" barmode, the bars are stacked on top of one another, with negative values
below the axis, positive values above.

```python
import plotly.graph_objects as go
x = [1, 2, 3, 4]

fig = go.Figure()
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16]))
fig.add_trace(go.Bar(x=x, y=[6, -8, -4.5, 8]))
fig.add_trace(go.Bar(x=x, y=[-15, -3, 4.5, -8]))
fig.add_trace(go.Bar(x=x, y=[-1, 3, -3, -4]))

fig.update_layout(barmode='relative', title_text='Relative Barmode')
fig.show()
```

### Bar Chart with Sorted or Ordered Categories

Set `categoryorder` to `"category ascending"` or `"category descending"` for the alphanumerical order of the category names or `"total ascending"` or `"total descending"` for numerical order of values. [categoryorder](https://plot.ly/python/reference/#layout-xaxis-categoryorder) for more information. Note that sorting the bars by a particular trace isn't possible right now - it's only possible to sort by the total values. Of course, you can always sort your data _before_ plotting it if you need more customization.

This example orders the bar chart alphabetically with `categoryorder: 'category ascending'`

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
fig.show()
```

This example shows how to customise sort ordering by defining `categoryorder` to "array" to derive the ordering from the attribute `categoryarray`.

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'array', 'categoryarray':['d','a','c','b']})
fig.show()
```

This example orders the bar chart by descending value with `categoryorder: 'total descending'`

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
fig.show()
```

### Horizontal Bar Charts

See examples of horizontal bar charts [here](https://plot.ly/python/horizontal-bar-charts/).


### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-barplot) is also show below and can easily be deployed to a PaaS (platform as a service).

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
