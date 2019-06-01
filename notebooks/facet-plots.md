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

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: `Facet Grids and Trellis Plots` are available in version <b>2.0.12+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Facet by Column
A `facet grid` is a generalization of a scatterplot matrix where we can "facet" a row and/or column by another variable. Given some tabular data, stored in a `pandas.DataFrame`, we can plot one variable against another to form a regular scatter plot, _and_ we can pick a third faceting variable to form panels along the rows and/or columns to segment the data even further, forming a bunch of panels. We can also assign a coloring rule or a heatmap based on a color variable to color the plot.

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd
mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

fig = ff.create_facet_grid(
    mpg,
    x='displ',
    y='cty',
    facet_col='cyl',
)

py.iplot(fig, filename='facet by col')
```

#### Facet by Row

```python
import plotly.plotly as py
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

py.iplot(fig, filename='facet by row')
```

#### Facet by Row and Column

```python
import plotly.plotly as py
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

py.iplot(fig, filename='facet by row and col')
```

#### Color by Categorical Variable

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd
mtcars = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv')

fig = ff.create_facet_grid(
    mtcars,
    x='mpg',
    y='wt',
    facet_col='cyl',
    color_name='cyl',
    color_is_cat=True,
)
py.iplot(fig, filename='facet - color by categorical variable')
```

#### Custom Colormap

```python
import plotly.plotly as py
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
py.iplot(fig, filename='facet - custom colormap')
```

#### Label Variable Name:Value

```python
import plotly.plotly as py
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
py.iplot(fig, filename='facet - label variable name')
```

#### Custom Labels

```python
import plotly.plotly as py
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

py.iplot(fig, filename='facet - custom labels')
```

#### Plot in 'ggplot2' style
To learn more about ggplot2, check out http://ggplot2.tidyverse.org/reference/facet_grid.html

```python
import plotly.plotly as py
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
py.iplot(fig, filename='facet - ggplot2 style')
```

#### Plot with 'scattergl' traces

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd
mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

grid = ff.create_facet_grid(
    mpg,
    x='class',
    y='displ',
    trace_type='scattergl',
)

py.iplot(grid, filename='facet - scattergl')
```

#### Plot with Histogram Traces

```python
import plotly.plotly as py
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

py.iplot(fig, filename='facet - histogram traces')
```

#### Other Trace Types
Facet Grids support `scatter`, `scattergl`, `histogram`, `bar` and `box` trace types. More trace types coming in the future.

```python
import plotly.plotly as py
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

py.iplot(fig, filename='facet - box traces')
```

#### Reference

```python
help(ff.create_facet_grid)
```

```python
! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'facet-and-trellis-plots.ipynb', 'python/facet-plots/', 'Facet and Trellis Plots',
    'How to make Facet and Trellis Plots in Python with Plotly.',
    title = 'Python Facet and Trellis Plots | plotly',
    redirect_from ='python/trellis-plots/',
    has_thumbnail='true', thumbnail='thumbnail/facet-trellis-thumbnail.jpg',
    language='python',
    display_as='statistical', order=10.2)
```

```python

```