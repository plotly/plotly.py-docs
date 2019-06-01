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
    description: How to add dropdowns to update Plotly chart attributes in Python.
    display_as: controls
    has_thumbnail: true
    ipynb: ~notebook_demo/85
    language: python
    layout: user-guide
    name: Dropdown Menus
    order: 2
    page_type: example_index
    permalink: python/dropdowns/
    thumbnail: thumbnail/dropdown.jpg
    title: Dropdown Menus | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Python Buttons are available in version <b>1.12.12+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Methods
The [updatemenu method](https://plot.ly/python/reference/#layout-updatemenus-buttons-method) determines which [plotly.js function](https://plot.ly/javascript/plotlyjs-function-reference/) will be used to modify the chart. There are 4 possible methods:
- `"restyle"`: modify data or data attributes
- `"relayout"`: modify layout attributes
- `"update"`: modify data **and** layout attributes 
- `"animate"`: start or pause an [animation](https://plot.ly/python/#animations))


#### Restyle Dropdown
The `"restyle"` method should be used when modifying the data and data attributes of the graph.<br>
**Update One Data Attribute**<br>
This example demonstrates how to update a single data attribute: chart `type` with the `"restyle"` method.

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import json
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

data = [go.Surface(z=df.values.tolist(), colorscale='Viridis')]

layout = go.Layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230, 230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        aspectratio = dict(x=1, y=1, z=0.7),
        aspectmode = 'manual'
    )
)

updatemenus=list([
    dict(
        buttons=list([   
            dict(
                args=['type', 'surface'],
                label='3D Surface',
                method='restyle'
            ),
            dict(
                args=['type', 'heatmap'],
                label='Heatmap',
                method='restyle'
            )             
        ]),
        direction = 'down',
        pad = {'r': 10, 't': 10},
        showactive = True,
        x = 0.1,
        xanchor = 'left',
        y = 1.1,
        yanchor = 'top' 
    ),
])

annotations = list([
    dict(text='Trace type:', x=0, y=1.085, yref='paper', align='left', showarrow=False)
])
layout['updatemenus'] = updatemenus
layout['annotations'] = annotations

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='cmocean-picker-one-dropdown')
```

**Update Several Data Attributes**<br>
This example demonstrates how to update several data attributes: colorscale, chart type, and line display with the "restyle" method.
This example uses the cmocean python package. You can install this package with `pip install cmocean`.

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import cmocean
import json
import numpy as np
import pandas as pd

def cmocean_to_plotly(cmap, pl_entries=100):
    h = 1.0/(pl_entries-1)
    pl_colorscale = []
    
    for k in range(pl_entries):
        C = map(np.uint8, np.array(cmap(k*h)[:3])*255)
        pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])
        
    return pl_colorscale

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

data = [go.Surface(z=df.values.tolist(), colorscale='Viridis')]

button_layer_1_height = 1.12
button_layer_2_height = 1.065

layout = go.Layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        aspectratio = dict(x=1, y=1, z=0.7 ),
        aspectmode = 'manual'
    )
)

updatemenus=list([
    dict(
        buttons=list([
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.haline)) ],
                label='Haline',
                method='restyle'
            ),
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.turbid))],
                label='Turbid',
                method='restyle'
            ),
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.speed))],
                label='Speed',
                method='restyle'
            ),
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.haline)) ],
                label='Tempo',
                method='restyle'
            ),
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.gray))],
                label='Gray',
                method='restyle'
            ),
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.phase))],
                label='Phase',
                method='restyle'
            ),  
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.balance)) ],
                label='Balance',
                method='restyle'
            ),
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.delta))],
                label='Delta',
                method='restyle'
            ),
            dict(
                args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.curl))],
                label='Curl',
                method='restyle'
            ),                       
        ]),
        direction = 'down',
        pad = {'r': 10, 't': 10},
        showactive = True,
        x = 0.1,
        xanchor = 'left',
        y = button_layer_1_height,
        yanchor = 'top'            
    ),
    dict(
        buttons=list([   
            dict(
                args=['reversescale', True],
                label='Reverse',
                method='restyle'
            ),
            dict(
                args=['reversescale', False],
                label='Undo',
                method='restyle'
            )                    
        ]),
        direction = 'down',
        pad = {'r': 10, 't': 10},
        showactive = True,
        x = 0.55,
        xanchor = 'left',
        y = button_layer_1_height,
        yanchor = 'top'            
    ),
    dict(
        buttons=list([   
            dict(
                args=[{'contours.showlines':False, 'type':'contour'}],
                label='Hide lines',
                method='restyle'
            ),
            dict(
                args=[{'contours.showlines':True, 'type':'contour'}],
                label='Show lines',
                method='restyle'
            ),                    
        ]),
        direction = 'down',
        pad = {'r': 10, 't': 10},
        showactive = True,
        x = 0.775,
        xanchor = 'left',
        y = button_layer_1_height,
        yanchor = 'top'            
    ),        
    dict(
        buttons=list([   
            dict(
                args=['type', 'surface'],
                label='3d Surface',
                method='restyle'
            ),
            dict(
                args=['type', 'heatmap'],
                label='Heatmap',
                method='restyle'
            ),  
            dict(
                args=['type', 'contour'],
                label='Contour',
                method='restyle'
            )                     
        ]),
        direction = 'down',
        pad = {'r': 10, 't': 10},
        showactive = True,
        x = 0.3,
        xanchor = 'left',
        y = button_layer_1_height,
        yanchor = 'top' 
    ),
])

annotations = list([
    dict(text='cmocean<br>scale', x=0, y=1.11, yref='paper', align='left', showarrow=False ),
    dict(text='Trace<br>type', x=0.25, y=1.11, yref='paper', showarrow=False ),
    dict(text="Colorscale", x=0.5, y=1.10, yref='paper', showarrow=False),
    dict(text="Lines", x=0.75, y=1.10, yref='paper', showarrow=False)
])
layout['updatemenus'] = updatemenus
layout['annotations'] = annotations

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='cmocean-picker-dropdown')
```

