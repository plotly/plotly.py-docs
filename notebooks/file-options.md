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
    description: How to update your graphs in Python with the fileopt parameter.
    display_as: file_settings
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Updating Plotly Graphs
    order: 3
    page_type: example_index
    permalink: python/file-options/
    thumbnail: thumbnail/horizontal-bar.jpg
    title: Python Filenames Options | Plotly
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

#### Overwriting existing graphs and updating a graph at its unique URL


By default, Plotly will overwrite files made with the same filename. For example, if a graph named 'my plot' already exists in your account, then it will be overwritten with this new version and the URL of the graph will persist.

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2],
        y=[3, 4]
    )
]

plot_url = py.plot(data, filename='my plot')
```

#### Saving to a folder


Filenames that contain `"/"` be treated as a Plotly directory and will be saved to your Plotly account in a folder tree. For example, to save your graphs to the folder `my-graphs` use the `filename = "my-graphs/my plot"` (if it doesn't already exist it will be created)

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2],
        y=[3, 4]
    )
]

plot_url = py.plot(data, filename='my-graphs/my plot')
```

#### Creating new files


With `fileopt='new'`, Plotly will always create a new file. If a file with the same name already exists, then Plotly will append a '(1)' to the end of the filename, e.g. `new plot (1)` and create a unique URL.

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2],
        y=[3, 4]
    )
]

plot_url = py.plot(data, filename='new plot', fileopt='new')
```

#### Extending traces in an existing graph


To extend existing traces with your new data, use `fileopt='extend'`.

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2],
    y=[1, 2]
)

trace1 = go.Scatter(
    x=[1, 2],
    y=[2, 3]
)

trace2 = go.Scatter(
    x=[1, 2],
    y=[3, 4]
)

data = [trace0, trace1, trace2]

# Take 1: if there is no data in the plot, 'extend' will create new traces.
plot_url = py.plot(data, filename='extend plot', fileopt='extend')
```

Then, extend the traces with more data.

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[3, 4],
    y=[2, 1]
)

trace1 = go.Scatter(
    x=[3, 4],
    y=[3, 2]
)

trace2 = go.Scatter(
    x=[3, 4],
    y=[4, 3]
)

data = [trace0, trace1, trace2]

# Take 2: extend the traces on the plot with the data in the order supplied.
py.iplot(data, filename='extend plot', fileopt='extend')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'fileopts.ipynb', 'python/file-options/', 'Updating Plotly Graphs',
    'How to update your graphs in Python with the fileopt parameter.',
    title = 'Python Filenames Options | Plotly',
    has_thumbnail='true',
    thumbnail='thumbnail/horizontal-bar.jpg',
    language='python',
    page_type='example_index',
    display_as='file_settings',
    order=3,
    #ipynb='~notebook_demo/1'
)
```

```python

```
