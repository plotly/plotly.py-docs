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
    description: How to create an plotly animation with slider that cycles through
      MRI cross-sections of a human brain.
    display_as: animations
    has_thumbnail: true
    ipynb: ~notebook_demo/190
    language: python
    layout: user-guide
    name: Visualizing MRI Volume Slices
    order: 4
    page_type: example_index
    permalink: python/visualizing-mri-volume-slices/
    thumbnail: thumbnail/brain-mri-animation_square.gif
    title: Visualizing MRI Volume Slices | plotly
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

#### Import Data

```python
import plotly.plotly as py
from plotly.grid_objs import Grid, Column

import time
import numpy as np

from skimage import io

vol = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")
volume = vol.T
r, c = volume[0].shape
```

#### Set the Color Scale

```python
pl_bone = [
    [0.0, 'rgb(0, 0, 0)'],
    [0.05, 'rgb(10, 10, 14)'],
    [0.1, 'rgb(21, 21, 30)'],
    [0.15, 'rgb(33, 33, 46)'],
    [0.2, 'rgb(44, 44, 62)'],
    [0.25, 'rgb(56, 55, 77)'],
    [0.3, 'rgb(66, 66, 92)'],
    [0.35, 'rgb(77, 77, 108)'],
    [0.4, 'rgb(89, 92, 121)'],
    [0.45, 'rgb(100, 107, 132)'],
    [0.5, 'rgb(112, 123, 143)'],
    [0.55, 'rgb(122, 137, 154)'],
    [0.6, 'rgb(133, 153, 165)'],
    [0.65, 'rgb(145, 169, 177)'],
    [0.7, 'rgb(156, 184, 188)'],
    [0.75, 'rgb(168, 199, 199)'],
    [0.8, 'rgb(185, 210, 210)'],
    [0.85, 'rgb(203, 221, 221)'],
    [0.9, 'rgb(220, 233, 233)'],
    [0.95, 'rgb(238, 244, 244)'],
    [1.0, 'rgb(255, 255, 255)']
]
```

#### Upload the Grid
Note: Since you cannot upload a grid with a filename shared by another grid you own in your profile, `str(time.time())` is appended to the filename to ensure a unique name is given to the grid.

Note: Due to the magnanimous size of data being uploaded, it will not work unless your daily data upload limit is high enough. Make sure your subscription is above the Free Community version. See the [Pricing and Plans page](https://plot.ly/products/cloud/) for more information.

```python
my_columns = []
nr_frames = 68
for k in range(nr_frames):
    my_columns.extend(
        [Column((6.7 - k * 0.1) * np.ones((r, c)), 'z{}'.format(k + 1)),
         Column(np.flipud(volume[67 - k]), 'surfc{}'.format(k + 1))]
    )
grid = Grid(my_columns)
py.grid_ops.upload(grid, 'anim_sliceshead'+str(time.time()), auto_open=False)
```

#### Create Data, Frames, Layout and Sliders

```python
data=[
    dict(
        type='surface',
        zsrc=grid.get_column_reference('z1'),
        surfacecolorsrc=grid.get_column_reference('surfc1'),
        colorscale=pl_bone,
        colorbar=dict(thickness=20, ticklen=4)
    )
]

frames=[]
for k in range(nr_frames):
    frames.append(
        dict(
            data=[dict(zsrc=grid.get_column_reference('z{}'.format(k + 1)),
                       surfacecolorsrc=grid.get_column_reference('surfc{}'.format(k + 1)))],
            name='frame{}'.format(k + 1)
        )
    )

sliders=[
    dict(
        steps=[dict(method='animate',
                    args= [['frame{}'.format(k + 1)],
                            dict(mode='immediate',
                                 frame= dict(duration=70, redraw= False),
                                 transition=dict(duration=0))],
                    label='{:d}'.format(k+1)) for k in range(68)],
        transition= dict(duration=0),
        x=0,
        y=0,
        currentvalue=dict(font=dict(size=12),
                          prefix='slice: ',
                          visible=True,
                          xanchor='center'
                         ),
        len=1.0
    )
]

axis3d = dict(
    showbackground=True,
    backgroundcolor="rgb(230, 230,230)",
    gridcolor="rgb(255, 255, 255)",
    zerolinecolor="rgb(255, 255, 255)",
)

layout3d = dict(
         title='Slices in volumetric data',
         font=dict(family='Balto'),
         width=600,
         height=600,
         scene=dict(xaxis=(axis3d),
                    yaxis=(axis3d),
                    zaxis=dict(axis3d, **dict(range=[-0.1, 6.8], autorange=False)),
                    aspectratio=dict(x=1, y=1, z=1),
                    ),
         updatemenus=[
             dict(type='buttons',
                  showactive=False,
                  y=1,
                  x=1.3,
                  xanchor='right',
                  yanchor='top',
                  pad=dict(t=0, r=10),
                  buttons=[dict(label='Play',
                                method='animate',
                                args=[
                                    None,
                                    dict(frame=dict(duration=70, redraw=False),
                                         transition=dict(duration=0),
                                         fromcurrent=True,
                                         mode='immediate')
                                ])])
         ],
        sliders=sliders
)
```

#### Upload to Plotly

```python
fig=dict(data=data, layout=layout3d, frames=frames)
py.icreate_animations(fig, filename='animslicesHead'+str(time.time()))
```

#### Credit:
All credit goes to Emilia Petrisor for this excellent animation!

Here's where you can find her:
- Her [Twitter](https://twitter.com/mathinpython) under the handle `@mathinpython`
- Her [GitHub Page](https://github.com/empet) with Username `empet`


#### Reference
For additional information and help setting up a slider in an animation, see https://plot.ly/python/gapminder-example/. For more documentation on creating animations with Plotly, see https://plot.ly/python/#animations.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'visualizing-mri-volume-slices.ipynb', 'python/visualizing-mri-volume-slices/', 'Visualizing MRI Volume Slices | plotly',
    'How to create an plotly animation with slider that cycles through MRI cross-sections of a human brain.',
    title='Visualizing MRI Volume Slices | plotly',
    name='Visualizing MRI Volume Slices',
    language='python',
    page_type='example_index', has_thumbnail='true', thumbnail='thumbnail/brain-mri-animation_square.gif',
    display_as='animations', order=4, ipynb='~notebook_demo/190')
```

```python

```