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
    description: How to make Gantt Charts in Python with Plotly. Gantt Charts use
      horizontal bars to represent the start and end times of tasks.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/6
    language: python
    layout: user-guide
    name: Gantt Charts
    order: 5.5
    page_type: u-guide
    permalink: python/gantt/
    thumbnail: thumbnail/gantt.jpg
    title: Python Gantt Charts | plotly
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Version Check
Note: Gantt Charts are available in version <b>1.12.2+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version
<!-- #endregion -->

```python deletable=true editable=true
import plotly
plotly.__version__
```

<!-- #region {"deletable": true, "editable": true} -->
#### Simple Gantt Chart
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

fig = ff.create_gantt(df)
py.iplot(fig, filename='gantt-simple-gantt-chart', world_readable=True)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Index by Numeric Variable
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Complete=10),
      dict(Task="Job B", Start='2008-12-05', Finish='2009-04-15', Complete=60),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Complete=95)]

fig = ff.create_gantt(df, colors='Viridis', index_col='Complete', show_colorbar=True)
py.iplot(fig, filename='gantt-numeric-variable', world_readable=True)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Index by String Variable
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-01', Resource='Apple'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource='Grape'),
      dict(Task="Job C", Start='2009-04-20', Finish='2009-09-30', Resource='Banana')]

colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(210, 60, 180)']

fig = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True, show_colorbar=True)
py.iplot(fig, filename='gantt-string-variable', world_readable=True)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Use a Dictionary for Colors
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2016-01-01', Finish='2016-01-02', Resource='Apple'),
      dict(Task="Job B", Start='2016-01-02', Finish='2016-01-04', Resource='Grape'),
      dict(Task="Job C", Start='2016-01-02', Finish='2016-01-03', Resource='Banana')]

colors = dict(Apple = 'rgb(220, 0, 0)',
              Grape = 'rgb(170, 14, 200)',
              Banana = (1, 0.9, 0.16))

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True)
py.iplot(fig, filename='gantt-dictioanry-colors', world_readable=True)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Use a Pandas Dataframe
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gantt_example.csv')

fig = ff.create_gantt(df, colors=['#333F44', '#93e4c1'], index_col='Complete', show_colorbar=True,
                      bar_width=0.2, showgrid_x=True, showgrid_y=True)
py.iplot(fig, filename='gantt-use-a-pandas-dataframe', world_readable=True)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Using Hours and Minutes in Times
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

df = [
    dict(Task='Morning Sleep', Start='2016-01-01', Finish='2016-01-01 6:00:00', Resource='Sleep'),
    dict(Task='Breakfast', Start='2016-01-01 7:00:00', Finish='2016-01-01 7:30:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 9:00:00', Finish='2016-01-01 11:25:00', Resource='Brain'),
    dict(Task='Break', Start='2016-01-01 11:30:00', Finish='2016-01-01 12:00:00', Resource='Rest'),
    dict(Task='Lunch', Start='2016-01-01 12:00:00', Finish='2016-01-01 13:00:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 13:00:00', Finish='2016-01-01 17:00:00', Resource='Brain'),
    dict(Task='Exercise', Start='2016-01-01 17:30:00', Finish='2016-01-01 18:30:00', Resource='Cardio'), 
    dict(Task='Post Workout Rest', Start='2016-01-01 18:30:00', Finish='2016-01-01 19:00:00', Resource='Rest'),
    dict(Task='Dinner', Start='2016-01-01 19:00:00', Finish='2016-01-01 20:00:00', Resource='Food'),
    dict(Task='Evening Sleep', Start='2016-01-01 21:00:00', Finish='2016-01-01 23:59:00', Resource='Sleep')
]

colors = dict(Cardio = 'rgb(46, 137, 205)',
              Food = 'rgb(114, 44, 121)',
              Sleep = 'rgb(198, 47, 105)',
              Brain = 'rgb(58, 149, 136)',
              Rest = 'rgb(107, 127, 135)')

fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Daily Schedule',
                      show_colorbar=True, bar_width=0.8, showgrid_x=True, showgrid_y=True)
py.iplot(fig, filename='gantt-hours-minutes', world_readable=True)
```

#### Group Tasks Together

```python
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Resource='Complete'),
      dict(Task="Job-1", Start='2017-02-15', Finish='2017-03-15', Resource='Incomplete'),
      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Not Started'),
      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Complete'),
      dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Resource='Not Started'),
      dict(Task="Job-3", Start='2017-04-01', Finish='2017-04-20', Resource='Not Started'),
      dict(Task="Job-3", Start='2017-05-18', Finish='2017-06-18', Resource='Not Started'),
      dict(Task="Job-4", Start='2017-01-14', Finish='2017-03-14', Resource='Complete')]

colors = {'Not Started': 'rgb(220, 0, 0)',
          'Incomplete': (1, 0.9, 0.16),
          'Complete': 'rgb(0, 255, 100)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
py.iplot(fig, filename='gantt-group-tasks-together', world_readable=True)
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
For info on Plotly Range Slider and Selector, see: https://plot.ly/python/reference/#layout-xaxis-rangeselector.
<!-- #endregion -->

```python deletable=true editable=true
help(ff.create_gantt)
```

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'gantt.ipynb', 'python/gantt/', 'Python Gantt Charts | plotly',
    'How to make Gantt Charts in Python with Plotly. Gantt Charts use horizontal bars to represent the start and end times of tasks.',
    title='Python Gantt Charts | plotly',
    name='Gantt Charts',
    thumbnail='thumbnail/gantt.jpg', language='python',
    has_thumbnail='true', display_as='basic', order=5.5,
    ipynb= '~notebook_demo/6')
```

```python deletable=true editable=true

```