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
    version: 3.7.3
  plotly:
    description: How missing values in the data appear in the plot
    display_as: file_settings
    language: python
    layout: base
    name: Missing Values
    order: 27
    permalink: python/missing-values/
    thumbnail: thumbnail/missing_values.jpg
---
### Missing Value in the Data

[connectgaps](https://plot.ly/python/reference/#scatter-connectgaps) determines if missing values in the provided data are shown as a gap in the graph or not. In [this tutorial](https://plot.ly/python/filled-area-on-mapbox/#multiple-filled-areas-with-a-scattermapbox-trace), we showed how to take benefit of this feature and illustrate multiple areas in mapbox. 

```python
import plotly.graph_objects as go 

fig = go.Figure(go.Scatter(
    x = [1,2,3,4,5,7],
    y = [2,3,4,None, 5,8],
    connectgaps = False))
 
fig.show()
```

#### Reference
See https://plot.ly/python/reference/#scatter-connectgaps for more information and chart attribute options!
