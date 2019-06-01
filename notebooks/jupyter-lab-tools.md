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
    description: Using Plotly FigureWidgets with Jupyter Lab
    display_as: chart_events
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Jupyter Lab with FigureWidget
    order: 2
    page_type: example_index
    permalink: python/jupyter-lab-tools/
    thumbnail: thumbnail/ipython_widgets.jpg
    title: Jupyter Lab with FigureWidget
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Create a New View for Output


Display a FigureWidget and then create a new window to display it in so that you can scroll through your code but still keep an eye on what you're doing.


<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/create_view_for_output_jupyter_lab.gif'>

#### View Live Updates

With the output view it is easy to take full advantage of FigureWidgets new impertive-style graph updates since you can see your code and your graph at the same time.

<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/demonstrate_view_jupyter_lab.gif'>



#### Reference


See [these Jupyter notebooks](https://github.com/jonmmease/plotly_ipywidget_notebooks) for even more FigureWidget examples.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
    
import publisher
publisher.publish(
    'jupyter-lab-tools.ipynb', 'python/jupyter-lab-tools/', 'IPython Widgets | plotly',
    'Using Plotly FigureWidgets with Jupyter Lab',
    title = 'Jupyter Lab with FigureWidget',
    name = 'Jupyter Lab with FigureWidget',
    has_thumbnail='true', thumbnail='thumbnail/ipython_widgets.jpg', 
    language='python', page_type='example_index', 
    display_as='chart_events', order=2)
```

```python

```