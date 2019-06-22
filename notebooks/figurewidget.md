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
  plotly:
    description: Introduction to the new Plotly FigureWidget
    display_as: chart_events
    has_thumbnail: true
    ipynb: ~notebook_demo/235
    language: python
    layout: user-guide
    name: Plotly FigureWidget Overview
    order: 0
    page_type: example_index
    permalink: python/figurewidget/
    thumbnail: thumbnail/ipython_widgets.jpg
    title: Plotly FigureWidget Overview
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Create a Simple FigureWidget
Create an empty FigureWidget and then view it.

```python
import plotly.graph_objs as go

f = go.FigureWidget()
f
```

<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/empty_fw.png'>


Add traces or update the layout and then watch the output above update in real time.

```python
f.add_scatter(y=[2, 1, 4, 3])
```

```python
f.add_bar(y=[1, 4, 3, 2])
```

```python
f.layout.title = 'Hello FigureWidget'
```

<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/figurewidget-create.gif'>


#### Update the Data and the Layout

```python
# update scatter data
scatter = f.data[0]
scatter.y = [3, 1, 4, 3]
```

```python
# update bar data
bar = f.data[1]
bar.y = [5, 3, 2, 8]
```

```python
f.layout.title = 'This is a new title'
```

#### Construct a FigureWidget With Data and Layout Arguments


We can construct a FigureWidget with the same arguments that `py.iplot` and `py.plot` use in order to convert an example of the latter using go.FigureWidget and we can also use a FigureWidget in the argument of iplot.


Using *Data* and *Layout*:

```python
import plotly.offline as py
py.init_notebook_mode()

trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening'])
data=[trace]
layout = go.Layout(title='Activity Heatmap')

f2 = go.FigureWidget(data,layout)

# two different ways to view f2
py.iplot(f2)
f2
```

Construct using a `go.Figure` object:

```python
figure = go.Figure(data=data, layout=layout)
f3 = go.FigureWidget(figure)
```

#### Reference


See [these Jupyter notebooks](https://github.com/jonmmease/plotly_ipywidget_notebooks) for even more FigureWidget examples.

```python
help(go.FigureWidget)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'figurewidget-overview.ipynb', 'python/figurewidget/', 'FigureWidget | Plotly',
    'Introduction to the new Plotly FigureWidget',
    title = 'Plotly FigureWidget Overview',
    name = 'Plotly FigureWidget Overview',
    uses_plotly_offline=True,
    has_thumbnail='true', thumbnail='thumbnail/ipython_widgets.jpg',
    language='python', page_type='example_index',
    display_as='chart_events', order=0,
    ipynb= '~notebook_demo/235')
```

```python

```
