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

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Note: Table traces are available in version <b>2.2.1+</b>.<br> 
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Basic Table

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Table(
    header=dict(values=['A Scores', 'B Scores']),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]]))

data = [trace] 
py.iplot(data, filename = 'basic_table')
```

#### Styled Table

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Table(
    header=dict(values=['A Scores', 'B Scores'],
                line = dict(color='#7D7F80'),
                fill = dict(color='#a1c3d1'),
                align = ['left'] * 5),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]],
               line = dict(color='#7D7F80'),
               fill = dict(color='#EDFAFF'),
               align = ['left'] * 5))

layout = dict(width=500, height=300)
data = [trace]
fig = dict(data=data, layout=layout)
py.iplot(fig, filename = 'styled_table')
```

#### Use a Panda's Dataframe

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

trace = go.Table(
    header=dict(values=list(df.columns),
                fill = dict(color='#C2D4FF'),
                align = ['left'] * 5),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
               fill = dict(color='#F5F8FF'),
               align = ['left'] * 5))

data = [trace] 
py.iplot(data, filename = 'pandas_table')
```

#### Changing Row and Column Size

```python
import plotly.plotly as py
import plotly.graph_objs as go

values = [[['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>']],
[["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]]


trace0 = go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],
  header = dict(
    values = [['<b>EXPENSES</b><br>as of July 2017'],
                  ['<b>DESCRIPTION</b>']],
    line = dict(color = '#506784'),
    fill = dict(color = '#119DFF'),
    align = ['left','center'],
    font = dict(color = 'white', size = 12),
    height = 40
  ),
  cells = dict(
    values = values,
    line = dict(color = '#506784'),
    fill = dict(color = ['#25FEFD', 'white']),
    align = ['left', 'center'],
    font = dict(color = '#506784', size = 12),
    height = 30
    ))

data = [trace0]

py.iplot(data, filename = "Row and Column Size")
```

#### Alternating Row Colors 

```python
import plotly.plotly as py
import plotly.graph_objs as go

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

trace0 = go.Table(
  header = dict(
    values = [['<b>EXPENSES</b>'],
                  ['<b>Q1</b>'],
                  ['<b>Q2</b>'],
                  ['<b>Q3</b>'],
                  ['<b>Q4</b>']],
    line = dict(color = '#506784'),
    fill = dict(color = headerColor),
    align = ['left','center'],
    font = dict(color = 'white', size = 12)
  ),
  cells = dict(
    values = [
      [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>']],
      [[1200000, 20000, 80000, 2000, 12120000]],
      [[1300000, 20000, 70000, 2000, 130902000]],
      [[1300000, 20000, 120000, 2000, 131222000]],
      [[1400000, 20000, 90000, 2000, 14102000]]],
    line = dict(color = '#506784'),
    fill = dict(color = [rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]),
    align = ['left', 'center'],
    font = dict(color = '#506784', size = 11)
    ))

data = [trace0]

py.iplot(data, filename = "alternating row colors")
```

#### Row Color Based on Variable

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import colorlover as cl

colors = cl.scales['5']['seq']['Blues']
data = {'Year' : [2010, 2011, 2012, 2013, 2014],
        'Color' : colors}
df = pd.DataFrame(data)


trace0 = go.Table(
  header = dict(
    values = ["Color", "<b>YEAR</b>"],
    line = dict(color = 'white'),
    fill = dict(color = 'white'),
    align = ['center'],
    font = dict(color = 'black', size = 12)
  ),
  cells = dict(
    values = [df.Color, df.Year],
    line = dict(color = [df.Color]),
    fill = dict(color = [df.Color]),
    align = 'center',
    font = dict(color = 'black', size = 11)
    ))

data = [trace0]

py.iplot(data, filename = "row variable color")
```

#### Cell Color Based on Variable

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import colorlover as cl

colors = cl.scales['9']['seq']['Reds']
a = np.random.randint(low=0, high=9, size=10)
b = np.random.randint(low=0, high=9, size=10)
c = np.random.randint(low=0, high=9, size=10)


trace0 = go.Table(
  header = dict(
    values = ['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'],
    line = dict(color = 'white'),
    fill = dict(color = 'white'),
    align = 'center',
    font = dict(color = 'black', size = 12)
  ),
  cells = dict(
    values = [a,b,c],
    line = dict(color = [np.array(colors)[a],np.array(colors)[b],
                        np.array(colors)[c]]),
    fill = dict(color = [np.array(colors)[a],np.array(colors)[b],
                        np.array(colors)[c]]),
    align = 'center',
    font = dict(color = 'white', size = 11)
    ))

data = [trace0]

py.iplot(data, filename = "cell variable color")
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

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'table.ipynb', 'python/table/', 'Python Tables | plotly',
    'How to make tables in Python with Plotly.',
    title = 'Tables | plotly',
    name = 'Tables',
    thumbnail='thumbnail/table.gif', language='python',
    has_thumbnail='true', display_as='basic', order=7,
    ipynb='~notebook_demo/197')
```