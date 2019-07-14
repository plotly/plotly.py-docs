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


#### Read the Data


Read both a [GeoJSON file](http://catalog.civicdashboards.com/dataset/cda82e8b-7a8b-411e-95ba-1200b921c35d/resource/5c5d19a0-b817-49e6-b76e-ea63a8e2c0f6/download/fd880c1e4d23463ca869f1122109b3eftemp.geojson) of the Florida counties and a [webpage](http://dos.myflorida.com/elections/data-statistics/voter-registration-statistics/voter-registration-monthly-reports/voter-registration-current-by-county/) indicating Florida's voting registration by county

```python
import pandas as pd
import string
import urllib

repub_democ_counties_url = 'http://dos.myflorida.com/elections/data-statistics/voter-registration-statistics/voter-registration-monthly-reports/voter-registration-current-by-county/'
florida_data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/florida_county_data.geojson'

repub_democ_counties = urllib.urlopen(repub_democ_counties_url).read()
florida_data = pd.read_json(florida_data_url)

county_names = []
county_names_dict = {}

for county in florida_data['features']:
    for m in range(len(county['properties']['name'])):
        if county['properties']['name'][m:m+6] == 'County':
            county_names.append(county['properties']['name'][0:m-1])
            county_names_dict[county['properties']['name'][0:m-1]] = county['properties']['name']

print county_names
```

Since we want to separate the counties into Republican and Democratic for the seperate coloring, and since the county names in the GeoJSON are fuller text descriptions of each county on the website, we need to parse through and convert the names in the GeoJSON to the website format


#### Color the Counties


We now run a script to color our counties based on political party. This involves parsing through our list of counties, finding their cooresponding Republican/Democratic votes on the website, and place our data into the cooresponding list `red_counties` or `blue_counties`, based on which party has more votes

```python
red_counties = []
blue_counties = []

for k, county in enumerate(county_names):
    for j in range(len(repub_democ_counties)):
        county_len = len(county)
        if repub_democ_counties[j:j+county_len] == string.upper(county):
            new_j = j
            while True:
                try:
                    int(repub_democ_counties[new_j])
                    break
                except ValueError:
                    new_j += 1

    repub_votes = ''
    while repub_democ_counties[new_j] != '<':
        if repub_democ_counties[new_j] != ',':
            repub_votes += repub_democ_counties[new_j]
        new_j += 1

    # advance to next set of numbers
    new_j += 11

    democ_votes = ''
    while repub_democ_counties[new_j] != '<':
        if repub_democ_counties[new_j] != ',':
            democ_votes += repub_democ_counties[new_j]
        new_j += 1

    try:
        repub_votes = int(repub_votes)
    except ValueError:
        repub_votes = 0
    try:
        democ_votes = int(democ_votes)
    except ValueError:
        democ_votes = 0

    if repub_votes >= democ_votes:
        red_counties.append(florida_data['features'][k])
    else:
        blue_counties.append(florida_data['features'][k])
```

#### Create JSON Files


In [plotly/datasets](https://github.com/plotly/datasets), you can find the generated JSON files below for the [red counties](https://raw.githubusercontent.com/plotly/datasets/master/florida-red-data.json) and [blue counties](https://raw.githubusercontent.com/plotly/datasets/master/florida-blue-data.json)

```python
import json

red_data = {"type": "FeatureCollection"}
red_data['features'] = red_counties

blue_data = {"type": "FeatureCollection"}
blue_data['features'] = blue_counties

with open('florida-red-data.json', 'w') as f:
    f.write(json.dumps(red_data))
with open('florida-blue-data.json', 'w') as f:
    f.write(json.dumps(blue_data))
```

and we can now plot our choropleth using Python. Make sure to have a [Mapbox Access Tolken](https://www.mapbox.com/studio) for the generation of the plot. For more information on plotting Mapbox maps in Python, checkout the [documentation](https://plot.ly/python/next/scattermapbox/)

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
