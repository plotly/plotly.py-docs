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
    description: How to set configuration options of plotly graphs in python. Examples
      of both online and offline configurations.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/97
    language: python
    layout: user-guide
    name: Configuration
    order: 7
    page_type: u-guide
    permalink: python/configuration-options/
    thumbnail: thumbnail/modebar-icons.png
    title: Configuration | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Online Configuration Options
Config options set via our API libraries are overridden on graphs hosted on plot.ly (i.e. when working online). 
To set configutation options online, you can edit the plot's embed url. Visit our embed tutorial: http://help.plot.ly/embed-graphs-in-websites/#step-8-customize-the-iframe for more information on customizing the embed url to remove the "Edit Chart" link, hide the modebar, or autosize the plot.


#### Offline Configuration Options
Now you can pass a `config` dictionary with all configurations options such as `showLink`, `linkText`, `scrollZoom`, and `displayModeBar`. For the complete list of config options check out: https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js

<br><br>Remove the "Edit Chart" link:

```python
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode()

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
]

config={'showLink': False}
iplot(data, config=config)
```

Edit Link Text:

```python
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
]

config = {'linkText': "Let's visit plot.ly !!!"}
iplot(data, config=config)
```

Enable Scroll Zoom

```python
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
]

config = {'scrollZoom': True}
iplot(data, config=config)
```

Display ModeBar

```python
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
]

config = {'displayModeBar': True}
iplot(data, config=config)
```

Edit Mode - change the title and axis titles

```python
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
]

config = {'editable': True}
iplot(data, config=config)
```

Multiple Config Options at Once!

```python
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
]

config = {
    'linkText': "Let's visit plot.ly !!!",
    'scrollZoom': True,
    'displayModeBar': True,
    'editable': True
}
iplot(data, config=config)
```

Remove Modebar Buttons

```python
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
]

config = {
    'modeBarButtonsToRemove': ['sendDataToCloud','hoverCompareCartesian']
}

iplot(data, config=config)
```

#### Reference

```python
import plotly.offline as offline
help(offline.plot)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'config_opts.ipynb', 'python/configuration-options/', 'Configuration',
    'How to set configuration options of plotly graphs in python. Examples of both online and offline configurations.',
    title = 'Configuration | plotly',
    name = 'Configuration',
    language='python', has_thumbnail= True,
    thumbnail= 'thumbnail/modebar-icons.png',
    display_as='file_settings', order=7, uses_plotly_offline=True,
    ipynb= '~notebook_demo/97')
```

```python

```