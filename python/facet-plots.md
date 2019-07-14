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
    description: How to make Facet and Trellis Plots in Python with Plotly.
    display_as: statistical
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Facet and Trellis Plots
    order: 10.2
    page_type: u-guide
    permalink: python/facet-plots/
    redirect_from: python/trellis-plots/
    thumbnail: thumbnail/facet-trellis-thumbnail.jpg
    title: Python Facet and Trellis Plots | plotly
---

#### Facet by Column
A `facet grid` is a generalization of a scatterplot matrix where we can "facet" a row and/or column by another variable. Given some tabular data, stored in a `pandas.DataFrame`, we can plot one variable against another to form a regular scatter plot, _and_ we can pick a third faceting variable to form panels along the rows and/or columns to segment the data even further, forming a bunch of panels. We can also assign a coloring rule or a heatmap based on a color variable to color the plot.

```python
import plotly.figure_factory as ff

import pandas as pd
mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

fig = ff.create_facet_grid(
    mpg,
    x='displ',
    y='cty',
    facet_col='cyl',
)

fig.show()
```

#### Facet by Row

```python
import plotly.figure_factory as ff

import pandas as pd
mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

fig = ff.create_facet_grid(
    mpg,
    x='displ',
    y='cty',
    facet_row='cyl',
    marker={'color': 'rgb(86, 7, 100)'},
)

fig.show()
```

#### Facet by Row and Column

```python
import plotly.figure_factory as ff

import pandas as pd
mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

fig = ff.create_facet_grid(
    mpg,
    x='displ',
    y='cty',
    facet_row='cyl',
    facet_col='drv',
    marker={'color': 'rgb(234, 239, 155)'},
)

fig.show()
```

#### Custom Colormap

```python
import plotly.figure_factory as ff

import pandas as pd
tips = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tips.csv')

fig = ff.create_facet_grid(
    tips,
    x='total_bill',
    y='tip',
    color_name='sex',
    show_boxes=False,
    marker={'size': 10, 'opacity': 1.0},
    colormap={'Male': 'rgb(165, 242, 242)', 'Female': 'rgb(253, 174, 216)'}
)
fig.show()
```

#### Label Variable Name:Value

```python
import plotly.figure_factory as ff

import pandas as pd
mtcars = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv')

fig = ff.create_facet_grid(
    mtcars,
    x='mpg',
    y='wt',
    facet_col='cyl',
    facet_col_labels='name',
    facet_row_labels='name',
)
fig.show()
```

#### Custom Labels

```python
import plotly.figure_factory as ff

import pandas as pd
mtcars = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv')

fig = ff.create_facet_grid(
    mtcars,
    x='wt',
    y='mpg',
    facet_col='cyl',
    facet_col_labels={4: '$2^2 = 4$', 6: '$\\frac{18}{3} = 6$', 8: '$2\cdot4 = 8$'},
    marker={'color': 'rgb(240, 100, 2)'},
)

fig.show()
```

#### Plot in 'ggplot2' style
To learn more about ggplot2, check out http://ggplot2.tidyverse.org/reference/facet_grid.html

```python
import plotly.figure_factory as ff

import pandas as pd
tips = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tips.csv')

fig = ff.create_facet_grid(
    tips,
    x='total_bill',
    y='tip',
    facet_row='sex',
    facet_col='smoker',
    marker={'symbol': 'circle-open', 'size': 10},
    ggplot2=True
)
fig.show()
```

#### Plot with 'scattergl' traces

```python
import plotly.figure_factory as ff

import pandas as pd
mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

grid = ff.create_facet_grid(
    mpg,
    x='class',
    y='displ',
    trace_type='scattergl',
)

fig.show()
```

#### Plot with Histogram Traces

```python
import plotly.figure_factory as ff

import pandas as pd
tips = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tips.csv')

fig = ff.create_facet_grid(
    tips,
    x='total_bill',
    y='tip',
    facet_row='sex',
    facet_col='smoker',
    trace_type='histogram',
)

fig.show()
```

#### Other Trace Types
Facet Grids support `scatter`, `scattergl`, `histogram`, `bar` and `box` trace types.

```python
import plotly.figure_factory as ff

import pandas as pd
tips = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tips.csv')

fig = ff.create_facet_grid(
    tips,
    y='tip',
    facet_row='sex',
    facet_col='smoker',
    trace_type='box',
)

fig.show()
```

#### Reference

```python
help(ff.create_facet_grid)
```
