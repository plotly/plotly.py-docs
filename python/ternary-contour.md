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

#### Basic Ternary Contour Plot

```python
import plotly.graph_objects as go

import requests

url = 'https://gist.githubusercontent.com/davenquinn/988167471993bc2ece29/raw/f38d9cb3dd86e315e237fde5d65e185c39c931c2/data.json'
data = requests.get(url).json()

colors = ['#8dd3c7','#ffffb3','#bebada',
          '#fb8072','#80b1d3','#fdb462',
          '#b3de69','#fccde5','#d9d9d9',
          '#bc80bd','#ccebc5','#ffed6f'];

# generate a,b and c from JSON data..
fig = go.Figure()

color_iter = iter(colors)
for i in data.keys():
    fig.add_trace(go.Scatterternary(
        text=i,
        a=[ k['clay'] for k in data[i] ],
        b=[ k['sand'] for k in data[i] ],
        c=[ k['silt'] for k in data[i] ],
        mode='lines',
        line=dict(color='#444'),
        fill='toself',
        fillcolor=color_iter.__next__()
    ))

fig.update_layout(
    title = 'Simple Ternary Contour Plot with Python',
    showlegend = False,
    ternary =  {
        'sum':100,
        'aaxis':{'title': 'clay', 'ticksuffix':'%', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
        'baxis':{'title': 'sand', 'ticksuffix':'%', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
        'caxis':{'title': 'silt', 'ticksuffix':'%', 'min': 0.01, 'linewidth':2, 'ticks':'outside' }},
)

fig.show()
```

```python

```
