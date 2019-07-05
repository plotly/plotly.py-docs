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
    description: How to make interactive treemap in Python with Plotly and Squarify.
      An examples of a treemap in Plotly using Squarify.
    display_as: statistical
    has_thumbnail: true
    ipynb: ~notebook_demo/29
    language: python
    layout: user-guide
    name: Treemaps
    order: 11
    page_type: u-guide
    permalink: python/treemaps/
    thumbnail: thumbnail/treemap.jpg
    title: Python Treemaps | plotly
    v4upgrade: true
---

#### Simple Example with Plotly and [Squarify](https://pypi.python.org/pypi/squarify)
Define the coordinate system for the returned rectangles: these values will range from x to x + width and y to y + height.
Then define your treemap values. The sum of the treemap values must equal the total area to be laid out (i.e. width `*` height). The values must be sorted in descending order and must be positive.

```python
import plotly.graph_objects as go

import squarify

fig = go.Figure()

x = 0.
y = 0.
width = 100.
height = 100.

values = [500, 433, 78, 25, 25, 7]

normed = squarify.normalize_sizes(values, width, height)
rects = squarify.squarify(normed, x, y, width, height)

# Choose colors from http://colorbrewer2.org/ under "Export"
color_brewer = ['rgb(166,206,227)','rgb(31,120,180)','rgb(178,223,138)',
                'rgb(51,160,44)','rgb(251,154,153)','rgb(227,26,28)']
shapes = []
annotations = []
counter = 0

for r, val, color in zip(rects, values, color_brewer):
    shapes.append(
        dict(
            type = 'rect',
            x0 = r['x'],
            y0 = r['y'],
            x1 = r['x']+r['dx'],
            y1 = r['y']+r['dy'],
            line = dict( width = 2 ),
            fillcolor = color
        )
    )
    annotations.append(
        dict(
            x = r['x']+(r['dx']/2),
            y = r['y']+(r['dy']/2),
            text = val,
            showarrow = False
        )
    )

# For hover text
fig.add_trace(go.Scatter(
    x = [ r['x']+(r['dx']/2) for r in rects ],
    y = [ r['y']+(r['dy']/2) for r in rects ],
    text = [ str(v) for v in values ],
    mode = 'text',
))

fig.update_layout(
    height=700,
    width=700,
    xaxis=dict(showgrid=False,zeroline=False),
    yaxis=dict(showgrid=False,zeroline=False),
    shapes=shapes,
    annotations=annotations,
    hovermode='closest'
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options or https://pypi.python.org/pypi/squarify for more information about squarify!
