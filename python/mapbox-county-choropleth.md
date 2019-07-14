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
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.6.7
  plotly:
    description: How to make a Mapbox Choropleth Map of the Florida Counties in Python
      with Plotly.
    display_as: maps
    has_thumbnail: true
    ipynb: ~notebook_demo/56
    language: python
    layout: user-guide
    name: Mapbox Choropleth Maps
    order: 1.5
    page_type: u-guide
    permalink: python/mapbox-county-choropleth/
    thumbnail: thumbnail/county-level-choropleth.jpg
    title: Python Mapbox Choropleth Maps | plotly
---

#### Mapbox Access Token


To plot on Mapbox maps with Plotly you'll need a Mapbox account and a [Mapbox Access Token](https://www.mapbox.com/studio) which you can add to your [Plotly settings](https://plot.ly/settings/mapbox). If you're using a Chart Studio Enterprise server, please see additional instructions here: https://help.plot.ly/mapbox-atlas/.

```python
import plotly.graph_objects as go

mapbox_access_token = open(".mapbox_token").read()

fig = go.Figure(go.Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
    ))

fig.update_layout(
    height=600,
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        layers=[
            dict(
                sourcetype = 'geojson',
                source = 'https://raw.githubusercontent.com/plotly/datasets/master/florida-red-data.json',
                type = 'fill',
                color = 'rgba(163,22,19,0.8)'
            ),
            dict(
                sourcetype = 'geojson',
                source = 'https://raw.githubusercontent.com/plotly/datasets/master/florida-blue-data.json',
                type = 'fill',
                color = 'rgba(40,0,113,0.8)'
            )
        ],
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=27.8,
            lon=-83
        ),
        pitch=0,
        zoom=5.2,
        style='light'
    ),
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#scattermapbox for more information about mapbox and their attribute options.