#### Relayout Dropdown
The `"relayout"` method should be used when modifying the layout attributes of the graph.<br>
**Update One Layout Attribute**<br>
This example demonstrates how to update a layout attribute: chart `type` with the `"relayout"` method.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x0 = np.random.normal(2, 0.4, 400)
y0 = np.random.normal(2, 0.4, 400)
x1 = np.random.normal(3, 0.6, 600)
y1 = np.random.normal(6, 0.4, 400)
x2 = np.random.normal(4, 0.2, 200)
y2 = np.random.normal(4, 0.4, 200)

trace0 = go.Scatter(
    x=x0,
    y=y0,
    mode='markers',
    marker=dict(color='#835AF1')
)
trace1 = go.Scatter(
    x=x1,
    y=y1,
    mode='markers',
    marker=dict(color='#7FA6EE')
)
trace2 = go.Scatter(
    x=x2,
    y=y2,
    mode='markers',
    marker=dict(color='#B8F7D4')
)
data = [trace0, trace1, trace2]

cluster0 = [dict(type='circle',
                 xref='x', yref='y',
                 x0=min(x0), y0=min(y0), 
                 x1=max(x0), y1=max(y0), 
                 opacity=.25,
                 line=dict(color='#835AF1'),
                 fillcolor='#835AF1')]
cluster1 = [dict(type='circle',
                 xref='x', yref='y',
                 x0=min(x1), y0=min(y1), 
                 x1=max(x1), y1=max(y1), 
                 opacity=.25,
                 line=dict(color='#7FA6EE'),
                 fillcolor='#7FA6EE')]
cluster2 = [dict(type='circle',
                 xref='x', yref='y',
                 x0=min(x2), y0=min(y2), 
                 x1=max(x2), y1=max(y2), 
                 opacity=.25,
                 line=dict(color='#B8F7D4'),
                 fillcolor='#B8F7D4')]

