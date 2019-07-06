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
    description: How to make Ternary plots in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/39
    language: python
    layout: user-guide
    name: Ternary Plots
    order: 9
    page_type: example_index
    permalink: python/ternary-plots/
    thumbnail: thumbnail/ternary.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Ternary Plots are available in version 1.9.10+
Run pip install plotly --upgrade to update your Plotly version

```python
import plotly
plotly.__version__
```

### Basic Ternary Plot with Markers

```python
import plotly.plotly as py
import plotly.graph_objs as go

rawData = [
    {'journalist':75,'developer':25,'designer':0,'label':'point 1'},
    {'journalist':70,'developer':10,'designer':20,'label':'point 2'},
    {'journalist':75,'developer':20,'designer':5,'label':'point 3'},
    {'journalist':5,'developer':60,'designer':35,'label':'point 4'},
    {'journalist':10,'developer':80,'designer':10,'label':'point 5'},
    {'journalist':10,'developer':90,'designer':0,'label':'point 6'},
    {'journalist':20,'developer':70,'designer':10,'label':'point 7'},
    {'journalist':10,'developer':20,'designer':70,'label':'point 8'},
    {'journalist':15,'developer':5,'designer':80,'label':'point 9'},
    {'journalist':10,'developer':10,'designer':80,'label':'point 10'},
    {'journalist':20,'developer':10,'designer':70,'label':'point 11'},
];

def makeAxis(title, tickangle):
    return {
      'title': title,
      'titlefont': { 'size': 20 },
      'tickangle': tickangle,
      'tickfont': { 'size': 15 },
      'tickcolor': 'rgba(0,0,0,0)',
      'ticklen': 5,
      'showline': True,
      'showgrid': True
    }

data = [{
    'type': 'scatterternary',
    'mode': 'markers',
    'a': [i for i in map(lambda x: x['journalist'], rawData)],
    'b': [i for i in map(lambda x: x['developer'], rawData)],
    'c': [i for i in map(lambda x: x['designer'], rawData)],
    'text': [i for i in map(lambda x: x['label'], rawData)],
    'marker': {
        'symbol': 100,
        'color': '#DB7365',
        'size': 14,
        'line': { 'width': 2 }
    },
    }]

layout = {
    'ternary': {
        'sum': 100,
        'aaxis': makeAxis('Journalist', 0),
        'baxis': makeAxis('<br>Developer', 45),
        'caxis': makeAxis('<br>Designer', -45)
    },
    'annotations': [{
      'showarrow': False,
      'text': 'Simple Ternary Plot with Markers',
        'x': 0.5,
        'y': 1.3,
        'font': { 'size': 15 }
    }]
}

fig = {'data': data, 'layout': layout}
py.iplot(fig, validate=False)
```

#### Reference
See https://plot.ly/python/reference/#scatterternary for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'ternary.ipynb', 'python/ternary-plots/', 'Python Ternary Plots | plotly',
    'How to make Ternary plots in Python with Plotly.',
    name = 'Ternary Plots',
    thumbnail='thumbnail/ternary.jpg', language='python',
    page_type='example_index', has_thumbnail='true', display_as='scientific', order=9,
    ipynb= '~notebook_demo/39')
```

```python

```