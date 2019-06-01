---
jupyter:
  jupytext:
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
    description: Interactive Data Analysis with Plotly
    display_as: chart_events
    has_thumbnail: true
    ipynb: ~notebook_demo/231
    language: python
    layout: user-guide
    name: Interactive Data Analysis with FigureWidget ipywidgets
    order: 23
    page_type: example_index
    permalink: python/figurewidget-app/
    thumbnail: thumbnail/multi-widget.jpg
    title: Interactive Data Analysis with FigureWidget ipywidgets
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

#### NYC Flights Database

```python
import datetime
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py

from ipywidgets import widgets
```

We'll be making an application to take a look at delays from all flights out of NYC in the year 2013.

```python
df = pd.read_csv(
    'https://raw.githubusercontent.com/yankev/testing/master/datasets/nycflights.csv')
df = df.drop(df.columns[[0]], axis=1)
```

```python
df.sample(3)
```

Let's get the set of all the `airlines`, so that we can type the right things into the search box later. 

```python
df['carrier'].unique()
```

Let's assign the widgets that we're going to be using in our app. In general all these widgets will be used to filter the data set, and thus what we visualize.

```python
month = widgets.IntSlider(
    value=1.0,
    min=1.0,
    max=12.0,
    step=1.0,
    description='Month:',
    continuous_update=False
)

use_date = widgets.Checkbox(
    description='Date: ',
    value=True,
)

container = widgets.HBox(children=[use_date, month])

textbox = widgets.Dropdown(
    description='Airline:   ',
    value='DL',
    options=df['carrier'].unique().tolist()
)

origin = widgets.Dropdown(
    options=list(df['origin'].unique()),
    value='LGA',
    description='Origin Airport:',
)


# Assign an emptry figure widget with two traces
trace1 = go.Histogram(x=df['arr_delay'], opacity=0.75, name='Arrival Delays')
trace2 = go.Histogram(x=df['dep_delay'], opacity=0.75, name='Departure Delays')
g = go.FigureWidget(data=[trace1, trace2],
                    layout=go.Layout(
                        title=dict(
                            text='NYC FlightDatabase'
                        ),
                        barmode='overlay'
                    ))
```

Let now write a function that will handle the input from the widgets, and alter the state of the graph.

```python
def validate():
    if origin.value in df['origin'].unique() and textbox.value in df['carrier'].unique():
        return True
    else:
        return False


def response(change):
    if validate():
        if use_date.value:
            filter_list = [i and j and k for i, j, k in
                           zip(df['month'] == month.value, df['carrier'] == textbox.value,
                               df['origin'] == origin.value)]
            temp_df = df[filter_list]

        else:
            filter_list = [i and j for i, j in
                           zip(df['carrier'] == 'DL', df['origin'] == origin.value)]
            temp_df = df[filter_list]
        x1 = temp_df['arr_delay']
        x2 = temp_df['dep_delay']
        with g.batch_update():
            g.data[0].x = x1
            g.data[1].x = x2
            g.layout.barmode = 'overlay'
            g.layout.xaxis.title = 'Delay in Minutes'
            g.layout.yaxis.title = 'Number of Delays'


origin.observe(response, names="value")
textbox.observe(response, names="value")
month.observe(response, names="value")
use_date.observe(response, names="value")
```

Time to try the app out!!

```python
container2 = widgets.HBox([origin, textbox])
widgets.VBox([container,
              container2,
              g])
```

```html
<img src = 'https://cloud.githubusercontent.com/assets/12302455/16637308/4e476280-43ac-11e6-9fd3-ada2c9506ee1.gif' >
```

#### Reference

```python
help(go.FigureWidget)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'figurewidget_app.ipynb', 'python/figurewidget-app/', 'IPython FigureWidget',
    'Interactive Data Analysis with Plotly',
    title='Interactive Data Analysis with FigureWidget ipywidgets',
    name='Interactive Data Analysis with FigureWidget ipywidgets',
    has_thumbnail='true', thumbnail='thumbnail/multi-widget.jpg',
    language='python', page_type='example_index',
    display_as='chart_events', order=23,
    ipynb='~notebook_demo/231')
```

```python

```