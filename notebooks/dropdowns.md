---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.7
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
    version: 3.7.2
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
    v4upgrade: true
---

#### Methods
The [updatemenu method](https://plot.ly/python/reference/#layout-updatemenus-buttons-method) determines which [plotly.js function](https://plot.ly/javascript/plotlyjs-function-reference/) will be used to modify the chart. There are 4 possible methods:
- `"restyle"`: modify data or data attributes
- `"relayout"`: modify layout attributes
- `"update"`: modify data **and** layout attributes
- `"animate"`: start or pause an [animation](https://plot.ly/python/#animations)


#### Restyle Dropdown
The `"restyle"` method should be used when modifying the data and data attributes of the graph.<br>
**Update One Data Attribute**<br>
This example demonstrates how to update a single data attribute: chart `type` with the `"restyle"` method.

```python
import plotly.graph_objects as go

import pandas as pd

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")

# create figure
fig = go.Figure()

# Add surface trace
fig.add_trace(go.Surface(z=df.values.tolist(), colorscale="Viridis"))

# Update plot sizing
fig.update_layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    template="plotly_white",
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# Add dropdown
fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            buttons=list([
                dict(
                    args=["type", "surface"],
                    label="3D Surface",
                    method="restyle"
                ),
                dict(
                    args=["type", "heatmap"],
                    label="Heatmap",
                    method="restyle"
                )
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

# Add annotation
fig.update_layout(
    annotations=[
        go.layout.Annotation(text="Trace type:", showarrow=False,
                             x=0, y=1.085, yref="paper", align="left")
    ]
)

fig.show()
```

**Update Several Data Attributes**<br>
This example demonstrates how to update several data attributes: colorscale, colorscale direction, and line display with the "restyle" method.

```python
import plotly.graph_objects as go

import pandas as pd

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")

# Create figure
fig = go.Figure()

# Add surface trace
fig.add_trace(go.Heatmap(z=df.values.tolist(), colorscale="Viridis"))

# Update plot sizing
fig.update_layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=100, b=0, l=0, r=0),
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# Add drowdowns
button_layer_1_height = 1.08
fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            buttons=list([
                dict(
                    args=["colorscale", "Viridis"],
                    label="Viridis",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Cividis"],
                    label="Cividis",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Blues"],
                    label="Blues",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Greens"],
                    label="Greens",
                    method="restyle"
                ),
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        go.layout.Updatemenu(
            buttons=list([
                dict(
                    args=["reversescale", False],
                    label="False",
                    method="restyle"
                ),
                dict(
                    args=["reversescale", True],
                    label="True",
                    method="restyle"
                )
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.37,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        go.layout.Updatemenu(
            buttons=list([
                dict(
                    args=[{"contours.showlines": False, "type": "contour"}],
                    label="Hide lines",
                    method="restyle"
                ),
                dict(
                    args=[{"contours.showlines": True, "type": "contour"}],
                    label="Show lines",
                    method="restyle"
                ),
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.58,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
    ]
)

fig.update_layout(
    annotations=[
        go.layout.Annotation(text="colorscale", x=0, xref="paper", y=1.06, yref="paper",
                             align="left", showarrow=False),
        go.layout.Annotation(text="Reverse<br>Colorscale", x=0.25, xref="paper", y=1.07,
                             yref="paper", showarrow=False),
        go.layout.Annotation(text="Lines", x=0.54, xref="paper", y=1.06, yref="paper",
                             showarrow=False)
    ])
    
fig.show()
```

#### Relayout Dropdown
The `"relayout"` method should be used when modifying the layout attributes of the graph.<br>
**Update One Layout Attribute**<br>
This example demonstrates how to update a layout attribute: chart `type` with the `"relayout"` method.

```python
import plotly.graph_objects as go

# Generate dataset
import numpy as np

x0 = np.random.normal(2, 0.4, 400)
y0 = np.random.normal(2, 0.4, 400)
x1 = np.random.normal(3, 0.6, 600)
y1 = np.random.normal(6, 0.4, 400)
x2 = np.random.normal(4, 0.2, 200)
y2 = np.random.normal(4, 0.4, 200)

# Create figure
fig = go.Figure()

# Add traces
fig.add_trace(
    go.Scatter(
        x=x0,
        y=y0,
        mode="markers",
        marker=dict(color="DarkOrange")
    )
)

fig.add_trace(
    go.Scatter(
        x=x1,
        y=y1,
        mode="markers",
        marker=dict(color="Crimson")
    )
)

fig.add_trace(
    go.Scatter(
        x=x2,
        y=y2,
        mode="markers",
        marker=dict(color="RebeccaPurple")
    )
)

# Add buttons that add shapes
cluster0 = [go.layout.Shape(type="circle",
                            xref="x", yref="y",
                            x0=min(x0), y0=min(y0),
                            x1=max(x0), y1=max(y0),
                            line=dict(color="DarkOrange"))]
cluster1 = [go.layout.Shape(type="circle",
                            xref="x", yref="y",
                            x0=min(x1), y0=min(y1),
                            x1=max(x1), y1=max(y1),
                            line=dict(color="Crimson"))]
cluster2 = [go.layout.Shape(type="circle",
                            xref="x", yref="y",
                            x0=min(x2), y0=min(y2),
                            x1=max(x2), y1=max(y2),
                            line=dict(color="RebeccaPurple"))]

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(buttons=list([
            dict(label="None",
                 method="relayout",
                 args=["shapes", []]),
            dict(label="Cluster 0",
                 method="relayout",
                 args=["shapes", cluster0]),
            dict(label="Cluster 1",
                 method="relayout",
                 args=["shapes", cluster1]),
            dict(label="Cluster 2",
                 method="relayout",
                 args=["shapes", cluster2]),
            dict(label="All",
                 method="relayout",
                 args=["shapes", cluster0 + cluster1 + cluster2])
        ]),
        )
    ]
)

# Update remaining layout properties
fig.update_layout(
    title_text="Highlight Clusters",
    showlegend=False,
)

fig.show()
```

#### Update Dropdown
The `"update"` method should be used when modifying the data and layout sections of the graph.<br>
This example demonstrates how to update which traces are displayed while simulaneously updating layout attributes such as the chart title and annotations.

```python
import plotly.graph_objects as go

import pandas as pd

# Load dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
df.columns = [col.replace("AAPL.", "") for col in df.columns]

# Initialize figure
fig = go.Figure()

# Add Traces

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=list(df.High),
               name="High",
               line=dict(color="#33CFA5")))

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=[df.High.mean()] * len(df.index),
               name="High Average",
               visible=False,
               line=dict(color="#33CFA5", dash="dash")))

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=list(df.Low),
               name="Low",
               line=dict(color="#F06A6A")))

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=[df.Low.mean()] * len(df.index),
               name="Low Average",
               visible=False,
               line=dict(color="#F06A6A", dash="dash")))

# Add Annotations and Buttons
high_annotations = [dict(x="2016-03-01",
                         y=df.High.mean(),
                         xref="x", yref="y",
                         text="High Average:<br> %.3f" % df.High.mean(),
                         ax=0, ay=-40),
                    dict(x=df.High.idxmax(),
                         y=df.High.max(),
                         xref="x", yref="y",
                         text="High Max:<br> %.3f" % df.High.max(),
                         ax=0, ay=-40)]
low_annotations = [dict(x="2015-05-01",
                        y=df.Low.mean(),
                        xref="x", yref="y",
                        text="Low Average:<br> %.3f" % df.Low.mean(),
                        ax=0, ay=40),
                   dict(x=df.High.idxmin(),
                        y=df.Low.min(),
                        xref="x", yref="y",
                        text="Low Min:<br> %.3f" % df.Low.min(),
                        ax=0, ay=40)]

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            active=0,
            buttons=list([
                dict(label="None",
                     method="update",
                     args=[{"visible": [True, False, True, False]},
                           {"title": "Yahoo",
                            "annotations": []}]),
                dict(label="High",
                     method="update",
                     args=[{"visible": [True, True, False, False]},
                           {"title": "Yahoo High",
                            "annotations": high_annotations}]),
                dict(label="Low",
                     method="update",
                     args=[{"visible": [False, False, True, True]},
                           {"title": "Yahoo Low",
                            "annotations": low_annotations}]),
                dict(label="Both",
                     method="update",
                     args=[{"visible": [True, True, True, True]},
                           {"title": "Yahoo",
                            "annotations": high_annotations + low_annotations}]),
            ]),
        )
    ])

# Set title
fig.update_layout(title_text="Yahoo")

fig.show()
```

#### Style Dropdown
When adding dropdowns to Plotly charts, users have the option of styling the color, font, padding, and position of the dropdown menus. The example below demonstrates how to apply different styling options. See all updatemenu styling attributes here: https://plot.ly/python/reference/#layout-updatemenus.

```python
import plotly.graph_objects as go

# Set mapbox access token
# mapbox_access_token = "pk..."

# Load data and process data
df_wind = pd.read_csv("https://plot.ly/~datasets/2805.csv")
df_known_capacity = df_wind[df_wind["total_cpcy"] != -99999.000]
df_sum = df_known_capacity.groupby("manufac")["total_cpcy"].sum().sort_values(
    ascending=False).to_frame()
df_farms = pd.read_csv("https://plot.ly/~jackp/17256.csv")
df_farms.set_index("Wind Farm", inplace=True)

# Initialize figure
fig = go.Figure()

# Add trace
data = []
for mfr in list(df_sum.index):
    if mfr != "unknown":
        trace = dict(
            lat=df_wind[df_wind["manufac"] == mfr]["lat_DD"],
            lon=df_wind[df_wind["manufac"] == mfr]["long_DD"],
            name=mfr,
            marker=dict(size=4),
            type="scattermapbox"
        )
        fig.add_trace(go.Scattermapbox(
            lat=df_wind[df_wind["manufac"] == mfr]["lat_DD"],
            lon=df_wind[df_wind["manufac"] == mfr]["long_DD"],
            name=mfr,
            marker=dict(size=4)))

# Add dropdowns
wind_farm_buttons = [
    dict(
        args=[{
            "mapbox.center.lat": 38,
            "mapbox.center.lon": -94,
            "mapbox.zoom": 3,
            "annotations[0].text": "All US wind turbines (scroll to zoom)"
        }],
        label="USA",
        method="relayout"
    )
]

for farm, row in df_farms.iterrows():
    desc = []
    for col in df_farms.columns:
        if col not in ["DegMinSec", "Latitude", "Longitude"]:
            if str(row[col]) not in ["None", "nan", ""]:
                desc.append(col + ": " + str(row[col]).strip("'"))
    desc.insert(0, farm)
    wind_farm_buttons.append(
        dict(
            args=[{
                "mapbox.center.lat": row["Latitude"],
                "mapbox.center.lon": float(str(row["Longitude"]).strip("'")),
                "mapbox.zoom": 9,
                "annotations[0].text": "<br>".join(desc)
            }],
            label=" ".join(farm.split(" ")[0:2]),
            method="relayout"
        )
    )
    
fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            buttons=wind_farm_buttons[0:10],
            pad={"r": 0, "t": 10},
            x=0.1,
            xanchor="left",
            y=1.0,
            yanchor="top",
            bgcolor="#AAAAAA",
            active=0,
            bordercolor="#FFFFFF",
            font=dict(size=11, color="#000000")
        ),
        go.layout.Updatemenu(
            buttons=list([
                dict(
                    args=["mapbox.style", "dark"],
                    label="Dark",
                    method="relayout"
                ),
                dict(
                    args=["mapbox.style", "light"],
                    label="Light",
                    method="relayout"
                ),
                dict(
                    args=["mapbox.style", "satellite"],
                    label="Satellite",
                    method="relayout"
                ),
                dict(
                    args=["mapbox.style", "satellite-streets"],
                    label="Satellite with Streets",
                    method="relayout"
                )
            ]),
            direction="up",
            x=0.75,
            xanchor="left",
            y=0.05,
            yanchor="bottom",
            bgcolor="#000000",
            bordercolor="#FFFFFF",
            font=dict(size=11)
        ),
    ]
)

# Update layout
fig.update_layout(
    height=800,
    margin=dict(t=0, b=0, l=0, r=0),
    font=dict(color="#FFFFFF", size=11),
    paper_bgcolor="#000000",
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=3,
        style="dark"
    ),
)

# Add annotations
fig.update_layout(
    annotations=[
        dict(text="All US wind turbines (scroll to zoom)",
             font=dict(color="magenta", size=14), borderpad=10,
             x=0.05, y=0.05, xref="paper", yref="paper", align="left", showarrow=False,
             bgcolor="black"),
        dict(text="Wind<br>Farms", x=0.01, y=0.99, yref="paper", align="left",
             showarrow=False, font=dict(size=14))
    ])

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#layout-updatemenus for more information about `updatemenu` dropdowns.
