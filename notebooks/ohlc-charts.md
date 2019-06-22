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
    description: How to make interactive OHLC charts in Python with Plotly. Six examples
      of OHLC charts with Pandas, time series, and yahoo finance data.
    display_as: financial
    has_thumbnail: true
    ipynb: ~notebook_demo/53
    language: python
    layout: user-guide
    name: OHLC Charts
    order: 1
    page_type: example_index
    permalink: python/ohlc-charts/
    thumbnail: thumbnail/ohlc.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Plotly's Python API is updated frequently. Run `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

##### Simple OHLC Chart with Pandas

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])
data = [trace]
py.iplot(data, filename='simple_ohlc')
```

##### OHLC Chart without Rangeslider

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])

layout = go.Layout(
    xaxis = dict(
        rangeslider = dict(
            visible = False
        )
    )
)

data = [trace]

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='OHLC without Rangeslider')
```

#### Adding Customized Text and Annotations

```python
import plotly.plotly as py
import plotly.graph_objs as go

from datetime import datetime
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])
data = [trace]
layout = {
    'title': 'The Great Recession',
    'yaxis': {'title': 'AAPL Stock'},
    'shapes': [{
        'x0': '2016-12-09', 'x1': '2016-12-09',
        'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
        'line': {'color': 'rgb(30,30,30)', 'width': 1}
    }],
    'annotations': [{
        'x': '2016-12-09', 'y': 0.05, 'xref': 'x', 'yref': 'paper',
        'showarrow': False, 'xanchor': 'left',
        'text': 'Increase Period Begins'
    }]
}
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='aapl-recession-ohlc')
```

#### Custom OHLC Colors

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'],
                increasing=dict(line=dict(color= '#17BECF')),
                decreasing=dict(line=dict(color= '#7F7F7F')))
data = [trace]
py.iplot(data, filename='styled_ohlc')
```

##### Simple OHLC with `datetime` Objects

```python
import plotly.plotly as py
import plotly.graph_objs as go

from datetime import datetime

open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
dates = [datetime(year=2013, month=10, day=10),
         datetime(year=2013, month=11, day=10),
         datetime(year=2013, month=12, day=10),
         datetime(year=2014, month=1, day=10),
         datetime(year=2014, month=2, day=10)]

trace = go.Ohlc(x=dates,
                open=open_data,
                high=high_data,
                low=low_data,
                close=close_data)
data = [trace]
py.iplot(data, filename='ohlc_datetime')
```

### Custom Hovertext

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime

hovertext=[]
for i in range(len(df['AAPL.Open'])):
    hovertext.append('Open: '+str(df['AAPL.Open'][i])+'<br>Close: '+str(df['AAPL.Close'][i]))

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'],
                text=hovertext,
                hoverinfo='text')
data = [trace]
py.iplot(data, filename='ohlc_custom_hover')
```

#### Reference
For more information on candlestick attributes, see: https://plot.ly/python/reference/#ohlc

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'ohlc-charts.ipynb', 'python/ohlc-charts/', 'Python OHLC Charts | plotly',
    'How to make interactive OHLC charts in Python with Plotly. '
    'Six examples of OHLC charts with Pandas, time series, and yahoo finance data.',
    name = 'OHLC Charts',
    thumbnail='thumbnail/ohlc.jpg', language='python',
    page_type='example_index', has_thumbnail='true', display_as='financial', order=1,
    ipynb= '~notebook_demo/53')
```

```python

```
