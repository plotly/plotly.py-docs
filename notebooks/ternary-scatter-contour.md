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
    description: How to make a scatter plot overlaid on ternary contour in Python
      with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/41
    language: python
    layout: user-guide
    name: Ternary Overlay
    order: 11
    page_type: u-guide
    permalink: python/ternary-scatter-contour/
    thumbnail: thumbnail/ternary-scatter-contour.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Ternary Charts are available in version 1.9.10+
Run pip install plotly --upgrade to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Load and Process Data Files

```python
import plotly.plotly as py

import json
import pandas as pd

contour_raw_data = pd.read_json('https://raw.githubusercontent.com/plotly/datasets/master/contour_data.json')
scatter_raw_data = pd.read_json('https://raw.githubusercontent.com/plotly/datasets/master/scatter_data.json')

scatter_data =  scatter_raw_data['Data']

def clean_data(data_in):
    """
    Cleans data in a format which can be conveniently
    used for drawing traces. Takes a dictionary as the
    input, and returns a list in the following format:

    input = {'key': ['a b c']}
    output = [key, [a, b, c]]
    """
    key = data_in.keys()[0]
    data_out = [key]
    for i in data_in[key]:
        data_out.append(map(float, i.split(' ')))

    return data_out


#Example:
print clean_data({'L1': ['.03 0.5 0.47','0.4 0.5 0.1']})
```

#### Create Ternary Scatter Plot:

```python
a_list = []
b_list = []
c_list = []
text = []

for raw_data in scatter_data:
    data = clean_data(raw_data)
    text.append(data[0])
    c_list.append(data[1][0])
    a_list.append(data[1][1])
    b_list.append(data[1][2])

trace1 = dict(type='scatterternary',
              text=text,
              a=a_list,
              b=b_list,
              c=c_list,
              mode='markers',
              marker={'symbol': 100,
                      'color': 'green',
                      'size': 10},
)

layout = {
    'title': 'Ternary Scatter Plot',
    'ternary':
        {
        'sum':1,
        'aaxis':{'title': 'X', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
        'baxis':{'title': 'W', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
        'caxis':{'title': 'S', 'min': 0.01, 'linewidth':2, 'ticks':'outside' }
    },
    'showlegend': False
}

scatter_fig = dict(data=[trace1], layout=layout)
py.iplot(scatter_fig)
```

#### Create Ternary Contour Plot:

```python
contour_dict = contour_raw_data['Data']

# Defining a colormap:
colors = ['#8dd3c7','#ffffb3','#bebada',
          '#fb8072','#80b1d3','#fdb462',
          '#b3de69','#fccde5','#d9d9d9',
          '#bc80bd']
colors_iterator = iter(colors)

traces = []
for raw_data in contour_dict:
    data = clean_data(raw_data)

    a = [inner_data[0] for inner_data in data[1:]]
    a.append(data[1][0]) # Closing the loop

    b = [inner_data[1] for inner_data in data[1:]]
    b.append(data[1][1]) # Closing the loop

    c = [inner_data[2] for inner_data in data[1:]]
    c.append(data[1][2]) # Closing the loop

    trace = dict(
        type='scatterternary',text = data[0],
        a=a, b=b, c=c, mode='lines',
        line=dict(color='#444', shape='spline'),
        fill='toself',
        fillcolor = colors_iterator.next()
    )
    traces.append(trace)

layout['title'] = 'Ternary Contour Plot'
contour_fig = dict(data=traces, layout=layout)
py.iplot(contour_fig)
```

#### Scatter Plot Overlaid on Contour Plot

We will change the marker symbol for the `trace1` (The one used in scatter plot), so that it is distinctly visible on the contour background:

```python
trace1['marker']['symbol'] = 'x'
trace1['marker']['color'] = '#4d79ff'
traces.append(trace1)

# update title:
layout['title'] = 'Scatter Plot overlaid on Ternary Contour Plot'
figure = dict(data=traces, layout=layout)
py.iplot(figure)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'ternary-scatter-contour.ipynb', 'python/ternary-scatter-contour/', 'Python Ternary Scatter Overlaid on Contour | plotly',
    'How to make a scatter plot overlaid on ternary contour in Python with Plotly.',
    name = 'Ternary Overlay',
    thumbnail='thumbnail/ternary-scatter-contour.jpg', language='python',
    has_thumbnail='true', display_as='scientific', order=11,
    ipynb= '~notebook_demo/41')
```

```python

```