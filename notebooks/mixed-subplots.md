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
    description: How to make mixed subplots in Python with Plotly.
    display_as: multiple_axes
    has_thumbnail: true
    ipynb: ~notebook_demo/132
    language: python
    layout: user-guide
    name: Mixed Subplots
    order: 5
    page_type: example_index
    permalink: python/mixed-subplots/
    thumbnail: thumbnail/mixed_subplot.JPG
    title: Mixed Subplots | plotly
    v4upgrade: true
---

#### Mixed Subplot

A mixed subplot with custom geometry can be created by setting the `domain` parameter in the figure layout. See also the [subplots page](../subplots/).

```python
import plotly.graph_objects as go
import pandas as pd

# read in volcano database data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv',
                 encoding='latin1')

fig = go.Figure()

# frequency of Country
freq = df
freq = freq.Country.value_counts().reset_index().rename(columns={'index': 'x'})

# plot(1) top 10 countries by total volcanoes
fig.add_trace(go.Bar(
        x=freq['x'][0:10], y=freq['Country'][0:10], marker_color='crimson'))

# read in 3d volcano surface data
df_v = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

# plot(2) 3d surface of volcano
fig.add_trace(go.Surface(z=df_v.values.tolist(), colorscale='Reds', showscale=False))

# plot(3)  scattergeo map of volcano locations
fig.add_trace(go.Scattergeo(
  lon=df['Longitude'],
  lat=df['Latitude'],
  hoverinfo='text',
  marker=dict(size=4, opacity=0.8,
              color='crimson', colorscale='Viridis'),
  mode="markers",
))


# control the subplot below using domain in 'geo', 'scene', and 'axis'
fig.update_layout(
  plot_bgcolor='black',
  paper_bgcolor='black',
  titlefont_size=20,
  font_color='white',
  dragmode="zoom",
  geo=dict(
    domain=dict(x=[0, 0.55], y=[0, 0.9]), # for Scattergeo
    lakecolor="cyan",
    oceancolor="mediumblue",
    landcolor='white',
    projection_type="orthographic",
    scope="world",
    showlakes=True,
    showocean=True,
    showland=True,
    bgcolor='black'
  ),
  margin=dict(r=10, t=25, b=40, l=60),
  scene=dict(
        domain=dict(x=[0.5, 1], y=[0, 0.55]), # for 3D surface
        xaxis_gridcolor='white',
        yaxis_gridcolor='white',
        zaxis_gridcolor='white'),
  showlegend=False,
  title_text="<br>Volcano Database",
  xaxis=dict(anchor="y", domain=[0.6, 0.95]), # for bar plot
  yaxis=dict(anchor="x", domain=[0.65, 0.95], showgrid=False) # for bar plot
)

fig.update_layout(annotations=[dict(
            text="Source: NOAA",
            showarrow=False,
            xref="paper", yref="paper",
            x=0, y=0)])

fig = go.Figure(data=data, layout=layout)
fig.show()
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

