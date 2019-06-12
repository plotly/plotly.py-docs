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
    description: How to make tables in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/197
    language: python
    layout: user-guide
    name: Tables
    order: 7
    page_type: u-guide
    permalink: python/table/
    thumbnail: thumbnail/table.gif
    title: Tables | plotly
---

`go.Table` provides a Table object for detailed data viewing. The data are arranged in
a grid of rows and columns. Most styling can be specified for header, columns, rows or individual cells. Table is using a column-major order, ie. the grid is represented as a vector of column vectors.

Note that [Dash](https://dash.plot.ly/) provides a different type of [DataTable](https://dash.plot.ly/datatable).

#### Basic Table

```python
import plotly.graph_objs as go

trace = go.Table(header=dict(values=['A Scores', 'B Scores']),
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))

fig = go.Figure(data=[trace]) 
fig.show()
```

#### Styled Table

```python
import plotly.graph_objs as go

trace = go.Table(
    header=dict(values=['A Scores', 'B Scores'],
                line_color='#7D7F80',
                fill_color='#a1c3d1',
                align='left'),
    cells=dict(values=[[100, 90, 80, 90], # 1st column
                       [95, 85, 75, 95]], # 2nd column
               line_color='#7D7F80',
               fill_color='#EDFAFF',
               align='left'))

fig = go.Figure(data=[trace])
fig.update(layout_width=500, layout_height=300)
```

#### Use a Pandas Dataframe

```python
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

trace = go.Table(
    header=dict(values=list(df.columns),
                fill_color='#C2D4FF',
                align='left'),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
               fill_color='#F5F8FF',
               align='left'))

fig = go.Figure(data=[trace])
fig.show()
```

#### Changing Row and Column Size

```python
import plotly.graph_objs as go

values = [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>'], #1st col
  ["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]


trace0 = go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],
  header = dict(
    values = [['<b>EXPENSES</b><br>as of July 2017'],
                  ['<b>DESCRIPTION</b>']],
    line_color='#506784',
    fill_color='#119DFF',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells = dict(
    values=values,
    line_color='#506784',
    fill=dict(color = ['#25FEFD', 'white']),
    align=['left', 'center'],
    font=dict(color='#506784', size=12),
    height=30
    ))

fig = go.Figure(data=[trace0])
fig.show()
```

#### Alternating Row Colors 

```python
import plotly.graph_objs as go

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

trace0 = go.Table(
  header=dict(
    values=['<b>EXPENSES</b>','<b>Q1</b>','<b>Q2</b>','<b>Q3</b>','<b>Q4</b>'],
    line_color='#506784',
    fill_color=headerColor,
    align=['left','center'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=[
      ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
      [1200000, 20000, 80000, 2000, 12120000],
      [1300000, 20000, 70000, 2000, 130902000],
      [1300000, 20000, 120000, 2000, 131222000],
      [1400000, 20000, 90000, 2000, 14102000]],
    line_color='#506784',
    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
    align = ['left', 'center'],
    font = dict(color = '#506784', size = 11)
    ))

fig = go.Figure(data=[trace0])
fig.show()
```

#### Row Color Based on Variable

```python
import plotly.graph_objs as go

import pandas as pd

colors = ['rgb(239, 243, 255)', 'rgb(189, 215, 231)', 'rgb(107, 174, 214)',
          'rgb(49, 130, 189)', 'rgb(8, 81, 156)']
data = {'Year' : [2010, 2011, 2012, 2013, 2014], 'Color' : colors}
df = pd.DataFrame(data)

trace0 = go.Table(
  header=dict(
    values=["Color", "<b>YEAR</b>"],
    line_color='white', fill_color='white',
    align='center', font=dict(color='black', size=12)
  ),
  cells=dict(
    values=[df.Color, df.Year],
    line_color=[df.Color], fill_color=[df.Color],
    align='center', font=dict(color='black', size=11)
  ))
fig = go.Figure(data=[trace0])
fig.show()
```

#### Cell Color Based on Variable

```python
import plotly.graph_objs as go
from plotly.colors import n_colors
import numpy as np

colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
a = np.random.randint(low=0, high=9, size=10)
b = np.random.randint(low=0, high=9, size=10)
c = np.random.randint(low=0, high=9, size=10)


trace0 = go.Table(
  header=dict(
    values=['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'],
    line_color='white', fill_color='white',
    align='center',font=dict(color='black', size=12)
  ),
  cells=dict(
    values=[a, b, c],
    line_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
    fill_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
    align='center', font=dict(color='white', size=11)
    ))

fig = go.Figure(data=[trace0])
fig.show()
```

### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-tableplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-tableplot/", width="100%", height="850px", frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-tableplot/code", width="100%", height=500, frameBorder="0")
```

#### Reference
For more information on tables and table attributes see: https://plot.ly/python/reference/#table.

