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
    v4upgrade: true
---

#### Import CSV Data

```python
import plotly.graph_objects as go

import pandas as pd
import re

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv')

# remove min:sec:millisec from dates
for i, row in enumerate(df['Date']):
    p = re.compile(' 00:00:00')
    datetime = p.split(df['Date'][i])[0]
    df.iloc[i, 1] = datetime

fig = go.Figure(go.Table(
    columnwidth=[0.4, 0.47, 0.48, 0.4, 0.4, 0.45, 0.5, 0.6],
    header=dict(
        values=['Date', 'Number<br>Transactions', 'Output<br>Volume (BTC)',
                'Market<br>Price', 'Hash<br>Rate', 'Cost per<br>trans-USD',
                'Mining<br>Revenue-USD', 'Trasaction<br>fees-BTC'],
        font_size=10,
        font_color='white',
        line_color='rgb(50, 50, 50)',
        align = 'left',
        fill_color='mediumpurple',
    ),
    cells=dict(
        values=[df[k].tolist() for k in df.columns[1:]],
        line_color='rgb(50, 50, 50)',
        align = 'left',
        fill_color='white'
    )
))
fig.show()
```

#### Table and Right Aligned Plots
In Plotly there is no native way to insert a Plotly Table into a Subplot. To do this, create your own `Layout` object and defining multiple `xaxis` and `yaxis` to split up the chart area into different domains. Then for the traces you wish to insert in your final chart, set their `xaxis` and `yaxis` individually to map to the domains definied in the `Layout`. See the example below to see how to align 3 Scatter plots to the right and a Table on the top.

```python
import plotly.graph_objects as go

import numpy as np
import pandas as pd

fig = go.Figure()

fig.add_trace(go.Table(
    domain=dict(x=[0, 0.5], y=[0, 1.0]),
    columnwidth = [30] + [33, 35, 33],
    columnorder=[0, 1, 2, 3, 4],
    header = dict(height = 50,
                  values = [['<b>Date</b>'],['<b>Number<br>transactions</b>'],
                            ['<b>Output<br>volume(BTC)</b>'], ['<b>Market<br>Price</b>']],
                  line_color='rgb(50, 50, 50)',
                  align = ['left'] * 5,
                  font = dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                  fill_color='#d562be'),
    cells = dict(values = [df[k].tolist() for k in
                          ['Date', 'Number-transactions', 'Output-volume(BTC)', 'Market-price']],
                 line_color='#506784',
                 align = ['left'] * 5,
                 font = dict(color=['rgb(40, 40, 40)'] * 5, size=12),
                 format = [None] + [", .2f"] * 2 + [',.4f'],
                 prefix = [None] * 2 + ['$', u'\u20BF'],
                 suffix=[None] * 4,
                 height = 27,
                 fill_color=['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)'])
))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Hash-rate'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=2, color='#9748a1'),
    name='hash-rate-TH/s'
))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Mining-revenue-USD'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=2, color='#b04553'),
    name='mining revenue'
))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Transaction-fees-BTC'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=2, color='#af7bbd'),
    name='transact-fee'
))

axis=dict(
    showline=True,
    zeroline=False,
    showgrid=True,
    mirror=True,
    ticklen=4,
    gridcolor='white',
    tickfont_size=10
)

fig.update_layout(
    width=950,
    height=800,
    autosize=False,
    title='Bitcoin mining stats for 180 days',
    margin_t=100,
    showlegend=False,
    xaxis1=dict(axis, domain=[0.55, 1], anchor='y1', showticklabels=False),
    xaxis2=dict(axis, domain=[0.55, 1], anchor='y2', showticklabels=False),
    xaxis3=dict(axis, domain=[0.55, 1], anchor='y3'),
    yaxis1=dict(axis, domain=[0.66, 1.0], anchor='x1', hoverformat='.2f'),
    yaxis2=dict(axis, domain=[0.3 + 0.03, 0.63], anchor='x2', tickprefix='$', 
                hoverformat='.2f'),
    yaxis3=dict(axis, domain=[0.0, 0.3], anchor='x3', tickprefix=u'\u20BF', 
                hoverformat='.2f'),
    plot_bgcolor='rgba(228, 222, 249, 0.65)'
)

fig.show()
```

#### Vertical Table and Graph Subplot

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Table(
    domain=dict(x=[0, 1], y=[0.7, 1.0]),
    columnwidth=[1, 2, 2, 2],
    columnorder=[0, 1, 2, 3, 4],
    header = dict(height = 50,
                  values = [['<b>Date</b>'],['<b>Number<br>transactions</b>'],
                            ['<b>Output<br>volume(BTC)</b>'], ['<b>Market<br>Price</b>']],
                  line_color='rgb(50, 50, 50)',
                  align = ['left'] * 5,
                  font = dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                  fill_color='#d562be'),
    cells = dict(values = [df[k].tolist() for k in
                          ['Date', 'Number-transactions', 'Output-volume(BTC)', 'Market-price']],
                 line_color='#506784',
                 align = ['left'] * 5,
                 font = dict(color=['rgb(40, 40, 40)'] * 5, size=12),
                 format = [None] + [", .2f"] * 2 + [',.4f'],
                 prefix = [None] * 2 + ['$', u'\u20BF'],
                 suffix=[None] * 4,
                 height = 27,
                 fill_color=['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)'])
))


fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Hash-rate'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=2, color='#9748a1'),
    name='hash-rate-TH/s'
))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Mining-revenue-USD'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=2, color='#b04553'),
    name='mining revenue'
))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Transaction-fees-BTC'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=2, color='#af7bbd'),
    name='transact-fee'
))

axis=dict(
    showline=True,
    zeroline=False,
    showgrid=True,
    mirror=True,
    ticklen=4,
    gridcolor='#ffffff',
    tickfont=dict(size=10)
)

fig.update_layout(
    width=950,
    height=800,
    autosize=False,
    title='Bitcoin mining stats for 180 days',
    margin = dict(t=100),
    showlegend=False,
    xaxis1=dict(axis, domain=[0, 1], anchor='y1', showticklabels=False),
    xaxis2=dict(axis, domain=[0, 1], anchor='y2', showticklabels=False),
    xaxis3=dict(axis, domain=[0, 1], anchor='y3'),
    yaxis1=dict(axis, domain=[2 * 0.21 + 0.02 + 0.02, 0.68], anchor='x1', hoverformat='.2f'),
    yaxis2=dict(axis, domain=[0.21 + 0.02, 2 * 0.21 + 0.02], anchor='x2', tickprefix='$', 
                hoverformat='.2f'),
    yaxis3=dict(axis, domain=[0.0, 0.21], anchor='x3', tickprefix=u'\u20BF', 
                hoverformat='.2f'),
    plot_bgcolor='rgba(228, 222, 249, 0.65)'
)

fig.show()
```

#### Reference
See  https://plot.ly/python/reference/#table for more information regarding chart attributes! <br>
For examples of Plotly Tables, see: https://plot.ly/python/table/

