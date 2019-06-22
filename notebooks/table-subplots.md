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
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to create a subplot with tables and charts in Python with Plotly.
    display_as: multiple_axes
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Table and Chart Subplots
    order: 11
    page_type: u-guide
    permalink: python/table-subplots/
    thumbnail: thumbnail/table_subplots.jpg
    title: Table and Chart Subplots | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Note: Tables are available in version <b>2.1.0+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Import CSV Data

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import re

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv')

# remove min:sec:millisec from dates
for i, row in enumerate(df['Date']):
    p = re.compile(' 00:00:00')
    datetime = p.split(df['Date'][i])[0]
    df.iloc[i, 1] = datetime

table = go.Table(
    columnwidth=[0.4, 0.47, 0.48, 0.4, 0.4, 0.45, 0.5, 0.6],
    header=dict(
        #values=list(df.columns[1:]),
        values=['Date', 'Number<br>Transactions', 'Output<br>Volume (BTC)',
                'Market<br>Price', 'Hash<br>Rate', 'Cost per<br>trans-USD',
                'Mining<br>Revenue-USD', 'Trasaction<br>fees-BTC'],
        font=dict(size=10),
        line = dict(color='rgb(50, 50, 50)'),
        align = 'left',
        fill = dict(color='#d562be'),
    ),
    cells=dict(
        values=[df[k].tolist() for k in df.columns[1:]],
        line = dict(color='rgb(50, 50, 50)'),
        align = 'left',
        fill = dict(color='#f5f5fa')
    )
)
py.iplot([table], filename='table-of-mining-data')
```

#### Table and Right Aligned Plots
In Plotly there is no native way to insert a Plotly Table into a Subplot. To do this, create your own `Layout` object and defining multiple `xaxis` and `yaxis` to split up the chart area into different domains. Then for the traces you wish to insert in your final chart, set their `xaxis` and `yaxis` individually to map to the domains definied in the `Layout`. See the example below to see how to align 3 Scatter plots to the right and a Table on the top.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd

table_trace1 = go.Table(
    domain=dict(x=[0, 0.5],
                y=[0, 1.0]),
    columnwidth = [30] + [33, 35, 33],
    columnorder=[0, 1, 2, 3, 4],
    header = dict(height = 50,
                  values = [['<b>Date</b>'],['<b>Number<br>transactions</b>'],
                            ['<b>Output<br>volume(BTC)</b>'], ['<b>Market<br>Price</b>']],
                  line = dict(color='rgb(50, 50, 50)'),
                  align = ['left'] * 5,
                  font = dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                  fill = dict(color='#d562be')),
    cells = dict(values = [df[k].tolist() for k in
                          ['Date', 'Number-transactions', 'Output-volume(BTC)', 'Market-price']],
                 line = dict(color='#506784'),
                 align = ['left'] * 5,
                 font = dict(color=['rgb(40, 40, 40)'] * 5, size=12),
                 format = [None] + [", .2f"] * 2 + [',.4f'],
                 prefix = [None] * 2 + ['$', u'\u20BF'],
                 suffix=[None] * 4,
                 height = 27,
                 fill = dict(color=['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']))
)

trace1=go.Scatter(
    x=df['Date'],
    y=df['Hash-rate'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=2, color='#9748a1'),
    name='hash-rate-TH/s'
)

trace2=go.Scatter(
    x=df['Date'],
    y=df['Mining-revenue-USD'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=2, color='#b04553'),
    name='mining revenue'
)

trace3=go.Scatter(
    x=df['Date'],
    y=df['Transaction-fees-BTC'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=2, color='#af7bbd'),
    name='transact-fee'
)

axis=dict(
    showline=True,
    zeroline=False,
    showgrid=True,
    mirror=True,
    ticklen=4,
    gridcolor='#ffffff',
    tickfont=dict(size=10)
)

layout1 = dict(
    width=950,
    height=800,
    autosize=False,
    title='Bitcoin mining stats for 180 days',
    margin = dict(t=100),
    showlegend=False,
    xaxis1=dict(axis, **dict(domain=[0.55, 1], anchor='y1', showticklabels=False)),
    xaxis2=dict(axis, **dict(domain=[0.55, 1], anchor='y2', showticklabels=False)),
    xaxis3=dict(axis, **dict(domain=[0.55, 1], anchor='y3')),
    yaxis1=dict(axis, **dict(domain=[0.66, 1.0], anchor='x1', hoverformat='.2f')),
    yaxis2=dict(axis, **dict(domain=[0.3 + 0.03, 0.63], anchor='x2', tickprefix='$', hoverformat='.2f')),
    yaxis3=dict(axis, **dict(domain=[0.0, 0.3], anchor='x3', tickprefix=u'\u20BF', hoverformat='.2f')),
    plot_bgcolor='rgba(228, 222, 249, 0.65)'
)

fig1 = dict(data=[table_trace1, trace1, trace2, trace3], layout=layout1)
py.iplot(fig1, filename='table-right-aligned-plots')
```

