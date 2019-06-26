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
    description: An introduction to creating animations with Plotly in Python.
    display_as: animations
    has_thumbnail: true
    ipynb: ~notebook_demo/131
    language: python
    layout: user-guide
    name: Intro to Animations
    order: 1
    page_type: example_index
    permalink: python/animations/
    thumbnail: thumbnail/animations.gif
    title: Intro to Animations in Python | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Animations are available in version 1.12.10+
Run `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

#### Frames
Now, along with `data` and `layout`, `frames` is added to the keys that `figure` allows. Your `frames` key points to a list of figures, each of which will be cycled through upon instantiation of the plot.

<!-- #region -->
#### Online Mode
You can use `plotly.plotly.icreate_animations()` or `plotly.plotly.create_animations()` to make `online` animations that you save on the Plotly cloud.

There are two steps for making an online animation:
1. Make a grid
2. Make the plot with data from the grid

The reason for making a grid is because animations are created through our [v2 api](https://api.plot.ly/v2/). In this process, we create a [grid](https://api.plot.ly/v2/#grids) composed of columns, and then make a plot which contains referenced data from the grid columns. You can learn how to upload a grid at the [grid endpoint](https://api.plot.ly/v2/grids#create) of the and how to make a plot with a grid at the [plot endpoint](https://api.plot.ly/v2/plots#create) of the v2 api.

A grid consists of columns which fundamentally are 1D lists of numerical data with an associated name. They are instantiated with the `grid_objs` class `Column`. To make a column, simply assign a varaible with a Column:


$$
\begin{align*}
Column([...], name)
\end{align*}
$$

The `Grid` class is also part of the `grid_objs` module. A `Grid` takes a list of columns:

$$
\begin{align*}
grid = Grid([column_1, column_2, ...])
\end{align*}
$$


**Please Note:** filenames MUST BE unique. An error will be thrown if a grid is not created with a unique filename. Therefore we reccomend appending a timestamp to your grid filename to ensure the filename is unique.
<!-- #endregion -->

```python
import plotly.plotly as py
from plotly.grid_objs import Grid, Column

import time

column_1 = Column([0.5], 'x')
column_2 = Column([0.5], 'y')
column_3 = Column([1.5], 'x2')
column_4 = Column([1.5], 'y2')

grid = Grid([column_1, column_2, column_3, column_4])
py.grid_ops.upload(grid, 'ping_pong_grid'+str(time.time()), auto_open=False)
```

Now you need to reference the columns from the grid that you just uploaded. You can do so by using the built-in grid method `get_column_reference()` which takes the *column name* as its argument and returns the reference to the data in the grid. Since we are dealing with *referenced data* which is pointing to data and not *raw data*, we use `xsrc` and `ysrc` in the `figure` to represent the `x` and `y` analogues that are normally used.

Make your figure and create an animated plot!

```python
figure = {
    'data': [
        {
            'xsrc': grid.get_column_reference('x'),
            'ysrc': grid.get_column_reference('y'),
            'mode': 'markers',
        }
    ],
    'layout': {'title': 'Ping Pong Animation',
               'xaxis': {'range': [0, 2], 'autorange': False},
               'yaxis': {'range': [0, 2], 'autorange': False},
               'updatemenus': [{
                   'buttons': [
                       {'args': [None],
                        'label': 'Play',
                        'method': 'animate'}
               ],
               'pad': {'r': 10, 't': 87},
               'showactive': False,
               'type': 'buttons'
                }]},
    'frames': [
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x2'),
                    'ysrc': grid.get_column_reference('y2'),
                    'mode': 'markers',
                }
            ]
        },
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x'),
                    'ysrc': grid.get_column_reference('y'),
                    'mode': 'markers',
                }
            ]
        }
    ]
}

py.icreate_animations(figure, 'ping_pong'+str(time.time()))
```

<!-- #region -->
#### Adding Control Buttons to Animations
You can add play and pause buttons to control your animated charts by adding an `updatemenus` array to the `layout` of your `figure`. More information on style and placement of the buttons is available in Plotly's [`updatemenus` reference](https://plot.ly/python/reference/#layout-updatemenus).
<br>
The buttons are defined as follows:
```
'updatemenus': [{'type': 'buttons',
                 'buttons': [{'label': 'Your Label',
                              'method': 'animate',
                              'args': [See Below]}]}]
