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
    description: How to make Treemap Charts with Plotly
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/280/
    language: python
    layout: base
    name: Treemap Charts
    order: 14
    page_type: u-guide
    permalink: python/treemaps/
    thumbnail: thumbnail/treemap.png
---

### Basic Treemap

[Treemap charts](https://en.wikipedia.org/wiki/Treemapping) visualize hierarchical data using nested rectangles. Same as [Sunburst](https://plot.ly/python/sunburst-charts/) the hierarchy is defined by [labels](https://plot.ly/python/reference/#treemap-labels) and [parents](https://plot.ly/python/reference/#treemap-parents) attributes. Click on one sector to zoom in/out, which also displays a pathbar in the upper-left corner of your treemap. To zoom out you can use the path bar as well.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
))

fig.show()
```

### Set Different Attributes in Treemap

This example uses the following attributes:

 1. [values](https://plot.ly/python/reference/#treemap-values): sets the values associated with each of the sectors.
 2. [textinfo](https://plot.ly/python/reference/#treemap-textinfo): determines which trace information appear on the graph that can be 'text', 'value', 'current path', 'percent root', 'percent entry', and 'percent parent', or any combination of them.
 3. [pathbar](https://plot.ly/python/reference/#treemap-pathbar): a main extra feature of treemap to display the current path of the visible portion of the hierarchical map. It may also be useful for zooming out of the graph.
 4. [branchvalues](https://plot.ly/python/reference/#treemap-branchvalues): determines how the items in `values` are summed. When set to "total", items in `values` are taken to be value of all its descendants. In the example below Eva = 65, which is equal to 14 + 12 + 10 + 2 + 6 + 6 + 1 + 4.
When set to "remainder", items in `values` corresponding to the root and the branches sectors are taken to be the extra part not part of the sum of the values at their leaves.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]

fig = make_subplots(
    cols = 2, rows = 1,
    column_widths = [0.4, 0.4],
    subplot_titles = ('branchvalues: <b>remainder<br />&nbsp;<br />', 'branchvalues: <b>total<br />&nbsp;<br />'),
    specs = [[{'type': 'treemap', 'rowspan': 1}, {'type': 'treemap'}]]
)

fig.add_trace(go.Treemap(
    labels = labels,
    parents = parents,
    values =  [10, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry+percent root",
    ),
              row = 1, col = 1)

fig.add_trace(go.Treemap(
    branchvalues = "total",
    labels = labels,
    parents = parents,
    values = [65, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry",
    outsidetextfont = {"size": 20, "color": "darkblue"},
    marker = {"line": {"width": 2}},
    pathbar = {"visible": False}),
              row = 1, col = 2)

fig.show()
```

### Set Color of Treemap Sectors

There are three different ways to change the color of the sectors in Treemap:
 1) [marker.colors](https://plot.ly/python/reference/#treemap-marker-colors), 2) [colorway](https://plot.ly/python/reference/#treemap-colorway), 3) [colorscale](https://plot.ly/python/reference/#treemap-colorscale). The following examples show how to use each of them.

```python
import plotly.graph_objects as go

labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    parents = parents,
    marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue"]))

fig.show()
```

This example uses `treemapcolorway` attribute, which should be set in layout.

```python
import plotly.graph_objects as go

labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    parents = parents
))

fig.update_layout(treemapcolorway = ["pink", "lightgray"])

fig.show()
```

```python
import plotly.graph_objects as go

values = ["11", "12", "13", "14", "15", "20", "30"]
labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colorscale = 'Blues'))

fig.show()
```

### Nested Layers in Treemap

The following example uses hierarchical data that includes layers and grouping. Treemap and [Sunburst](https://plot.ly/python/sunburst-charts/) charts reveal insights into the data, and the format of your hierarchical data. [maxdepth](https://plot.ly/python/reference/#treemap-maxdepth) attribute sets the number of rendered sectors from the given level.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

fig = make_subplots(
    rows = 1, cols = 2,
    column_widths = [0.4, 0.4],
    specs = [[{'type': 'treemap', 'rowspan': 1}, {'type': 'treemap'}]]
)

fig.add_trace(
    go.Treemap(
        ids = df1.ids,
        labels = df1.labels,
        parents = df1.parents),
    col = 1, row = 1)

fig.add_trace(
    go.Treemap(
        ids = df2.ids,
        labels = df2.labels,
        parents = df2.parents,
        maxdepth = 3),
    col = 2, row = 1)

fig.update_layout(
    margin = {'t':0, 'l':0, 'r':0, 'b':0}
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#treemap for more information and chart attribute options!
