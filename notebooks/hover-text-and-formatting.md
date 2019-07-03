---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.7
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
    version: 3.6.5
  plotly:
    description: How to use hover text and formatting in Python with Plotly.
    display_as: layout_opt
    has_thumbnail: false
    ipynb: ~notebook_demo/198
    language: python
    layout: user-guide
    name: Hover Text and Formatting
    order: 20
    page_type: example_index
    permalink: python/hover-text-and-formatting/
    thumbnail: thumbnail/hover-text.jpg
    title: Hover Text and Formatting | Plotly
    v4upgrade: true
---

#### Add Hover Text

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2, 1, 6, 4, 4],
    hovertext=["Text A", "Text B", "Text C", "Text D", "Text E"],
    hoverinfo="text",
    marker=dict(
        color="green"
    ),
    showlegend=False
))

fig.show()
```

#### Format Hover Text

```python
import plotly.graph_objects as go


fig = go.Figure(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2.02825, 1.63728, 6.83839, 4.8485, 4.73463],
    hoverinfo="y",
    marker=dict(
        color="green"
    ),
    showlegend=False
))

fig.update_layout(
    title_text=("Set hover text formatting<br>" +
                "<a href= https://github.com/d3/d3-time-format/blob/master/README.md#locale_format>" +
                "https://github.com/d3/d3-time-format/blob/master/README.md#locale_format</a>"),
    title_font=dict(
        size=10
    ),
)

fig.update_xaxes(zeroline=False)
fig.update_yaxes(hoverformat=".2f")

fig.show()
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!