updatemenus = list([
    dict(buttons=list([   
            dict(label = 'None',
                 method = 'relayout',
                 args = ['shapes', []]),
            dict(label = 'Cluster 0',
                 method = 'relayout',
                 args = ['shapes', cluster0]),
            dict(label = 'Cluster 1',
                 method = 'relayout',
                 args = ['shapes', cluster1]),
            dict(label = 'Cluster 2',
                 method = 'relayout',
                 args = ['shapes', cluster2]),
            dict(label = 'All',
                 method = 'relayout',
                 args = ['shapes', cluster0+cluster1+cluster2])
        ]),
    )
])

layout = dict(title='Highlight Clusters', showlegend=False,
              updatemenus=updatemenus)

fig = dict(data=data, layout=layout)

py.iplot(fig, filename='relayout_option_dropdown')
```

#### Update Dropdown
The `"update"` method should be used when modifying the data and layout sections of the graph.<br>
This example demonstrates how to update which traces are displayed while simulaneously updating layout attributes such as the chart title and annotations.

```python
import plotly.plotly as py
import plotly.graph_objs as go 

from datetime import datetime
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df.columns = [col.replace('AAPL.', '') for col in df.columns]

trace_high = go.Scatter(x=list(df.index),
                        y=list(df.High),
                        name='High',
                        line=dict(color='#33CFA5'))

trace_high_avg = go.Scatter(x=list(df.index),
                            y=[df.High.mean()]*len(df.index),
                            name='High Average',
                            visible=False,
                            line=dict(color='#33CFA5', dash='dash'))

trace_low = go.Scatter(x=list(df.index),
                       y=list(df.Low),
                       name='Low',
                       line=dict(color='#F06A6A'))

trace_low_avg = go.Scatter(x=list(df.index),
                           y=[df.Low.mean()]*len(df.index),
                           name='Low Average',
                           visible=False,
                           line=dict(color='#F06A6A', dash='dash'))

data = [trace_high, trace_high_avg, trace_low, trace_low_avg]

high_annotations=[dict(x='2016-03-01',
                       y=df.High.mean(),
                       xref='x', yref='y',
                       text='High Average:<br>'+str(df.High.mean()),
                       ax=0, ay=-40),
                  dict(x=df.High.idxmax(),
                       y=df.High.max(),
                       xref='x', yref='y',
                       text='High Max:<br>'+str(df.High.max()),
                       ax=0, ay=-40)]
low_annotations=[dict(x='2015-05-01',
                      y=df.Low.mean(),
                      xref='x', yref='y',
                      text='Low Average:<br>'+str(df.Low.mean()),
                      ax=0, ay=40),
                 dict(x=df.High.idxmin(),
                      y=df.Low.min(),
                      xref='x', yref='y',
                      text='Low Min:<br>'+str(df.Low.min()),
                      ax=0, ay=40)]

updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'High',
                 method = 'update',
                 args = [{'visible': [True, True, False, False]},
                         {'title': 'Yahoo High',
                          'annotations': high_annotations}]),
            dict(label = 'Low',
                 method = 'update',
                 args = [{'visible': [False, False, True, True]},
                         {'title': 'Yahoo Low',
                          'annotations': low_annotations}]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True, True, True, True]},
                         {'title': 'Yahoo',
                          'annotations': high_annotations+low_annotations}]),
            dict(label = 'Reset',
                 method = 'update',
                 args = [{'visible': [True, False, True, False]},
                         {'title': 'Yahoo',
                          'annotations': []}])
        ]),
    )
])

layout = dict(title='Yahoo', showlegend=False,
              updatemenus=updatemenus)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='update_dropdown')
```

#### Style Dropdown
When adding dropdowns to Plotly charts, users have the option of styling the color, font, padding, and position of the dropdown menus. The example below demonstrates how to apply different styling options. See all updatemenu styling attributes here: https://plot.ly/python/reference/#layout-updatemenus.

```python
df_wind = pd.read_csv('https://plot.ly/~datasets/2805.csv')

df_known_capacity = df_wind[ df_wind['total_cpcy'] != -99999.000 ]
df_sum = df_known_capacity.groupby('manufac')['total_cpcy'].sum().sort_values(ascending=False).to_frame()

