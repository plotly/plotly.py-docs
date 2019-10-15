---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
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
    language: python
    layout: base
    name: Sunburst Charts
    order: 6.1
    page_type: u-guide
    permalink: python/sunburst-charts/
    thumbnail: thumbnail/sunburst.gif
    title: Sunburst in Python | plotly
---

### Basic Treemap

Treemap chart visualize hierarchical data using nested rectangles. Same as [Sunburst](https://plot.ly/python/sunburst-charts/) the hierarchy is defined by [labels](https://plot.ly/python/reference/#treemap-labels) and [parents]((https://plot.ly/python/reference/#treemap-parents)) attributes. [count](https://plot.ly/python/reference/#treemap-count) attribute allows counting the numbers of leaves, branches or both when values array is not provided.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Treemap(
    labels = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
))

fig.show()
```

### Set Different Attributes in Treemap

This example uses the following attributs:

 1. [values](https://plot.ly/python/reference/#treemap-values): sets the values associated with each of the sunburst sectors
 2. [textinfo](https://plot.ly/python/reference/#treemap-textinfo): determines which trace information appear on the graph that can be 'text', 'value', 'current path',      'percent root', 'percent entry', and 'percent parent', or any combination of them.  
 3. [pathbar](https://plot.ly/python/reference/#treemap-pathbar): a main extra feature of treemap to display the current path of the visible portion of the hierarchical map. It may also be useful for zooming out of the graph.
 4. [branchvalues](https://plot.ly/python/reference/#treemap-branchvalues): determines how the items in `values` are summed. When set to "total", items in `values` are taken to be value of all its descendants. In the example below Eva = 65, which is equal to 14 + 12 + 10 + 2 + 6 + 6 + 1 + 4. 
When set to "remainder", items in `values` corresponding to the root and the branches sectors are taken to be the extra part not part of the sum of the values at their leaves.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values =  [10, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry+percent root",
    domain = {"x": [0, 0.48]}))

fig.add_trace(go.Treemap(
    branchvalues = "total",
    labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    domain = {"x": [0.52, 1]},
    values = [65, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry",
    outsidetextfont = {"size": 20, "color": "darkblue"},
    marker = {"line": {"width": 2}},
    pathbar = {"visible": False}))

fig.update_layout(
    annotations = [{
      "showarrow": False,
      "text": "branchvalues: <b>remainder</b>",
      "x": 0.25,
      "xanchor": "center",
      "y": 1,
      "yanchor": "bottom"
    }, {
      "showarrow": False, 
      "text": "branchvalues: <b>total</b>",
      "x": 0.75,
      "xanchor": "center",
      "y": 1,
      "yanchor": "bottom"
    }])

fig.show()
```

### Advance Treemap

The following example uses hierarchical data that includes layers and grouping. Treemap and [Sunburst](https://plot.ly/python/sunburst-charts/) charts reveal indights into the data, and the format of your hierarchical data. 

```python
import plotly.graph_objects as go 
import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

fig = go.Figure()

fig.add_trace(go.Treemap(
    ids = df1.ids,
    labels = df1.labels,
    parents = df1.parents,
    domain = {'column':0}
))

fig.add_trace(go.Treemap(
    ids = df2.ids,
    labels = df2.labels,
    parents = df2.parents,
    domain = {'column':1},
    maxdepth = 2
))

fig.update_layout(
    grid = {'columns':2, 'rows':1},
    margin = {'t':0, 'l':0, 'r':0, 'b':0}
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#treemap for more information and chart attribute options!
