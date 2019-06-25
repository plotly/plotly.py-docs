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
    description: How to add images to charts as background images or logos.
    display_as: style_opt
    has_thumbnail: true
    ipynb: ~notebook_demo/216
    language: python
    layout: user-guide
    name: Images
    order: 4
    page_type: example_index
    permalink: python/images/
    thumbnail: thumbnail/your-tutorial-chart.jpg
    title: Layout with images | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Add a Background Image

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
trace1= go.Scatter(x=[0,0.5,1,2,2.2],y=[1.23,2.5,0.42,3,1])
layout= go.Layout(images= [dict(
                  source= "https://images.plot.ly/language-icons/api-home/python-logo.png",
                  xref= "x",
                  yref= "y",
                  x= 0,
                  y= 3,
                  sizex= 2,
                  sizey= 2,
                  sizing= "stretch",
                  opacity= 0.5,
                  layer= "below")])
fig=go.Figure(data=[trace1],layout=layout)
py.iplot(fig,filename='EXAMPLES/background')
```

#### Add a Logo
See more examples of [adding logos to charts](https://plot.ly/python/logos/)!

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Bar(
        x=['-35.3', '-15.9', '-15.8', '-15.6', '-11.1',
           '-9.6', '-9.2', '-3.5', '-1.9', '-0.9',
           '1.0', '1.4', '1.7', '2.0', '2.8', '6.2',
           '8.1', '8.5', '8.5', '8.6', '11.4', '12.5',
           '13.3', '13.7', '14.4', '17.5', '17.7',
           '18.9', '25.1', '28.9', '41.4'],
        y=['Designers, musicians, artists, etc.',
           'Secretaries and administrative assistants',
           'Waiters and servers', 'Archivists, curators, and librarians',
           'Sales and related', 'Childcare workers, home car workers, etc.',
           'Food preparation occupations', 'Janitors, maids, etc.',
           'Healthcare technicians, assistants. and aides',
           'Counselors, social and religious workers',
           'Physical, life and social scientists', 'Construction',
           'Factory assembly workers', 'Machinists, repairmen, etc.',
           'Media and communications workers', 'Teachers',
           'Mechanics, repairmen, etc.', 'Financial analysts and advisers',
           'Farming, fishing and forestry workers',
           'Truck drivers, heavy equipment operator, etc.','Accountants and auditors',
           'Human resources, management analysts, etc.', 'Managers',
           'Lawyers and judges', 'Engineers, architects and surveyors',
           'Nurses', 'Legal support workers',
           'Computer programmers and system admin.', 'Police officers and firefighters',
           'Chief executives', 'Doctors, dentists and surgeons'],
        marker=dict(
            color='rgb(253, 240, 54)',
            line=dict(color='rgb(0, 0, 0)',
                      width=2)
        ),
        orientation='h',
    )
]

layout = go.Layout(
    images=[dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
      )],
    autosize=False, height=800, width=700,
    bargap=0.15, bargroupgap=0.1,
    barmode='stack', hovermode='x',
    margin=dict(r=20, l=300,
                  b=75, t=125),
    title='Moving Up, Moving Down<br><i>Percentile change in income between childhood and adulthood</i>',
    xaxis=dict(
        dtick=10, nticks=0,
        gridcolor='rgba(102, 102, 102, 0.4)',
        linecolor='#000', linewidth=1,
        mirror=True,
        showticklabels=True, tick0=0, tickwidth=1,
        title='<i>Change in percentile</i>',
    ),
    yaxis=dict(
        anchor='x',
        gridcolor='rgba(102, 102, 102, 0.4)', gridwidth=1,
        linecolor='#000', linewidth=1,
        mirror=True, showgrid=False,
        showline=True, zeroline=False,
        showticklabels=True, tick0=0,
        type='category',
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig,filename='EXAMPLES/logo')
```

#### Label Spectroscopy Data by Adding Multiple Images

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from scipy.signal import savgol_filter

#simulate spectroscopy data
def simulated_absorption(mu,sigma,intensity):
    data = [np.random.normal(mu[i],sigma[i],intensity[i]) for i in range(len(mu))]
    hists = [np.histogram(d,1000,range=(200,500),normed=True) for d in data]
    ys = [y for y,x in hists]
    s = savgol_filter(np.max(ys,axis = 0),41,3)
    return hists[0][1],s

mus = [[290,240,260],[330,350]]
sigmas = [[4,6,10],[5,4]]
intensities = [[100000,300000,700000],[40000,20000]]

simulated_absorptions = [simulated_absorption(m,s,i) for m,s,i in zip(mus,sigmas,intensities)]

#create traces from data
names=['Benzene','Naphthalene']
colors = ['red','maroon']
traces = [go.Scatter(x=x,y=y,name=n,line = dict(color=c)) for (x,y),n,c in zip(simulated_absorptions,names,colors)]

#add pictures using layout-images and then connect the image to its trace using annotations
layout= go.Layout(
    images= [dict(
        source= "https://raw.githubusercontent.com/michaelbabyn/plot_data/master/benzene.png",
        xref= "paper",
        yref= "paper",
        x= 0.75,
        y= 0.65,
        sizex= 0.3,
        sizey= 0.3,
        xanchor= "right",
        yanchor= "bottom"
      ),dict(
        source= "https://raw.githubusercontent.com/michaelbabyn/plot_data/master/naphthalene.png",
        xref="paper",
        yref= "paper",
        x= 0.9,
        y= 0.3,
        sizex= 0.3,
        sizey= 0.3,

        xanchor= "right",
        yanchor= "bottom"
      )
    ],
    annotations=[
        dict(
            x=93.0/300,
            y=0.07/0.1,
            xref='paper',
            yref='paper',
            showarrow=True,
            arrowhead=0,
            opacity=0.5,
            ax=250,
            ay=-40,
        ),
        dict(
            x=156/300,
            y=0.04/0.1,
            xref='paper',
            yref='paper',
            showarrow=True,
            arrowhead=0,
            opacity=0.5,
            ax=140,
            ay=-10,
        )
    ],
    title = 'Absorption Frequencies of Benzene and Naphthalene',
    yaxis = dict(hoverformat='.3f', title='Absorption'),
    xaxis = dict(title='Wavelength'),
    showlegend=False,
    height = 500,
    width = 900

)

