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
    description: How to make Ternary Contour Plots in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/40
    language: python
    layout: user-guide
    name: Ternary Contour Plots
    order: 10
    page_type: u-guide
    permalink: python/ternary-contour/
    thumbnail: thumbnail/ternary-contour.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Ternary Plots are available in version 1.9.10+ <br>Run pip install plotly --upgrade to update your Plotly version


#### Basic Ternary Contour Plot

```python
import plotly.plotly as py

import json
import urllib

url = 'https://gist.githubusercontent.com/davenquinn/988167471993bc2ece29/raw/f38d9cb3dd86e315e237fde5d65e185c39c931c2/data.json'
response = urllib.urlopen(url).read()
data = json.loads(response)

colors = ['#8dd3c7','#ffffb3','#bebada',
          '#fb8072','#80b1d3','#fdb462',
          '#b3de69','#fccde5','#d9d9d9',
          '#bc80bd','#ccebc5','#ffed6f'];

# generate a,b and c from JSON data..
traces = []
color_iter = iter(colors)
for i in data.keys():
    trace = dict(text=i,
        type='scatterternary',
        a=[ k['clay'] for k in data[i] ],
        b=[ k['sand'] for k in data[i] ],
        c=[ k['silt'] for k in data[i] ],
        mode='lines',
        line=dict(color='#444'),
        fill='toself',
        fillcolor=color_iter.next()
    )
    traces.append(trace)

layout = {
    'title': 'Simple Ternary Contour Plot with Python',
    'ternary':
        {'sum':100,
         'aaxis':{'title': 'clay', 'ticksuffix':'%', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
         'baxis':{'title': 'sand', 'ticksuffix':'%', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
         'caxis':{'title': 'silt','ticksuffix':'%', 'min': 0.01, 'linewidth':2, 'ticks':'outside' }},
    'showlegend': False
}

figure = dict(data=traces, layout=layout)
py.iplot(figure, validate=False)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'ternary-contour.ipynb', 'python/ternary-contour/', 'Python Ternary Contour Plots | plotly',
    'How to make Ternary Contour Plots in Python with Plotly.',
    name = 'Ternary Contour Plots',
    thumbnail='thumbnail/ternary-contour.jpg', language='python',
    has_thumbnail='true', display_as='scientific', order=10,
    ipynb= '~notebook_demo/40')
```

```python

```