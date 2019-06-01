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
    description: How to make funnel charts in Python with Plotly.
    display_as: financial
    has_thumbnail: true
    ipynb: ~notebook_demo/140
    language: python
    layout: user-guide
    name: Funnel Charts
    order: 4
    page_type: example_index
    permalink: python/funnel-charts/
    thumbnail: thumbnail/funnel-chart.jpg
    title: Python Funnel Charts | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Plotly's Python API is updated frequently. Run `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

#### Funnel Chart Outline

*Funnel charts* are often used to represent data in different stages of a business process.
It’s an important mechanism in Business Intelligence to identify potential problem areas of a process. For example, it’s used to observe the revenue or loss in a sales process for each stage. A funnel chart has multiple *phases* and *values* associated with them. Here is a table that represents a *user flow* funnel for a social media campaign. The column named 'Values' represents the total number of users at that *Phase*.

```python
import plotly.plotly as py
import plotly.figure_factory as ff

data_table = [['Phases', 'Values'],
               ['Visit', 13873],
               ['Sign-up', 10553],
               ['Selection', 5443],
               ['Purchase', 3703],
               ['Review', 1708]]

table = ff.create_table(data_table)
py.iplot(table)
```

#### Basic Funnel Chart

```python
import plotly.plotly as py
from plotly import graph_objs as go

from __future__ import division

# chart stages data
values = [13873, 10553, 5443, 3703, 1708]
phases = ['Visit', 'Sign-up', 'Selection', 'Purchase', 'Review']

# color of each funnel section
colors = ['rgb(32,155,160)', 'rgb(253,93,124)', 'rgb(28,119,139)', 'rgb(182,231,235)', 'rgb(35,154,160)']
```