df_farms = pd.read_csv('https://plot.ly/~jackp/17256.csv')
df_farms.set_index('Wind Farm', inplace=True)

wind_farms=list([
    dict(
        args=[ { 
            'mapbox.center.lat':38,
            'mapbox.center.lon':-94,
            'mapbox.zoom':3,
            'annotations[0].text':'All US wind turbines (scroll to zoom)'
        } ],
        label='USA',
        method='relayout'
    )
])

for farm, row in df_farms.iterrows():
    desc = []
    for col in df_farms.columns:
        if col not in ['DegMinSec','Latitude','Longitude']:
            if str(row[col]) not in ['None','nan','']: 
                desc.append( col + ': ' + str(row[col]).strip("'") )
    desc.insert(0, farm)
    wind_farms.append( 
        dict(
            args=[ { 
                'mapbox.center.lat':row['Latitude'], 
                'mapbox.center.lon':float(str(row['Longitude']).strip("'")), 
                'mapbox.zoom':9,
                'annotations[0].text': '<br>'.join(desc)
            } ],
            label=' '.join(farm.split(' ')[0:2]),
            method='relayout'
        )
    )

data = []
for mfr in list(df_sum.index):
    if mfr != 'unknown':
        trace = dict(
            lat = df_wind[ df_wind['manufac'] == mfr ]['lat_DD'],
            lon = df_wind[ df_wind['manufac'] == mfr ]['long_DD'],
            name = mfr,
            marker = dict(size = 4),
            type = 'scattermapbox'
        )
    data.append(trace)

# mapbox_access_token = 'insert mapbox token here'

layout = dict(
    height = 800,
    margin = dict( t=0, b=0, l=0, r=0 ),
    font = dict( color='#FFFFFF', size=11 ),
    paper_bgcolor = '#000000',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=3,
        style='dark'
    ),
)

updatemenus=list([
    dict(
        buttons = wind_farms[0:10],
        pad = {'r': 0, 't': 10},
        x = 0.1,
        xanchor = 'left',
        y = 1.0,
        yanchor = 'top',
        bgcolor = '#AAAAAA',
        active = 99,
        bordercolor = '#FFFFFF',
        font = dict(size=11, color='#000000')
    ),
    dict(
        buttons=list([
            dict(
                args=['mapbox.style', 'dark'],
                label='Dark',
                method='relayout'
            ),                    
            dict(
                args=['mapbox.style', 'light'],
                label='Light',
                method='relayout'
            ),
            dict(
                args=['mapbox.style', 'satellite'],
                label='Satellite',
                method='relayout'
            ),
            dict(
                args=['mapbox.style', 'satellite-streets'],
                label='Satellite with Streets',
                method='relayout'
            )                    
        ]),
        direction = 'up',
        x = 0.75,
        xanchor = 'left',
        y = 0.05,
        yanchor = 'bottom',
        bgcolor = '#000000',
        bordercolor = '#FFFFFF',
        font = dict(size=11)
    ),        
])

annotations = list([
    dict(text='All US wind turbines (scroll to zoom)', font=dict(color='magenta',size=14), borderpad=10, 
         x=0.05, y=0.05, xref='paper', yref='paper', align='left', showarrow=False, bgcolor='black'),
    dict(text='Wind<br>Farms', x=0.01, y=0.99, yref='paper', align='left', showarrow=False,font=dict(size=14))
])

layout['updatemenus'] = updatemenus
layout['annotations'] = annotations

figure = dict(data=data, layout=layout)
py.iplot(figure, filename='wind-turbine-territory-dropdown')
```

#### Reference
See https://plot.ly/python/reference/#layout-updatemenus for more information about `updatemenu` dropdowns.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'dropdown.ipynb', 'python/dropdowns/', 'Dropdown Menus | plotly',
    'How to add dropdowns to update Plotly chart attributes in Python.',
    title='Dropdown Menus | plotly',
    name='Dropdown Menus',
    has_thumbnail='true', thumbnail='thumbnail/dropdown.jpg',
    language='python', page_type='example_index',
    display_as='controls', order=2, ipynb= '~notebook_demo/85')
```

```python

```