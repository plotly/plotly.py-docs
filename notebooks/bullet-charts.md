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
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to create Stephen Few Bullet Charts in Python with Plotly.
    display_as: statistical
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Bullet Charts
    order: 9
    page_type: u-guide
    permalink: python/bullet-charts/
    thumbnail: thumbnail/bullet_charts.jpg
    title: Python Bullet Charts | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: `Bullet Charts` are available in version <b>2.2.2+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

<!-- #region -->
#### Simple Bullet Chart
Stephen Few's Bullet Chart was invented to replace dashboard gauges and meters, combining both types of charts into simple bar charts with qualitative bars (`ranges`), quantitiative bars (`measures`) and performance points (`markers`) all into one simple layout. `ranges` typically are broken into three values: bad, okay, good, the `measures` are the darker bars that represent the actual values that a particular variable reached, and the points or `markers` usually indicate a goal point relative to the value achieved by the measure bar.

To use this figure factory, you can input either a pandas DataFrame as your data, or a sequence (ex. list, tuple, np.array, etc.) of dictionaries. You must map the column to the name of the particular column or key in your data. For example, if you want column `A` in your DataFrame to be the `measures` column, your function call will look like:

```
ff.create_bullet(data, measures='A', ...)
```

The valid params to set your DataFrame columns or dictionary keys to are `titles`, `subtitles`, `ranges`, `measures` and `markers`. The variable for `titles` and `subtitles` must contain strings as its elements and the rest lists.
<!-- #endregion -->

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd

data = pd.read_json('https://cdn.rawgit.com/plotly/datasets/master/BulletData.json')

fig = ff.create_bullet(
    data, markers='markers', measures='measures',
    ranges='ranges', subtitles='subtitle', titles='title',
)
py.iplot(fig, filename='bullet chart from a dataframe')
```

#### Vertical Bullet Chart
This example uses a tuple of dictionaries as its data input.

```python
import plotly.plotly as py
import plotly.figure_factory as ff

data = (
  {"label": "Revenue", "sublabel": "US$, in thousands",
   "range": [150, 225, 300], "performance": [220,270], "point": [250]},
  {"label": "Profit", "sublabel": "%", "range": [20, 25, 30],
   "performance": [21, 23], "point": [26]},
  {"label": "Order Size", "sublabel":"US$, average","range": [350, 500, 600],
   "performance": [100,320],"point": [550]},
  {"label": "New Customers", "sublabel": "count", "range": [1400, 2000, 2500],
   "performance": [1000, 1650],"point": [2100]},
  {"label": "Satisfaction", "sublabel": "out of 5","range": [3.5, 4.25, 5],
   "performance": [3.2, 4.7], "point": [4.4]}
)

fig = ff.create_bullet(
    data, titles='label', subtitles='sublabel', markers='point',
    measures='performance', ranges='range', orientation='v',
)
py.iplot(fig, filename='bullet chart from dict')
```

#### Use Your Own Colors
You can use different colors for the `range` and the `measure` columns. Set `range_colors` and `measure_colors` to a 2-item list of two colors to interpolate between.

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd

data = pd.read_json('https://cdn.rawgit.com/plotly/datasets/master/BulletData.json')

measure_colors=['rgb(63,102,153)', 'rgb(120,194,195)']
range_colors=['rgb(245,225,218)', 'rgb(241,241,241)']


fig = ff.create_bullet(
    data, orientation='h', markers='markers', measures='measures',
    ranges='ranges', subtitles='subtitle', titles='title',
    range_colors=range_colors,
    measure_colors=measure_colors
)
py.iplot(fig, filename='bullet chart - custom colors')
```

#### Custom Kwargs

```python
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd

data = pd.read_json('https://cdn.rawgit.com/plotly/datasets/master/BulletData.json')

fig = ff.create_bullet(
    data, orientation='v', markers='markers', measures='measures',
    ranges='ranges', subtitles='subtitle', titles='title',
    title='lots of kwargs', width=600, showlegend=True,
    scatter_options={'marker': {'size': 30,
                                'color': 'rgb(21, 166, 20)',
                                'symbol': 'hourglass'}}

)

# group legends
chart_elements = 6  # 3 grey bars, 2 blue bars, 1 marker
for cols, title in enumerate(data['title']):
    for ele in range(chart_elements):
        if ele == 0:
            showlegend = True
        else:
            showlegend = False
        fig['data'][cols * 6 + ele].update(
            {
                'legendgroup': '{}'.format(title),
                'name': title,
                'showlegend': showlegend
            }
        )

py.iplot(fig, filename='bullet chart - custom kwargs')
```

#### Reference

```python
help(ff.create_bullet)
```

```python
! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'bullet-chart.ipynb', 'python/bullet-charts/', 'Bullet Charts',
    "How to create Stephen Few Bullet Charts in Python with Plotly.",
    title = 'Python Bullet Charts | plotly',
    has_thumbnail='true', thumbnail='thumbnail/bullet_charts.jpg',
    language='python',
    display_as='statistical', order=9)
```

```python

```