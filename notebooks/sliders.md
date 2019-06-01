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
    description: How to add slider controls to your plots in Python with Plotly.
    display_as: controls
    has_thumbnail: true
    ipynb: ~notebook_demo/85
    language: python
    layout: user-guide
    name: Sliders
    order: 1.5
    page_type: example_index
    permalink: python/sliders/
    thumbnail: thumbnail/slider2017.gif
    title: Python Slider Controls | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Sliders are available in version <b>1.12.6+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Simple Slider Control
Sliders can now be used in Plotly to change the data displayed or style of a plot!

```python
import plotly.plotly as py
import numpy as np

data = [dict(
        visible = False,
        line=dict(color='#00CED1', width=6),
        name = '𝜈 = '+str(step),
        x = np.arange(0,10,0.01),
        y = np.sin(step*np.arange(0,10,0.01))) for step in np.arange(0,5,0.1)]
data[10]['visible'] = True

py.iplot(data, filename='Single Sine Wave')
```

```python
steps = []
for i in range(len(data)):
    step = dict(
        method = 'restyle',  
        args = ['visible', [False] * len(data)],
    )
    step['args'][1][i] = True # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active = 10,
    currentvalue = {"prefix": "Frequency: "},
    pad = {"t": 50},
    steps = steps
)]

layout = dict(sliders=sliders)

fig = dict(data=data, layout=layout)

py.iplot(fig, filename='Sine Wave Slider')
```

#### Reference
Check out https://plot.ly/python/reference/#layout-updatemenus for more information!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
    
import publisher
publisher.publish(
    'sliders.ipynb', 'python/sliders/', 'Sliders | plotly',
    'How to add slider controls to your plots in Python with Plotly.',
    title = 'Python Slider Controls | plotly',
    name = 'Sliders',
    has_thumbnail='true', thumbnail='thumbnail/slider2017.gif', 
    language='python', page_type='example_index',
    display_as='controls', order=1.5,
    ipynb= '~notebook_demo/85')  
```

```python

```