A funnel section will be drawn using [Plotly shapes](https://plot.ly/python/shapes/), in the shape of a *Rectangle* or *Isosceles Trapezoid* depending on the value of the next phase. The phase having *maximum value* will have the width equal to the plot.

```python
n_phase = len(phases)
plot_width = 400

# height of a section and difference between sections 
section_h = 100
section_d = 10

# multiplication factor to calculate the width of other sections
unit_width = plot_width / max(values)

# width of each funnel section relative to the plot width
phase_w = [int(value * unit_width) for value in values]

# plot height based on the number of sections and the gap in between them
height = section_h * n_phase + section_d * (n_phase - 1)
```

Each section will have a height of 100px and there will be a difference of 10px in successive sections. To draw a section, we are going to use [SVG paths](https://developer.mozilla.org/en/docs/Web/SVG/Tutorial/Paths).

```python
# list containing all the plot shapes
shapes = []

# list containing the Y-axis location for each section's name and value text
label_y = []

for i in range(n_phase):
        if (i == n_phase-1):
                points = [phase_w[i] / 2, height, phase_w[i] / 2, height - section_h]
        else:
                points = [phase_w[i] / 2, height, phase_w[i+1] / 2, height - section_h]

        path = 'M {0} {1} L {2} {3} L -{2} {3} L -{0} {1} Z'.format(*points)

        shape = {
                'type': 'path',
                'path': path,
                'fillcolor': colors[i],
                'line': {
                    'width': 1,
                    'color': colors[i]
                }
        }
        shapes.append(shape)
        
        # Y-axis location for this section's details (text)
        label_y.append(height - (section_h / 2))

        height = height - (section_h + section_d)
```

To draw the phase names and values, we are using the *text* mode in *scatter* plots. To style the plot, we are changing the background color of the plot and the plot paper, hiding the *legend* and *tick labels*, and removing the *zeroline*.

```python
# For phase names
label_trace = go.Scatter(
    x=[-350]*n_phase,
    y=label_y,
    mode='text',
    text=phases,
    textfont=dict(
        color='rgb(200,200,200)',
        size=15
    )
)
 
# For phase values
value_trace = go.Scatter(
    x=[350]*n_phase,
    y=label_y,
    mode='text',
    text=values,
    textfont=dict(
        color='rgb(200,200,200)',
        size=15
    )
)

data = [label_trace, value_trace]
 
layout = go.Layout(
    title="<b>Funnel Chart</b>",
    titlefont=dict(
        size=20,
        color='rgb(203,203,203)'
    ),
    shapes=shapes,
    height=560,
    width=800,
    showlegend=False,
    paper_bgcolor='rgba(44,58,71,1)',
    plot_bgcolor='rgba(44,58,71,1)',
    xaxis=dict(
        showticklabels=False,
        zeroline=False,
    ),
    yaxis=dict(
        showticklabels=False,
        zeroline=False
    )
)
 
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
```

#### Segmented Funnel Chart
Instead of having a single source of data like the *funnel charts*, the segmented funnel charts have multiple data sources.

```python
import plotly.plotly as py
import plotly.graph_objs as go

from __future__ import division
import pandas as pd
 
# campaign data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/segment-funnel-dataset.csv')
 
# color for each segment
colors = ['rgb(63,92,128)', 'rgb(90,131,182)', 'rgb(255,255,255)', 'rgb(127,127,127)', 'rgb(84,73,75)']
```

You can calculate the total number of users in each phase using `DataFrame.iterrows()` method.

```python
total = [sum(row[1]) for row in df.iterrows()]
```

Number of phases and segments can be calculated using the shape (returns a tuple) attribute of DataFrame.

```python
n_phase, n_seg = df.shape
```

We are using a fixed width for the plot and the width of each phase will be calculated according to the total users compared to the initial phase.

```python
plot_width = 600
unit_width = plot_width / total[0]
 
phase_w = [int(value * unit_width) for value in total]
 
# height of a section and difference between sections 
section_h = 100
section_d = 10

# shapes of the plot
shapes = []
 
# plot traces data
data = []
 
# height of the phase labels
label_y = []
```

A phase in the chart will be a rectangle made of smaller rectangles representing different segments.

```python
height = section_h * n_phase + section_d * (n_phase-1)

# rows of the DataFrame
df_rows = list(df.iterrows())

# iteration over all the phases
for i in range(n_phase):
    # phase name
    row_name = df.index[i]
    
    # width of each segment (smaller rectangles) will be calculated
    # according to their contribution in the total users of phase
    seg_unit_width = phase_w[i] / total[i]
    seg_w = [int(df_rows[i][1][j] * seg_unit_width) for j in range(n_seg)]
    
    # starting point of segment (the rectangle shape) on the X-axis
    xl = -1 * (phase_w[i] / 2)
    
    # iteration over all the segments
    for j in range(n_seg):
        # name of the segment
        seg_name = df.columns[j]
        
        # corner points of a segment used in the SVG path
        points = [xl, height, xl + seg_w[j], height, xl + seg_w[j], height - section_h, xl, height - section_h]
        path = 'M {0} {1} L {2} {3} L {4} {5} L {6} {7} Z'.format(*points)
        
        shape = {
                'type': 'path',
                'path': path,
                'fillcolor': colors[j],
                'line': {
                    'width': 1,
                    'color': colors[j]
                }
        }
        shapes.append(shape)
        
        # to support hover on shapes
        hover_trace = go.Scatter(
            x=[xl + (seg_w[j] / 2)],
            y=[height - (section_h / 2)],
            mode='markers',
            marker=dict(
                size=min(seg_w[j]/2, (section_h / 2)),
                color='rgba(255,255,255,1)'
            ),
            text="Segment : %s" % (seg_name),
            name="Value : %d" % (df[seg_name][row_name])
        )
        data.append(hover_trace)
        
        xl = xl + seg_w[j]

    label_y.append(height - (section_h / 2))

    height = height - (section_h + section_d)
```

We will use text mode to draw the name of phase and its value.

```python
# For phase names
label_trace = go.Scatter(
    x=[-350]*n_phase,
    y=label_y,
    mode='text',
    text=df.index.tolist(),
    textfont=dict(
        color='rgb(200,200,200)',
        size=15
    )
)

data.append(label_trace)
 
# For phase values (total)
value_trace = go.Scatter(
    x=[350]*n_phase,
    y=label_y,
    mode='text',
    text=total,
    textfont=dict(
        color='rgb(200,200,200)',
        size=15
    )
)

data.append(value_trace)
```

We will style the plot by changing the background color of the plot and the plot paper, hiding the legend and tick labels, and removing the zeroline.

```python
layout = go.Layout(
    title="<b>Segmented Funnel Chart</b>",
    titlefont=dict(
        size=20,
        color='rgb(230,230,230)'
    ),
    hovermode='closest',
    shapes=shapes,
    showlegend=False,
    paper_bgcolor='rgba(44,58,71,1)',
    plot_bgcolor='rgba(44,58,71,1)',
    xaxis=dict(
        showticklabels=False,
        zeroline=False,
    ),
    yaxis=dict(
        showticklabels=False,
        zeroline=False
    )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
```

#### Reference
See https://plot.ly/python/reference/#layout-shapes for more information!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install --user git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'funnel-chart.ipynb',
    'python/funnel-charts/',
    'Funnel Charts | plotly',
    'How to make funnel charts in Python with Plotly.',
    title = 'Python Funnel Charts | plotly',
    name = 'Funnel Charts',
    has_thumbnail='true',
    thumbnail='thumbnail/funnel-chart.jpg', 
    language='python', 
    page_type='example_index',
    display_as='financial',
    order=4,
    ipynb= '~notebook_demo/140')
```

```python

```