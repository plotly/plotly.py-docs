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
  plotly:
    description: How to use Plotly offline inside IPython notebooks
    display_as: chart_studio
    has_thumbnail: true
    ipynb: ~notebook_demo/267
    language: python
    layout: user-guide
    name: Offline Plots in Plotly
    page_type: example_index
    permalink: python/offline/
    thumbnail: thumbnail/offline.png
    title: Plotly Offline for IPython Notebooks
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

#### Plotly Offline from Command Line
You can plot your graphs from a python script from command line. On executing the script, it will open a web browser with your Plotly Graph drawn.

```python
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])
```

#### Generating Offline Graphs within Jupyter Notebook
You can also plot your graphs offline inside a Jupyter Notebook Environment. First you need to initiate the Plotly Notebook mode as below:

```python
init_notebook_mode(connected=True)
```

Run at the start of every ipython notebook to use plotly.offline. This injects the plotly.js source files into the notebook.

```python
iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])
```

```python
import plotly.graph_objs as go

import numpy as np

x = np.random.randn(2000)
y = np.random.randn(2000)
iplot([go.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap')),
       go.Scatter(x=x, y=y, mode='markers', marker=dict(color='white', size=3, opacity=0.3))], show_link=False)
```

#### Plotting Offline with Cufflinks

```python
import cufflinks as cf

iplot(cf.datagen.lines().iplot(asFigure=True,
                               kind='scatter',xTitle='Dates',yTitle='Returns',title='Returns'))
```

#### Use with the Cloud
All methods in plotly.plotly will communicate with a Chart Studio Cloud or Chart Studio Enterprise. <br>
`get_figure` downloads a figure from plot.ly or Chart Studio Enterprise.<br>
You need to provide credentials to download figures: https://plot.ly/python/getting-started/

```python
import plotly.plotly as py

fig = py.get_figure('https://plot.ly/~jackp/8715', raw=True)
iplot(fig)
```

#### Static Image Export


The `plotly.io.to_image` function can then be used to convert a plotly figure to a static image bytes string.

```python
import plotly.io as pio

static_image_bytes = pio.to_image(fig, format='png')
```

Use `IPython.display.Image` to display the image bytes as image in the notebook

```python
from IPython.display import Image

Image(static_image_bytes)
```

Use `plotly.io.write_image` to convert a figure to a static image and write it to a file or writeable object.

Make sure to add a file extension or specify the file type using the format parameter.

```python
pio.write_image(fig, file='plotly_static_image.png', format='png')
```

### Reference
For more information, run `help(plotly.offline.iplot)` or `help(plotly.offline.plot)` or `help(plotly.io.to_image)` or `help(plotly.io.write_image)`

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'plotly_offline.ipynb', 'python/offline/', 'Plotly Offline for IPython Notebooks',
    'How to use Plotly offline inside IPython notebooks',
    title= 'Plotly Offline for IPython Notebooks',
    name = 'Offline Plots in Plotly',
    has_thumbnail='false',
    language='python', page_type='example_index',
    ipynb= '~notebook_demo/267',
    uses_plotly_offline=True
)
```

```python

```
