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
    description: How to make guage meter charts in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/11
    language: python
    layout: user-guide
    name: Gauge Charts
    order: 11
    page_type: u-guide
    permalink: python/gauge-charts/
    thumbnail: thumbnail/gauge.jpg
    title: Python Gauge Chart | plotly
    v4upgrade: true
---

#### Gauge Chart Outline

We will use `donut` charts with custom colors to create a `semi-circular` gauge meter, such that lower half of the chart is invisible(same color as background).

This `semi-circular` meter will be overlapped on a base `donut` chart to create the `analog range` of the meter. We will have to rotate the base chart to align the range marks in the edges of meter's section, because by default `Plotly` places them at the center of a pie section.


#### Base Chart (rotated)

To make a `gauge meter` with 5 equally sized sections, we will create 6 sections in the base chart. So that center(position of label) aligns with the edges of each section.

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Pie(
    values=[40, 10, 10, 10, 10, 10, 10],
    labels=["-", "0", "20", "40", "60", "80", "100"],
    domain={"x": [0, .48]},
    marker=dict(colors=['white']*7, line_width=1),
    name="Gauge",
    hole=.4,
    direction="clockwise",
    rotation=108,
    showlegend=False,
    hoverinfo="none",
    textinfo="label",
    textposition="outside"
))
fig.show()
```

##### Meter Chart

Now we will superimpose our `semi-circular` meter on top of this.<br>
For that, we will also use 6 sections, but one of them will be invisible to form the lower half (colored same as the background).

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Pie(
    values=[50, 10, 10, 10, 10, 10],
    labels=["Log Level", "Debug", "Info", "Warn", "Error", "Fatal"],
    domain={"x": [0, .48]},
    marker=dict(colors=[
            'rgb(255, 255, 255)',
            'rgb(232,226,202)',
            'rgb(226,210,172)',
            'rgb(223,189,139)',
            'rgb(223,162,103)',
            'rgb(226,126,64)'
        ], line_width=1),
    name="Gauge",
    hole=.3,
    direction="clockwise",
    rotation=90,
    showlegend=False,
    hoverinfo="none",
    textinfo="label",
    textposition="inside"
))

fig.show()
```

You can see that the first section's value is equal to the sum of other sections.<br>
We are using `rotation` and `direction` parameters to start the sections from 3 o'clock `[rotation=90]` instead of the default value of 12 o'clock `[rotation=0]`.


##### Dial

Now we need a `dial` to show the current position in the meter at a particular time.<br>
`Plotly's` [path shape](https://plot.ly/python/reference/#layout-shapes-path) can be used for this. A nice explanation of SVG path is available [here](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths) by Mozilla.<br>
We can use a `filled triangle` to create our `Dial`.



```
'shapes': [
    {
        'type': 'path',
        'path': 'M 0.235 0.5 L 0.24 0.62 L 0.245 0.5 Z',
        'fillcolor': 'rgba(44, 160, 101, 0.5)',
        'line': {
            'width': 0.5
        },
        'xref': 'paper',
        'yref': 'paper'
    }
]
```



For the `filled-triangle`, the first point `(0.235, 0.5)` is left to the center of meter `(0.24, 0.5)`, the second point `(0.24 0.62)` is representing the current position on the `semi-circle` and the third point `(0.245, 0.5)` is just right to the center.


`M` represents the `'Move'` command that moves cursor to a particular point, `L` is the `'Line To'` command and `Z` represents the `'Close Path'` command. This way, this path string makes a triangle with those three points.

```python
# Now put everything together!
import plotly.graph_objects as go

fig = go.Figure(data=go.Pie(
    values=[50, 10, 10, 10, 10, 10],
    labels=["Log Level", "Debug", "Info", "Warn", "Error", "Fatal"],
    domain={"x": [0, .48]},
    marker_colors=[
            'rgb(255, 255, 255)',
            'rgb(232,226,202)',
            'rgb(226,210,172)',
            'rgb(223,189,139)',
            'rgb(223,162,103)',
            'rgb(226,126,64)'
        ],
    name="Gauge",
    hole=.3,
    direction="clockwise",
    rotation=90,
    showlegend=False,
    hoverinfo="none",
    textinfo="label",
    textposition="inside"
))

# For numerical labels
fig.add_trace(go.Pie(
    values=[40, 10, 10, 10, 10, 10, 10],
    labels=["-", "0", "20", "40", "60", "80", "100"],
    domain={"x": [0, .48]},
    marker_colors=['rgba(255, 255, 255, 0)']*7,
    hole=.4,
    direction="clockwise",
    rotation=108,
    showlegend=False,
    hoverinfo="none",
    textinfo="label",
    textposition="outside"
))

fig.update_layout(
    xaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    ),
    yaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    ),
    shapes=[dict(
                type='path',
                path='M 0.235 0.5 L 0.24 0.65 L 0.245 0.5 Z',
                fillcolor='rgba(44, 160, 101, 0.5)',
                line_width=0.5,
                xref='paper',
                yref='paper')
    ],
    annotations=[
        dict(xref='paper',
             yref='paper',
             x=0.23,
             y=0.45,
            text='50',
            showarrow=False
        )
    ]
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!