```
<!-- #endregion -->

#### Defining Button Arguments
- `None`: Setting `'args'` to undefined (i.e. `'args': [None]`) will create a simple play button that will animate all frames.
- string: Animate all frames with group `'<some string>'`. This is a way of scoping the animations in case you would prefer to animate without explicitly enumerating all frames.
- `['frame1', 'frame2', ...]`: Animate a sequence of named frames.
- `[{data: [], layout: {}, traces: []}, {...}]`: Nearly identical to animating named frames; though this variant lets you inline data instead of adding it as named frames. This can be useful for interaction where it's undesirable to add and manage named frames for ephemeral changes.
- `[null]`: A simple way to create a pause button (requires `mode: 'immediate'`). This argument dumps the currently queued frames (`mode: 'immediate'`), and then animates an empty sequence of frames (`[null]`).
- <b>Please Note:</b> We <b>do not</b> recommend using: `[ ]`. This syntax may cause confusion because it looks indistinguishable from a "pause button", but nested properties have logic that treats empty arrays as entirely removable, so it will function as a play button.<br><br>
Refer to the examples below to see the buttons in action!


#### Points Changing Size

```python
import plotly.plotly as py
from plotly.grid_objs import Grid, Column

import time

column_1 = Column([0.9, 1.1], 'x')
column_2 = Column([1.0, 1.0], 'y')
column_3 = Column([0.8, 1.2], 'x2')
column_4 = Column([1.2, 0.8], 'y2')
column_5 = Column([0.7, 1.3], 'x3')
column_6 = Column([0.7, 1.3], 'y3')
column_7 = Column([0.6, 1.4], 'x4')
column_8 = Column([1.5, 0.5], 'y4')
column_9 = Column([0.4, 1.6], 'x5')
column_10 = Column([1.2, 0.8], 'y5')

grid = Grid([column_1, column_2, column_3, column_4, column_5,
             column_6, column_7, column_8, column_9, column_10])
py.grid_ops.upload(grid, 'points_changing_size_grid'+str(time.time()), auto_open=False)

# create figure
figure = {
    'data': [
        {
            'xsrc': grid.get_column_reference('x'),
            'ysrc': grid.get_column_reference('y'),
            'mode': 'markers',
            'marker': {'color': '#48186a', 'size': 10}
        }
    ],
    'layout': {'title': 'Growing Circles',
               'xaxis': {'range': [0, 2], 'autorange': False},
               'yaxis': {'range': [0, 2], 'autorange': False},
               'updatemenus': [{
                   'buttons': [
                       {'args': [None],
                        'label': 'Play',
                        'method': 'animate'}
               ],
               'pad': {'r': 10, 't': 87},
               'showactive': False,
               'type': 'buttons'
                }]},
    'frames': [
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x2'),
                    'ysrc': grid.get_column_reference('y2'),
                    'mode': 'markers',
                    'marker': {'color': '#3b528b', 'size': 25}
                }
            ]
        },
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x3'),
                    'ysrc': grid.get_column_reference('y3'),
                    'mode': 'markers',
                    'marker': {'color': '#26828e', 'size': 50}
                }
            ]
        },
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x4'),
                    'ysrc': grid.get_column_reference('y4'),
                    'mode': 'markers',
                    'marker': {'color': '#5ec962', 'size': 80}
                }
            ]
        },
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x5'),
                    'ysrc': grid.get_column_reference('y5'),
                    'mode': 'markers',
                    'marker': {'color': '#d8e219', 'size': 100}
                }
            ]
        }
    ]
}
py.icreate_animations(figure, 'points_changing_size'+str(time.time()))
```

#### Offline Mode
`Animations` can be created either `offline` or `online`. To learn about how to set up working offline, check out the [offline documentation](https://plot.ly/python/offline/).


#### Basic Example
To re-run the animation see the following example with a play button.

```python
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML

init_notebook_mode(connected=True)

