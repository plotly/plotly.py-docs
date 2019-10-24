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
    description: How to use text template in Python with Plotly.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/252
    language: python
    layout: base
    name: Text Template
    order: 40
    page_type: u-guide
    permalink: python/texttemplate/
    thumbnail: thumbnail/texttemplate.jpg
    title: Text Template and Formatting| plotly
    v4upgrade: true
---

### Customize Displayed Text with a Text Template
To show an arbitrary text in your chart you can use [texttemplate](https://plot.ly/python/reference/#pie-texttemplate), which is a template string used for rendering the information, and will override [textinfo](https://plot.ly/python/reference/#treemap-textinfo). 
This template string can include `variables` in %{variable} format, `numbers` in [d3-format's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_forma), and `date` in [d3-time-fomrat's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Time-Formatting.md#format).
`texttemplate` customizes the text that appears on your plot vs. [hovertemplate](https://plot.ly/python/reference/#pie-hovertemplate) customize the tooltip text. 

```python
import plotly.graph_objects as go

fig = go.Figure(go.Pie(
    values = [2, 5, 3, 2.5],
    labels = ["R", "Python", "Java Script", "Matlab"],
    texttemplate = "%{label}: %{value} (%{percent})",
    textposition = "inside"))

fig.show()
```

### Customize Text Template

The following example uses [textfont](https://plot.ly/python/reference/#scatterternary-textfont) to customize the added text. 

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatterternary(
    a = [3, 2, 5],
    b = [2, 5, 2],
    c = [5, 2, 2],
    mode = "markers+text",
    text = ["A", "B", "C"],
    texttemplate = "%{text}<br>(%{a:.2f}, %{b:.2f}, %{c:.2f})",
    textposition = "bottom center",
    textfont = {'family': "Times", 'size': [18, 21, 20], 'color': ["IndianRed", "MediumPurple", "DarkOrange"]}
))

fig.show()
```
### Set Date in Text Template
The following example shows how to show date by setting [axis.type](https://plot.ly/python/reference/#layout-yaxis-type) in [funnel charts](https://plot.ly/python/funnel-charts/).

```python
from plotly import graph_objects as go

fig = go.Figure()

fig.add_trace(go.Funnel(
    name = 'Montreal',
    orientation = "h",
    y = ["2018-01-01", "2018-07-01", "2019-01-01", "2020-01-01"],
    x = [100, 60, 40, 20],
    textposition = "inside",
    texttemplate = "%{label}"))

fig.add_trace(go.Funnel(
    name = 'Vancouver',
    orientation = "h",
    y = ["2018-01-01", "2018-07-01", "2019-01-01", "2020-01-01"],
    x = [90, 70, 50, 10],
    textposition = "inside",
    textinfo = "label"))

fig.update_layout(yaxis = {'type': 'date'})

fig.show()
```
