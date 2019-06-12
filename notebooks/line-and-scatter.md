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
    version: 3.6.7
  plotly:
    description: How to make scatter plots in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/2
    language: python
    layout: user-guide
    name: Scatter Plots
    order: 2
    page_type: example_index
    permalink: python/line-and-scatter/
    redirect_from: python/line-and-scatter-plots-tutorial/
    thumbnail: thumbnail/line-and-scatter.jpg
    title: Python Scatter Plots | plotly
---

## Scatter plot with plotly express

Plotly express functions take as argument a tidy [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html). With ``px.scatter``, each data point is represented as a marker point, which location is given by the `x` and `y` columns.

```python
import plotly_express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length")
fig.show()
```

#### Set size and color with column names

Note that `color` and `info` data are added to hover information. You can add other columns to hover data with the `hover_data` argument of `px.scatter`.

```python
import plotly_express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length')
fig.show()
```

## Line plot with plotly express

```python
import plotly_express as px
gapminder = px.data.gapminder().query("continent == 'Oceania'")
px.line(gapminder, x='year', y='lifeExp', color='country')
```

## Scatter and line plot with go.Scatter

When data are not available as tidy dataframes, it is possible to use the more generic `go.Scatter` function from `plotly.graph_objs`. Whereas `plotly_express` has two functions `scatter` and `line`, `go.Scatter` can be used both for plotting points (makers) or lines, depending on the value of `mode`. The different options of `go.Scatter` are documented in its [reference page](https://plot.ly/python/reference/#scatter ).


#### Simple Scatter Plot

```python
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(x=random_x, y=random_y,
                   mode='markers')

fig = go.Figure(data=[trace])
fig.show()
```

#### Line and Scatter Plots

Use `mode` argument to choose between markers, lines, or a combination of both. For more options about line plots, see also the [line charts notebook](https://plot.ly/python/line-charts/) and the [filled area plots notebook](https://plot.ly/python/filled-area-plots/).

```python
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Create traces
trace0 = go.Scatter(x=random_x, y=random_y0,
                    mode='markers',
                    name='markers')
trace1 = go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers')
trace2 = go.Scatter(x=random_x, y=random_y2,
                    mode='lines',
                    name='lines')

fig = go.Figure(data=[trace0, trace1, trace2])
fig.show()
```

#### Bubble Scatter Plots

In [bubble charts](https://en.wikipedia.org/wiki/Bubble_chart), a third dimension of the data is shown through the size of markers. For more examples, see the [bubble chart notebook](https://plot.ly/python/bubble-charts/)  

```python
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100], 
                color=[0, 1, 2, 3])
)

fig = go.Figure(data=[trace0])
fig.show()
```

#### Style Scatter Plots

```python
import plotly.graph_objs as go
import numpy as np

N = 500

trace0 = go.Scatter(
    x = np.random.randn(N), y = np.random.randn(N)+2,
    name='Above',
    mode='markers',
    marker=dict(
        size=10,
        color='rgba(152, 0, 0, .8)',
        line=dict(width=2, color='rgb(0, 0, 0)')
    )
)

trace1 = go.Scatter(
    x=np.random.randn(N),
    y=np.random.randn(N)-2,
    name='Below',
    mode='markers',
    marker=dict(size=10, color='rgba(255, 182, 193, .9)', line_width = 2)
)

layout = go.Layout(title='Styled Scatter',
                   yaxis_zeroline=False, xaxis_zeroline=False)

fig = go.Figure(data=[trace0, trace1], layout=layout)
fig.show()
```

#### Data Labels on Hover

```python
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd

l= []
y= []
data= pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
# Setting colors for plot.
N= 53
c= ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

for i in range(int(N)):
    y.append((2000+i))
    trace0 = go.Scatter(
        x=data['Rank'],
        y=data['Population']+(i*1000000),
        mode='markers',
        marker=dict(size=14, line_width=1, color=c[i], opacity=0.3),
        name=y[i],
        text=data['State']) # The hover text goes here... 
    l.append(trace0);

layout= go.Layout(
    title='Stats of USA States',
    hovermode='closest',
    xaxis=dict(title='Population', zeroline= False, gridwidth= 2),
    yaxis=dict(title='Rank', gridwidth= 2),
    showlegend= False
)
fig = go.Figure(data=l, layout=layout)
fig.show()
```

#### Scatter with a Color Dimension

```python
import plotly.graph_objs as go
import numpy as np

trace1 = go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color=np.random.randn(500), #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )
)
fig = go.Figure(data=[trace1])
fig.show()
```

#### Large Data Sets

Now in Ploty you can implement WebGL with `Scattergl()` in place of `Scatter()` <br>
for increased speed, improved interactivity, and the ability to plot even more data!

```python
import plotly.graph_objs as go
import numpy as np

N = 100000
trace = go.Scattergl(
    x = np.random.randn(N),
    y = np.random.randn(N),
    mode='markers',
    marker=dict(
        color=np.random.randn(N),
        colorscale='Viridis',
        line_width=1
    )
)
fig = go.Figure(data=[trace])
fig.show()
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-linescatterplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-linescatterplot/", width="100%",height="750px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-linescatterplot/code", width="100%",height=500, frameBorder="0")
```

### Reference
See https://plot.ly/python/reference/#scatter or https://plot.ly/python/reference/#scattergl for more information and chart attribute options!

