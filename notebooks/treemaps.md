---
jupyter:
  jupytext:
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
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!

#### Version Check
Plotly's python API is updated frequently. To upgrade, run `pip install plotly --upgrade`.


#### Simple Example with Plotly and [Squarify](https://pypi.python.org/pypi/squarify)
Define the coordinate system for the returned rectangles: these values will range from x to x + width and y to y + height.
Then define your treemap values. The sum of the treemap values must equal the total area to be laid out (i.e. width `*` height). The values must be sorted in descending order and must be positive.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import squarify

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

for r in rects:
    shapes.append( 
        dict(
            type = 'rect', 
            x0 = r['x'], 
            y0 = r['y'], 
            x1 = r['x']+r['dx'], 
            y1 = r['y']+r['dy'],
            line = dict( width = 2 ),
            fillcolor = color_brewer[counter]
        ) 
    )
    annotations.append(
        dict(
            x = r['x']+(r['dx']/2),
            y = r['y']+(r['dy']/2),
            text = values[counter],
            showarrow = False
        )
    )
    counter = counter + 1
    if counter >= len(color_brewer):
        counter = 0

# For hover text
trace0 = go.Scatter(
    x = [ r['x']+(r['dx']/2) for r in rects ], 
    y = [ r['y']+(r['dy']/2) for r in rects ],
    text = [ str(v) for v in values ], 
    mode = 'text',
)
        
layout = dict(
    height=700, 
    width=700,
    xaxis=dict(showgrid=False,zeroline=False),
    yaxis=dict(showgrid=False,zeroline=False),
    shapes=shapes,
    annotations=annotations,
    hovermode='closest'
)

# With hovertext
figure = dict(data=[trace0], layout=layout)

# Without hovertext
# figure = dict(data=[Scatter()], layout=layout)

py.iplot(figure, filename='squarify-treemap')
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options or https://pypi.python.org/pypi/squarify for more information about squarify!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'treemap.ipynb', 'python/treemaps/', 'Python Treemaps | plotly',
    'How to make interactive treemap in Python with Plotly and Squarify. '
    'An examples of a treemap in Plotly using Squarify.',
    title = 'Python Treemaps | plotly',
    name = 'Treemaps',
    thumbnail='thumbnail/treemap.jpg', language='python',
    has_thumbnail='true', display_as='statistical', order=11,
    ipynb= '~notebook_demo/29')
```

```python

```