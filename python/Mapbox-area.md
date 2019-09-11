---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
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
    description: How to make a Mapbox Choropleth Map of US Counties in Python with
      Plotly.
    display_as: maps
    has_thumbnail: true
    ipynb: ~notebook_demo/56
    language: python
    layout: user-guide
    name: Mapbox Choropleth Maps
    order: 1
    page_type: example_index
    permalink: python/mapbox-county-choropleth/
    thumbnail: thumbnail/mapbox-choropleth.png
    title: Python Mapbox Choropleth Maps | plotly
---


### Mapbox Access Token

To plot on Mapbox maps with Plotly you *may* need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](/python/mapbox-layers/) documentation for more information.


### How to Show an Area on a Map 

There are three different ways to show an area in a mapbox: 
- Set `fill` attribute to 'toself' 
- Define the corresponding geojson
- Use the new trace type: [Choroplethmapbox](https://plot.ly/python/mapbox-county-choropleth/) for mapbox cases, or [Choropleth](https://plot.ly/python/choropleth-maps/) trace for non-mapbox ones.

The following example uses `Scattermapbox` and sets `fill = 'toself'` 

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    fill = "toself", 
    lon = [-74, -70, -70, -74], lat = [47, 47, 45, 45],
    marker = { 'size': 10, 'color': "orange" }))

fig.update_layout(
    mapbox = {
        'style': "stamen-terrain", 
        'center': {'lon': -73, 'lat': 46 }, 
        'zoom': 5}, 
    showlegend = False)
        
fig.show()
```

### Provide Gaps on Map

The following example shows how to use missing values in your data to provide gap in your graph. To ignore the gap on your plot, take benefit of [connectorgaps](https://plot.ly/python/reference/#scattermapbox-connectgaps) attribute.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "lines", fill = "toself",
    lon = [-10, -10, 8, 8, None, 30, 30, 50, 50, None, 100, 100, 80, 80], lat = [30, 6, 6, 30, None, 20, 30, 30, 20, None, 40, 50, 50, 40]))

fig.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 30, 'lat': 30}, 'zoom': 2},
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig.show()
```

### Use the Coresponding Geojson

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "markers",
    lon = [-73.605], lat = [45.51],
    marker = {'size': 20, 'color': ["cyan"]}))

fig.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': { 'lon': -73.6, 'lat': 45.5},
        'zoom': 12, 'layers': [{
            'source': {
                'type': "FeatureCollection",
                'features': [{
                    'type': "Feature",
                    'geometry': {
                        'type': "MultiPolygon",
                        'coordinates': [[[
                            [-73.606352888, 45.507489991], [-73.606133883, 45.50687600],
                            [-73.605905904, 45.506773980], [-73.603533905, 45.505698946],
                            [-73.602475870, 45.506856969], [-73.600031904, 45.505696003],
                            [-73.599379992, 45.505389066], [-73.599119902, 45.505632008],
                            [-73.598896977, 45.505514039], [-73.598783894, 45.505617001],
                            [-73.591308727, 45.516246185], [-73.591380782, 45.516280145],
                            [-73.596778656, 45.518690062], [-73.602796770, 45.521348046],
                            [-73.612239983, 45.525564037], [-73.612422919, 45.525642061],
                            [-73.617229085, 45.527751983], [-73.617279234, 45.527774160],
                            [-73.617304713, 45.527741334], [-73.617492052, 45.527498362],
                            [-73.617533258, 45.527512253], [-73.618074188, 45.526759105],
                            [-73.618271651, 45.526500673], [-73.618446320, 45.526287943],
                            [-73.618968507, 45.525698560], [-73.619388002, 45.525216750],
                            [-73.619532966, 45.525064183], [-73.619686662, 45.524889290],
                            [-73.619787038, 45.524770086], [-73.619925742, 45.524584939],
                            [-73.619954486, 45.524557690], [-73.620122362, 45.524377961],
                            [-73.620201713, 45.524298907], [-73.620775593, 45.523650879]
                        ]]]
                    }
                }]
            },
            'type': "fill", 'below': "traces", 'color': "royalblue"}]},
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#choroplethmapbox for more information about mapbox and their attribute options.
