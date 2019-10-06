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
    version: 3.7.3
  plotly:
    description: How to make Sunburst Charts.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/274/
    language: python
    layout: base
    name: Sunburst Charts
    order: 6.1
    page_type: u-guide
    permalink: python/sunburst-charts/
    thumbnail: thumbnail/sunburst.gif
    title: Sunburst in Python | plotly
---

### Basic Sunburst Plot ###
Sunburst plot visualizes hierarchical data spanning outwards radially from root to leaves. The sunburst sectors are determined by the entries in "labels" and in "parents". The root starts from the center and children are added to the outer rings.

Main arguments:
1. **labels**: sets the labels of sunburst sectors.
2. **parents**: sets the parent sectors of sunburst sectors. An empty string '' is used for the root node in the hierarchy. In this example, the root is "Eve".
3. **values**: sets the values associated with sunburst sectors, determining their width (See the "Branchvalues" section below for different modes for setting the width).


```python
import plotly.graph_objects as go

fig =go.Figure(go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
))
# Update layout for tight margin
# See https://plot.ly/python/creating-and-updating-figures/
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
```

### Sunburst with Repeated Labels

```python
import plotly.graph_objects as go

fig =go.Figure(go.Sunburst(
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
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
```

### Branchvalues

With branchvalues "total", the value of the parent represents the width of its wedge. In the example below, "Enoch" is 4 and "Awan" is 6 and so Enoch's width is 4/6ths of Awans. With branchvalues "remainder", the parent's width is determined by its own value plus those of its children. So, Enoch's width is 4/10ths of Awan's (4 / (6 + 4)).

Note that this means that the sum of the values of the children cannot exceed the value of their parent when branchvalues "total". When branchvalues "relative" (the default), children will not take up all of the space below their parent (unless the parent is the root and it has a value of 0).

```python
import plotly.graph_objects as go

fig =go.Figure(go.Sunburst(
    labels=[ "Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["",    "Eve",  "Eve",  "Seth", "Seth", "Eve",  "Eve",  "Awan",  "Eve" ],
    values=[  65,    14,     12,     10,     2,      6,      6,      4,       4],
    branchvalues="total",
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
```

### Large Number of Slices

This example uses a [plotly grid attribute](https://plot.ly/python/reference/#layout-grid) for the suplots. Reference the row and column destination using the [domain](https://plot.ly/python/reference/#sunburst-domain) attribute.

```python
import plotly.graph_objects as go

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

fig = go.Figure()

fig.add_trace(go.Sunburst(
    ids=df1.ids,
    labels=df1.labels,
    parents=df1.parents,
    domain=dict(column=0)
))

fig.add_trace(go.Sunburst(
    ids=df2.ids,
    labels=df2.labels,
    parents=df2.parents,
    domain=dict(column=1),
    maxdepth=2
))

fig.update_layout(
    grid= dict(columns=2, rows=1),
    margin = dict(t=0, l=0, r=0, b=0)
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#sunburst for more information and chart attribute options!
