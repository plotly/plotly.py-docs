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
    description: How to set configuration options of plotly graphs in python. Examples
      of both online and offline configurations.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/97
    language: python
    layout: base
    name: Configuration
    order: 7
    page_type: u-guide
    permalink: python/configuration-options/
    thumbnail: thumbnail/modebar-icons.png
    
    v4upgrade: true
---

#### Offline Configuration Options
Now you can pass a `config` dictionary with all configurations options such as `scrollZoom`, `editable`, and `displayModeBar`. For the complete list of config options check out: https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js

##### Enable Scroll Zoom

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={'scrollZoom': True})
```

##### Display ModeBar

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={'displayModeBar': True})
```

##### Edit Mode - change the title and axis titles

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={'editable': True})
```

##### Multiple Config Options at Once!

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={
    'scrollZoom': True,
    'displayModeBar': True,
    'editable': True
})
```

##### Remove Modebar Buttons

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={
    'modeBarButtonsToRemove': ['toggleSpikelines','hoverCompareCartesian']
})
```

#### Reference


See config options at https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js#L6