#### Vertical Table and Graph Subplot

```python
import plotly.plotly as py
import plotly.graph_objs as go

table_trace2 = go.Table(
    domain=dict(x=[0, 1],
                y=[0.7, 1.0]),
    columnwidth=[1, 2, 2, 2],
    columnorder=[0, 1, 2, 3, 4],
    header = dict(height = 50,
                  values = [['<b>Date</b>'],['<b>Hash Rate, TH/sec</b>'],
                            ['<b>Mining revenue</b>'], ['<b>Transaction fees</b>']],
                  line = dict(color='rgb(50, 50, 50)'),
                  align = ['left'] * 5,
                  font = dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                  fill = dict(color='#d562be')),
    cells = dict(values = [df[k].tolist() for k in ['Date', 'Hash-rate', 'Mining-revenue-USD', 'Transaction-fees-BTC']],
                 line = dict(color='#506784'),
                 align = ['left'] * 5,
                 font = dict(color=['rgb(40, 40, 40)'] * 5, size=12),
                 format = [None] + [", .2f"] * 2 + [',.4f'],
                 prefix = [None] * 2 + ['$', u'\u20BF'],
                 suffix=[None] * 4,
                 height = 27,
                 fill = dict(color=['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']))
)

trace4=go.Scatter(
    x=df['Date'],
    y=df['Hash-rate'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=2, color='#9748a1'),
    name='hash-rate-TH/s'
)

trace5=go.Scatter(
    x=df['Date'],
    y=df['Mining-revenue-USD'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=2, color='#b04553'),
    name='mining revenue'
)

trace6=go.Scatter(
    x=df['Date'],
    y=df['Transaction-fees-BTC'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=2, color='#af7bbd'),
    name='transact-fee'
)

axis=dict(
    showline=True,
    zeroline=False,
    showgrid=True,
    mirror=True,
    ticklen=4,
    gridcolor='#ffffff',
    tickfont=dict(size=10)
)

layout2 = dict(
    width=950,
    height=800,
    autosize=False,
    title='Bitcoin mining stats for 180 days',
    margin = dict(t=100),
    showlegend=False,
    xaxis1=dict(axis, **dict(domain=[0, 1], anchor='y1', showticklabels=False)),
    xaxis2=dict(axis, **dict(domain=[0, 1], anchor='y2', showticklabels=False)),
    xaxis3=dict(axis, **dict(domain=[0, 1], anchor='y3')),
    yaxis1=dict(axis, **dict(domain=[2 * 0.21 + 0.02 + 0.02, 0.68], anchor='x1', hoverformat='.2f')),
    yaxis2=dict(axis, **dict(domain=[0.21 + 0.02, 2 * 0.21 + 0.02], anchor='x2', tickprefix='$', hoverformat='.2f')),
    yaxis3=dict(axis, **dict(domain=[0.0, 0.21], anchor='x3', tickprefix=u'\u20BF', hoverformat='.2f')),
    plot_bgcolor='rgba(228, 222, 249, 0.65)'
)

fig2 = dict(data=[table_trace2, trace4, trace5, trace6], layout=layout2)
py.iplot(fig2, filename='vertical-stacked-subplot-tables')
```

#### Reference
See  https://plot.ly/python/reference/#table for more information regarding chart attributes! <br>
For examples of Plotly Tables, see: https://plot.ly/python/table/

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'table-subplots.ipynb', 'python/table-subplots/', 'Table and Chart Subplots',
    'How to create a subplot with tables and charts in Python with Plotly.',
    title = 'Table and Chart Subplots | plotly',
    has_thumbnail='true', thumbnail='thumbnail/table_subplots.jpg',
    language='python',
    display_as='multiple_axes', order=11)
```

```python

```