figure = {'data': [{'x': [0, 1], 'y': [0, 1]}],
          'layout': {'xaxis': {'range': [0, 5], 'autorange': False},
                     'yaxis': {'range': [0, 5], 'autorange': False},
                     'title': 'Start Title'},
          'frames': [{'data': [{'x': [1, 2], 'y': [1, 2]}]},
                     {'data': [{'x': [1, 4], 'y': [1, 4]}]},
                     {'data': [{'x': [3, 4], 'y': [3, 4]}],
                      'layout': {'title': 'End Title'}}]}

iplot(figure)
```

#### Simple Play Button

```python
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML

init_notebook_mode(connected=True)

figure = {'data': [{'x': [0, 1], 'y': [0, 1]}],
          'layout': {'xaxis': {'range': [0, 5], 'autorange': False},
                     'yaxis': {'range': [0, 5], 'autorange': False},
                     'title': 'Start Title',
                     'updatemenus': [{'type': 'buttons',
                                      'buttons': [{'label': 'Play',
                                                   'method': 'animate',
                                                   'args': [None]}]}]
                    },
          'frames': [{'data': [{'x': [1, 2], 'y': [1, 2]}]},
                     {'data': [{'x': [1, 4], 'y': [1, 4]}]},
                     {'data': [{'x': [3, 4], 'y': [3, 4]}],
                      'layout': {'title': 'End Title'}}]}

iplot(figure)
```

#### Moving Point on a Curve

```python
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML
import numpy as np

init_notebook_mode(connected=True)

t=np.linspace(-1,1,100)
x=t+t**2
y=t-t**2
xm=np.min(x)-1.5
xM=np.max(x)+1.5
ym=np.min(y)-1.5
yM=np.max(y)+1.5
N=50
s=np.linspace(-1,1,N)
xx=s+s**2
yy=s-s**2


data=[dict(x=x, y=y,
           mode='lines',
           line=dict(width=2, color='blue')
          ),
      dict(x=x, y=y,
           mode='lines',
           line=dict(width=2, color='blue')
          )
    ]

layout=dict(xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
            yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
            title='Kinematic Generation of a Planar Curve', hovermode='closest',
            updatemenus= [{'type': 'buttons',
                           'buttons': [{'label': 'Play',
                                        'method': 'animate',
                                        'args': [None]}]}])

frames=[dict(data=[dict(x=[xx[k]],
                        y=[yy[k]],
                        mode='markers',
                        marker=dict(color='red', size=10)
                        )
                  ]) for k in range(N)]

figure1=dict(data=data, layout=layout, frames=frames)
iplot(figure1)
```

#### Moving Frenet Frame Along a Planar Curve

```python
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML
import numpy as np

init_notebook_mode(connected=True)

N=50
s=np.linspace(-1,1,N)
vx=1+2*s
vy=1-2*s #v=(vx, vy) is the velocity
speed=np.sqrt(vx**2+vy**2)
ux=vx/speed #(ux, uy) unit tangent vector, (-uy, ux) unit normal vector
uy=vy/speed

xend=xx+ux #end coordinates for the unit tangent vector at (xx, yy)
yend=yy+uy

xnoe=xx-uy #end coordinates for the unit normal vector at (xx,yy)
ynoe=yy+ux


data=[dict(x=x, y=y,
           name='frame',
           mode='lines',
           line=dict(width=2, color='blue')),
      dict(x=x, y=y,
           name='curve',
           mode='lines',
           line=dict(width=2, color='blue'))
    ]

layout=dict(width=600, height=600,
            xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
            yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
            title='Moving Frenet Frame Along a Planar Curve', hovermode='closest',
            updatemenus= [{'type': 'buttons',
                           'buttons': [{'label': 'Play',
                                        'method': 'animate',
                                        'args': [None]}]}])

frames=[dict(data=[dict(x=[xx[k], xend[k], None, xx[k], xnoe[k]],
                        y=[yy[k], yend[k], None, yy[k], ynoe[k]],
                        mode='lines',
                        line=dict(color='red', width=2))
                  ]) for k in range(N)]

