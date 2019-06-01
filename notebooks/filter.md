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
    description: How to use filters in Python with Plotly.
    display_as: transforms
    has_thumbnail: true
    ipynb: ~notebook_demo/195
    language: python
    layout: user-guide
    name: Filter
    order: 1
    page_type: example_index
    permalink: python/filter/
    thumbnail: thumbnail/filter.jpg
    title: Filter | Plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Plotly's python package is updated frequently. Run `pip install plotly --upgrade` to use the latest version.

```python
import plotly
plotly.__version__
```

#### Basic Example

```python
import plotly.offline as off

off.init_notebook_mode(connected=True)

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly']
score = [1,6,2,8,2,9,4,5,1,5,2,8]

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'filter',
    target = 'y',
    operation = '>',
    value = 4
  )]
)]

layout = dict(
    title = 'Scores > 4'
)

off.iplot({'data': data, 'layout': layout}, validate=False)
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'filter.ipynb', 'python/filter/', 'Filter',
    'How to use filters in Python with Plotly.',
    title = 'Filter | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/filter.jpg', 
    language='python', uses_plotly_offline=True,
    page_type='example_index',
    display_as='transforms', order=1,
    ipynb= '~notebook_demo/195')
```

```python

```