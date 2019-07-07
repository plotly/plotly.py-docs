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
    description: How to create charts from csv files with Plotly and Python
    display_as: databases
    has_thumbnail: false
    ipynb: ~notebook_demo/84
    language: python
    layout: user-guide
    name: Plot CSV Data
    order: 1
    page_type: example_index
    permalink: python/plot-data-from-csv/
    thumbnail: thumbnail/csv.jpg
    title: Plot Data from CSV | plotly
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

#### Imports

```python
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd
```

#### A Simple Example
CSV or comma-delimited-values is a very popular format for storing structured data. In this tutorial, we will see how to plot beautiful graphs using csv data, and Pandas. We will import data from a local file `sample-data.csv` with the pandas function: `read_csv()`.

```python
df = pd.read_csv('sample-data.csv')

sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='sample-data-table')
```

```python
trace1 = go.Scatter(
                    x=df['x'], y=df['logx'], # Data
                    mode='lines', name='logx' # Additional options
                   )
trace2 = go.Scatter(x=df['x'], y=df['sinx'], mode='lines', name='sinx' )
trace3 = go.Scatter(x=df['x'], y=df['cosx'], mode='lines', name='cosx')

layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Plot data in the notebook
py.iplot(fig, filename='simple-plot-from-csv')
```

#### Plotting Data from External Source
In the next example, we will learn how to import csv data from an external source (a url), and plot it using Plotly and pandas. We are going to use this data for the example.

```python
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

df_external_source = FF.create_table(df.head())
py.iplot(df_external_source, filename='df-external-source-table')
```

```python
trace = go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)')
layout = go.Layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
fig = go.Figure(data=[trace], layout=layout)

py.iplot(fig, filename='apple-stock-prices')
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-plotfromcsvplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-plotfromcsvplot/", width="100%", height="650px", frameBorder="0")

```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-plotfromcsvplot/code", width="100%", height=500, frameBorder="0")

```

#### Reference
See https://plot.ly/python/getting-started for more information about Plotly's Python API!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'plotting-csv-data.ipynb', 'python/plot-data-from-csv/', 'Plot CSV Data',
    'How to create charts from csv files with Plotly and Python',
    title = 'Plot Data from CSV | plotly',
    thumbnail='thumbnail/csv.jpg', language='python',
    page_type='example_index', has_thumbnail='false', display_as='databases', order=1,
    ipynb= '~notebook_demo/84')
```