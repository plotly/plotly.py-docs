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
    description: How to make Sunburst Charts.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/274/
    language: python
    layout: user-guide
    name: Sunburst Charts
    order: 6.1
    page_type: u-guide
    permalink: python/sunburst-charts/
    thumbnail: thumbnail/sunburst.gif
    title: Sunburst in Python | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



#### Version Check
Note: Sunburst Charts are available in version <b>3.8+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version



```python
import plotly
plotly.__version__
```

### Basic Sunburst Plot ###

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
    outsidetextfont = {"size": 20, "color": "#377eb8"},
    marker = {"line": {"width": 2}},
)

layout = go.Layout(
    margin = go.layout.Margin(t=0, l=0, r=0, b=0)
)

py.iplot(go.Figure([trace], layout), filename='basic_sunburst_chart')
```

### Sunburst with Repeated Labels

```python
import plotly.plotly as py
import plotly.graph_objs as go


trace = go.Sunburst(
 ids=[
    "North America", "Europe", "Australia", "North America - Football", "Soccer",
    "North America - Rugby", "Europe - Football", "Rugby",
    "Europe - American Football","Australia - Football", "Association",
    "Australian Rules", "Autstralia - American Football", "Australia - Rugby",
    "Rugby League", "Rugby Union"
  ],
  labels= [
    "North<br>America", "Europe", "Australia", "Football", "Soccer", "Rugby",
    "Football", "Rugby", "American<br>Football", "Football", "Association",
    "Australian<br>Rules", "American<br>Football", "Rugby", "Rugby<br>League",
    "Rugby<br>Union"
  ],
  parents=[
    "", "", "", "North America", "North America", "North America", "Europe",
    "Europe", "Europe","Australia", "Australia - Football", "Australia - Football",
    "Australia - Football", "Australia - Football", "Australia - Rugby",
    "Australia - Rugby"
  ],
  outsidetextfont={"size": 20, "color": "#377eb8"},
  leaf={"opacity": 0.4},
  marker={"line": {"width": 2}}
)

layout = go.Layout(
    margin = go.layout.Margin(t=0, l=0, r=0, b=0),
    sunburstcolorway=["#636efa","#ef553b","#00cc96"]
)

fig = go.Figure([trace], layout)

py.iplot(fig, filename='repeated_labels_sunburst')
```

### Large Number of Slices
This example uses a [plotly grid attribute](https://plot.ly/python/reference/#layout-grid) for the suplots. Reference the row and column destination using the [domain](https://plot.ly/python/reference/#sunburst-domain) attribute.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

trace1 = go.Sunburst(
    ids=df1.ids,
    labels=df1.labels,
    parents=df1.parents,
    domain=dict(column=0)
)

trace2 = go.Sunburst(
    ids=df2.ids,
    labels=df2.labels,
    parents=df2.parents,
    domain=dict(column=1),
    maxdepth=2
)

layout = go.Layout(
    grid=go.layout.Grid(columns=2, rows=1),
    margin = go.layout.Margin(t=0, l=0, r=0, b=0),
    sunburstcolorway=[
    "#636efa","#EF553B","#00cc96","#ab63fa","#19d3f3",
    "#e763fa", "#FECB52","#FFA15A","#FF6692","#B6E880"
  ],
    extendsunburstcolors=True
)

data = [trace1, trace2]

fig = go.Figure(data, layout)

py.iplot(fig, filename='large_number_of_slices')
```

#### Reference
See https://plot.ly/python/reference/#sunburst for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'sunburst-charts.ipynb', 'python/sunburst-charts/', 'Sunburst Charts',
    'How to make Sunburst Charts.',
    title= 'Sunburst in Python | plotly',
    has_thumbnail='true', thumbnail='thumbnail/sunburst.gif',
    language='python',
    display_as='basic', order=6.1,
    ipynb='~notebook_demo/274/')
```

```python

```
