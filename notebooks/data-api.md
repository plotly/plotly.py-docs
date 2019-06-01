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
    description: How to upload data to Plotly from Python with the Plotly Grid API.
    display_as: file_settings
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Plots from Grids
    order: 5
    page_type: u-guide
    permalink: python/data-api/
    thumbnail: thumbnail/table.jpg
    title: Plotly Data API
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



#### Creating a Plotly Grid
You can instantiate a grid with data by either uploading tabular data to Plotly or by creating a Plotly `grid` using the API. To upload the grid we will use `plotly.plotly.grid_ops.upload()`. It takes the following arguments:
- `grid` (Grid Object): the actual grid object that you are uploading.
- `filename` (str): name of the grid in your plotly account,
- `world_readable` (bool): if `True`, the grid is `public` and can be viewed by anyone in your files. If `False`, it is private and can only be viewed by you. 
- `auto_open` (bool): if determines if the grid is opened in the browser or not.

You can run `help(py.grid_ops.upload)` for a more detailed description of these and all the arguments.

```python
import plotly
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
from plotly.grid_objs import Column, Grid

from datetime import datetime as dt
import numpy as np
from IPython.display import Image

column_1 = Column(['a', 'b', 'c'], 'column 1')
column_2 = Column([1, 2, 3], 'column 2') # Tabular data can be numbers, strings, or dates
grid = Grid([column_1, column_2])
url = py.grid_ops.upload(grid, 
                         filename='grid_ex_'+str(dt.now()), 
                         world_readable=True, 
                         auto_open=False)
print(url)
```

#### View and Share your Grid
You can view your newly created grid at the `url`:

```python
Image('view_grid_url.png')
```

You are also able to view the grid in your list of files inside your [organize folder](https://plot.ly/organize).


#### Upload Dataframes to Plotly
Along with uploading a grid, you can upload a Dataframe as well as convert it to raw data as a grid:

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
df_head = df.head()
table = ff.create_table(df_head)
py.iplot(table, filename='dataframe_ex_preview')
```

```python
grid = Grid([Column(df[column_name], column_name) for column_name in df.columns])
url = py.grid_ops.upload(grid, filename='dataframe_ex_'+str(dt.now()), world_readable=True, auto_open=True)
print(url)
```

#### Making Graphs from Grids
Plotly graphs are usually described with data embedded in them. For example, here we place `x` and `y` data directly into our `Histogram2dContour` object:

```python
x = np.random.randn(1000)
y = np.random.randn(1000) + 1

data = [
    go.Histogram2dContour(
        x=x,
        y=y
    )
]

py.iplot(data, filename='Example 2D Histogram Contour')
```

We can also create graphs based off of references to columns of grids.  Here, we'll upload several `column`s to our Plotly account:

```python
column_1 = Column(np.random.randn(1000), 'column 1')
column_2 = Column(np.random.randn(1000)+1, 'column 2')
column_3 = Column(np.random.randn(1000)+2, 'column 3')
column_4 = Column(np.random.randn(1000)+3, 'column 4')

grid = Grid([column_1, column_2, column_3, column_4])
url = py.grid_ops.upload(grid, filename='randn_int_offset_'+str(dt.now()))
print(url)
```

```python
Image('rand_int_histogram_view.png')
```

#### Make Graph from Raw Data
Instead of placing data into `x` and `y`, we'll place our Grid columns into `xsrc` and `ysrc`:

```python
data = [
    go.Histogram2dContour(
        xsrc=grid[0],
        ysrc=grid[1]
    )
]

py.iplot(data, filename='2D Contour from Grid Data')
```

So, when you view the data, you'll see your original grid, not just the columns that compose this graph:


#### Attaching Meta Data to Grids
In [Chart Studio Enterprise](https://plot.ly/product/enterprise/), you can upload and assign free-form JSON `metadata` to any grid object. This means that you can keep all of your raw data in one place, under one grid.

If you update the original data source, in the workspace or with our API, all of the graphs that are sourced from it will be updated as well. You can make multiple graphs from a single Grid and you can make a graph from multiple grids. You can also add rows and columns to existing grids programatically.

```python
meta = {
    "Month": "November",
    "Experiment ID": "d3kbd",
    "Operator": "James Murphy",
    "Initial Conditions": {
          "Voltage": 5.5
    }
}

grid_url = py.grid_ops.upload(grid, filename='grid_with_metadata_'+str(dt.now()), meta=meta)
print(url)
```

```python
Image('metadata_view.png')
```

#### Reference

```python
help(py.grid_ops)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'grid-api.ipynb', 'python/data-api/', 'Upload Data to Plotly from Python',
    'How to upload data to Plotly from Python with the Plotly Grid API.',
    title = 'Plotly Data API', name = 'Plots from Grids', order = 5,
    language='python', has_thumbnail='true', thumbnail='thumbnail/table.jpg', display_as='file_settings'
)
```

```python

```