figure2=dict(data=data, layout=layout, frames=frames)
iplot(figure2)
```

#### Using a Slider and Buttons
The following example uses the well known [Gapminder dataset](https://www.gapminder.org/tag/gdp-per-capita/) to exemplify animation capabilites. This bubble chart animation shows the change in 'GDP per Capita' against the 'Life Expectancy' of several countries from the year 1952 to 2007, colored by their respective continent and sized by population.

```python
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML

import pandas as pd

init_notebook_mode(connected=True)

url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
dataset = pd.read_csv(url)

years = ['1952', '1962', '1967', '1972', '1977', '1982', '1987', '1992', '1997', '2002', '2007']
# make list of continents
continents = []
for continent in dataset['continent']:
    if continent not in continents:
        continents.append(continent)
# make figure
figure = {
    'data': [],
    'layout': {},
    'frames': []
}

# fill in most of layout
figure['layout']['xaxis'] = {'range': [30, 85], 'title': 'Life Expectancy'}
figure['layout']['yaxis'] = {'title': 'GDP per Capita', 'type': 'log'}
figure['layout']['hovermode'] = 'closest'
figure['layout']['sliders'] = {
    'args': [
        'transition', {
            'duration': 400,
            'easing': 'cubic-in-out'
        }
    ],
    'initialValue': '1952',
    'plotlycommand': 'animate',
    'values': years,
    'visible': True
}
figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]

sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Year:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}

# make data
year = 1952
for continent in continents:
    dataset_by_year = dataset[dataset['year'] == year]
    dataset_by_year_and_cont = dataset_by_year[dataset_by_year['continent'] == continent]

    data_dict = {
        'x': list(dataset_by_year_and_cont['lifeExp']),
        'y': list(dataset_by_year_and_cont['gdpPercap']),
        'mode': 'markers',
        'text': list(dataset_by_year_and_cont['country']),
        'marker': {
            'sizemode': 'area',
            'sizeref': 200000,
            'size': list(dataset_by_year_and_cont['pop'])
        },
        'name': continent
    }
    figure['data'].append(data_dict)

# make frames
for year in years:
    frame = {'data': [], 'name': str(year)}
    for continent in continents:
        dataset_by_year = dataset[dataset['year'] == int(year)]
        dataset_by_year_and_cont = dataset_by_year[dataset_by_year['continent'] == continent]

        data_dict = {
            'x': list(dataset_by_year_and_cont['lifeExp']),
            'y': list(dataset_by_year_and_cont['gdpPercap']),
            'mode': 'markers',
            'text': list(dataset_by_year_and_cont['country']),
            'marker': {
                'sizemode': 'area',
                'sizeref': 200000,
                'size': list(dataset_by_year_and_cont['pop'])
            },
            'name': continent
        }
        frame['data'].append(data_dict)

    figure['frames'].append(frame)
    slider_step = {'args': [
        [year],
        {'frame': {'duration': 300, 'redraw': False},
         'mode': 'immediate',
       'transition': {'duration': 300}}
     ],
     'label': year,
     'method': 'animate'}
    sliders_dict['steps'].append(slider_step)


figure['layout']['sliders'] = [sliders_dict]

iplot(figure)
```

#### Important Notes
- Defining `redraw`: Setting `redraw: false` is an optimization for scatter plots so that animate just makes changes without redrawing the whole plot. For other plot types, such as contour plots, every frame <b>must</b> be a total plot redraw, i.e. `redraw: true`.


### Dash Example


[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-animationplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-animationplot/", width="100%", height="750px", frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-animationplot/code", width="100%", height=500, frameBorder="0")
```

#### Reference
For additional information and attributes for creating bubble charts in Plotly see: https://plot.ly/python/bubble-charts/.
For more documentation on creating animations with Plotly, see https://plot.ly/python/#animations.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'intro-to-animations.ipynb', 'python/animations/', 'Intro to Animations | plotly',
    'An introduction to creating animations with Plotly in Python.',
    title='Intro to Animations in Python | plotly',
    name='Intro to Animations',
    language='python',
    page_type='example_index',
    has_thumbnail='true', thumbnail='thumbnail/animations.gif',
    display_as='animations', ipynb= '~notebook_demo/131', order=1)
```
