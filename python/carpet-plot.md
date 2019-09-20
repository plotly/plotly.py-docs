---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernel_info:
    name: python3
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
    version: 3.6.8
  plotly:
    description: How to make carpet plots in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/144
    language: python
    layout: user-guide
    name: Carpet Plots
    order: 26
    page_type: u-guide
    permalink: python/carpet-plot/
    thumbnail: thumbnail/carpet.jpg
    title: Carpet Plots | Plotly
---

<!-- #region -->
### Set X and Y Coordinates


To set the `x` and `y` coordinates use `x` and `y` attributes. If `x` coordindate values are ommitted a cheater plot will be created. The plot below has a `y` array specified but requires `a` and `b` parameter values before an axis may be plotted.
<!-- #endregion -->

```python
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10]
)

data = [trace1]

fig = go.Figure(data = data)
url = py.plot(fig, filename = "carpet/basic")
```

### Add Parameter Values

To save parameter values use the `a` and `b` attributes.

```python inputHidden=false outputHidden=false
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10]
)

data = [trace1]

fig = go.Figure(data = data)
py.iplot(fig, filename = "carpet/add-parameters")
```

### Add A and B axis

Use `aaxis` or `baxis` list to make changes to the axes. For a more detailed list of attributes refer to [R reference](https://plot.ly/r/reference/#carpet-aaxis).

```python inputHidden=false outputHidden=false
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
    aaxis = dict(
        tickprefix = 'a = ',
        ticksuffix = 'm',
        smoothing = 1,
        minorgridcount = 9,
    ),
    baxis = dict(
        tickprefix = 'b = ',
        ticksuffix = 'pa',
        smoothing = 1,
        minorgridcount = 9,
    )
)

data = [trace1]

fig = go.Figure(data = data)
py.iplot(fig, filename = "carpet/add-axes")
```

### Alternate input format

The data arrays `x`, `y` may either be specified as one-dimensional arrays of data or as arrays of arrays. If one-dimensional, then `x`, `y`, `a`, and `b` should all be the same length. If `x` and `y` are arrays of arrays, then the length of `a` should match the inner dimension and the length of `b` the outer dimension. The plot below represents the same plot as those above.

```python
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [4, 4.5, 5, 6],
    b = [1, 2, 3],
    y = [[2, 3, 5.5, 8],
         [3.5, 4.5, 6.5, 8.5],
         [4, 5, 7.5, 10]]
)

data = [trace1]

fig = go.Figure(data = data)
py.iplot(fig, filename = "carpet/input-format")
```

### Cheater plot layout


The layout of cheater plots is not unique and depends upon the `cheaterslope` and axis `cheatertype` parameters. If `x` is not specified, each row of the `x` array is constructed based on the the formula `a + cheaterslope * b`, where `a` and `b` are either the value or the integer index of `a` and `b` respectively, depending on the corresponding axis `cheatertype`. Although the layout of the axis below is different than the plots above, it represents the same data as the axes above.

```python
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [4, 4.5, 5, 6],
    b = [1, 2, 3],
    y = [[2, 3, 5.5, 8],
         [3.5, 4.5, 6.5, 8.5],
         [4, 5, 7.5, 10]],
    cheaterslope = -5,
    aaxis = dict(cheatertype = 'index'),
    baxis = dict(cheatertype = 'value')
)

data = [trace1]

fig = go.Figure(data = data)
py.iplot(fig, filename = "carpet/cheater-layout")
```

### Style A and B axis

```python inputHidden=false outputHidden=false
import plotly.graph_objs as go
import plotly.plotly as py

trace1 = go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
    aaxis = dict(
        tickprefix = 'a = ',
        ticksuffix = 'm',
        smoothing = 1,
        minorgridcount = 9,
        minorgridwidth = 0.6,
        minorgridcolor = 'white',
        gridcolor = 'white',
        color = 'white'
    ),
    baxis = dict(
        ticksuffix = 'Pa',
        smoothing = 1,
        minorgridcount = 9,
        minorgridwidth = 0.6,
        gridcolor = 'white',
        minorgridcolor = 'white',
        color = 'white'
    )
)

data = [trace1]

layout = go.Layout(
    plot_bgcolor = 'black',
    paper_bgcolor = 'black',
    xaxis = dict(
        showgrid = False,
        showticklabels = False
    ),
    yaxis = dict(
        showgrid = False,
        showticklabels = False
    )
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename = "carpet/styled")
```

### Add Points and Contours

To add points and lines see [Carpet Scatter Plots](https://plot.ly/python/carpet-scatter) or to add contours see [Carpet Contour Plots](https://plot.ly/python/carpet-contour)


### Reference

See https://plot.ly/python/reference/#carpet for more information and chart attribute options!
