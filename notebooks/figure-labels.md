---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.6
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
    description: How to set the title, legend-entries, and axis-titles in python.
    display_as: layout_opt
    has_thumbnail: false
    ipynb: ~notebook_demo/271
    language: python
    layout: user-guide
    name: Setting the Title, Legend Entries, and Axis Titles
    order: 0.5
    page_type: example_index
    permalink: python/figure-labels/
    thumbnail: thumbnail/labels.jpg
    title: Setting the Title, Legend Entries, and Axis Titles in Python | Examples
      | Plotly
    v4upgrade: true
---

```python
import plotly.graph_objects as go


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    name="Name of Trace 1"
))


fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[1, 0, 3, 2, 5, 4, 7, 6, 8],
    name="Name of Trace 2"
))

fig.update_layout(
    title=go.layout.Title(
        text="Plot Title",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="x Axis",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="y Axis",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
        )
    )
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#layout for more information!
