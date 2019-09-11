---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.3
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

#### Visualization of MRI volume slices

```python
# Import data
import time
import numpy as np

from skimage import io

vol = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")
volume = vol.T
r, c = volume[0].shape

# Visualize data
import plotly.graph_objects as go

nb_frames = 10

# Define frames
fig = go.Figure(frames=[go.Frame(data=go.Surface(
    z=(6.7 - k * 0.1) * np.ones((r, c)),
    surfacecolor=np.flipud(volume[67 - k]),
    cmin=0, cmax=200
    ))
    for k in range(nb_frames)])

# Add data to be displayed before animation starts
fig.add_trace(go.Surface(
    z=6.7 * np.ones((r, c)),
    surfacecolor=np.flipud(volume[67]),
    colorscale='Gray',
    cmin=0, cmax=200,
    colorbar=dict(thickness=20, ticklen=4)
    ))

# Sliders
sliders=[
    dict(
        steps=[dict(method='animate',
                    args= [None, dict(fromcurrent=True, mode='immediate', transition=dict(duration=0))
                          ],
                    label='{:d}'.format(k+1)) 
               for k in range(nb_frames)],
        transition= dict(duration=0),
    )
]

# Layout
fig.update_layout(
         title='Slices in volumetric data',
         width=600,
         height=600,
         scene=dict(
                    zaxis=dict(range=[-0.1, 6.8], autorange=False),
                    aspectratio=dict(x=1, y=1, z=1),
                    ),
         updatemenus=[
             dict(type='buttons',
                  buttons=[dict(label='Play',
                                method='animate',
                                args=[None])])
         ],
         sliders=sliders
)

fig.show()
```

#### Credit:
All credit goes to Emilia Petrisor for this excellent animation!

Here's where you can find her:
- Her [Twitter](https://twitter.com/mathinpython) under the handle `@mathinpython`
- Her [GitHub Page](https://github.com/empet) with Username `empet`

```python
from scipy import stats
stats.scoreatpercentile(volume, 99.5)
```

#### Reference
For additional information and help setting up a slider in an animation, see https://plot.ly/python/gapminder-example/. For more documentation on creating animations with Plotly, see https://plot.ly/python/#animations.