fig = go.Figure(data=traces,layout=layout)
py.iplot(fig,filename='EXAMPLES/spectroscopy')
```

#### Zoom on Static Images

```python
import plotly.plotly as py
import plotly.graph_objs as go

img_width = 1600
img_height = 900
scale_factor = 0.5

layout = go.Layout(
    xaxis = go.layout.XAxis(
        visible = False,
        range = [0, img_width*scale_factor]),
    yaxis = go.layout.YAxis(
        visible=False,
        range = [0, img_height*scale_factor],
        # the scaleanchor attribute ensures that the aspect ratio stays constant
        scaleanchor = 'x'),
    width = img_width*scale_factor,
    height = img_height*scale_factor,
    margin = {'l': 0, 'r': 0, 't': 0, 'b': 0},
    images = [go.layout.Image(
        x=0,
        sizex=img_width*scale_factor,
        y=img_height*scale_factor,
        sizey=img_height*scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        source='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/bridge.jpg')]
)
# we add a scatter trace with data points in opposite corners to give the Autoscale feature a reference point
fig = go.Figure(data=[{
    'x': [0, img_width*scale_factor],
    'y': [0, img_height*scale_factor],
    'mode': 'markers',
    'marker': {'opacity': 0}}],layout = layout)
py.iplot(fig, filename='EXAMPLES/zoom_bridge')
```

#### Interactive Facial Recognition Overlays


This example requires the python library `dlib`, which can be install with pip.

`pip install dlib`

Note: building this library requires `cmake` to be installed and may take some time.

Also needed are the two `.dat` files (mmod_human_face_detector.dat and mmod_dog_hipsterizer.dat) which can be downloaded [here](https://github.com/davisking/dlib-models) compressed as .gz files. Download and uncompress them in the same root directory as this example.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import dlib


#load dlib's pretrained face detector
cnn_human_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')

#choose a file in your current directory or download https://raw.githubusercontent.com/michaelbabyn/plot_data/master/beethoven.jpg
f = 'beethoven.jpg'
img = dlib.load_rgb_image(f)

human_dets = cnn_human_detector(img,1)

#load dlib's pretrained dog-face detector
cnn_dog_detector = dlib.cnn_face_detection_model_v1('mmod_dog_hipsterizer.dat')

dog_dets = cnn_dog_detector(img, 1)

layout= go.Layout(
    xaxis = go.layout.XAxis(
        showticklabels = False,
        showgrid=False,
        zeroline=False,
        range = [0, img.shape[1]]
    ),
    yaxis = go.layout.YAxis(
        showticklabels = False,
        showgrid=False,
        zeroline=False,
        range = [0, img.shape[0]],
        scaleanchor = 'x'
        ),
    autosize=False,
    height=img.shape[0],
    width=img.shape[1],
    margin = {'l': 0, 'r': 0, 't': 0, 'b': 0},
    images= [dict(
        source= "https://raw.githubusercontent.com/michaelbabyn/plot_data/master/beethoven.jpg",
        x=0,
        sizex=img.shape[1],
        y=img.shape[0],
        sizey=img.shape[0],
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch"
     )]
)

humans=[
    go.Scatter(
        x=[d.rect.left(), d.rect.right(), d.rect.right(), d.rect.left(), d.rect.left()],
        y=[img.shape[0] - d.rect.top(),img.shape[0] - d.rect.top(),img.shape[0] - d.rect.bottom(),img.shape[0] - d.rect.bottom(),img.shape[0] - d.rect.top()],
        hoveron = 'fills',
        name = 'Human #{0}'.format(i+1),
        text = 'confidence: {:.2f}'.format(d.confidence),
        mode='lines',
        line = dict(width=4,color='red'),
        showlegend = False
        )
    for i,d in enumerate(human_dets)]

dogs = [
    go.Scatter(
        x=[d.rect.left(),d.rect.right(),d.rect.right(),d.rect.left(),d.rect.left()],
        y=[img.shape[0] - d.rect.top(),img.shape[0] - d.rect.top(),img.shape[0] - d.rect.bottom(),img.shape[0] - d.rect.bottom(),img.shape[0] - d.rect.top()],
        hoveron = 'fills',
        name = 'Dog #{0}'.format(i+1),
        text = 'confidence: {:.2f}'.format(d.confidence),
        mode='lines',
        line = dict(width=4,color='blue'),
        showlegend = False
        )
    for i,d in enumerate(dog_dets)]

py.iplot(dict(data=humans+dogs,layout=layout),filename='EXAMPLES/facial_rec')
```

#### Reference
See https://plot.ly/python/reference/#layout-images for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'images.ipynb', 'python/images/', 'Layout with images',
    'How to add images to charts as background images or logos.',
    title = 'Layout with images | plotly',
    name = 'Images',
    has_thumbnail='true', thumbnail='thumbnail/your-tutorial-chart.jpg',
    language='python', page_type='example_index',
    display_as='style_opt', order=4,
    ipynb= '~notebook_demo/216')
```

```python

```
