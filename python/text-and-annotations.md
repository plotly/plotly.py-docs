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
    version: 3.6.5
  plotly:
    description: How to add text labels and annotations to plots in python.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/204
    language: python
    layout: base
    name: Text and Annotations
    order: 30
    permalink: python/text-and-annotations/
    thumbnail: thumbnail/text-and-annotations.png
    title: Text and Annotations | plotly
    v4upgrade: true
---

### Text scatter plot with Plotly Express

Here is an example that creates a scatter plot with text labels using Plotly Express.

```python
import plotly.express as px

gapminder = px.data.gapminder().query("year==2007 and continent=='Americas'")

fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", text="country", log_x=True, size_max=60)

fig.update_traces(textposition='top center')

fig.update_layout(
    height=800,
    title_text='GDP and Life Expectancy (Americas, 2007)'
)

fig.show()
```

### Adding Text to Data in Line and Scatter Plots

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode="lines+markers+text",
    name="Lines, Markers and Text",
    text=["Text A", "Text B", "Text C"],
    textposition="top center"
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode="markers+text",
    name="Markers and Text",
    text=["Text D", "Text E", "Text F"],
    textposition="bottom center"
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[3, 3, 3],
    mode="lines+text",
    name="Lines and Text",
    text=["Text G", "Text H", "Text I"],
    textposition="bottom center"
))

fig.show()
```

### Adding Hover Text to Data in Line and Scatter Plots

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[1, 3, 2],
    mode="markers",
    hovertext=["Text A", "Text B", "Text C"]
))

fig.update_layout(title_text="Hover over the points to see the text")

fig.show()
```

### Simple Annotation

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig.update_layout(
    showlegend=False,
    annotations=[
        go.layout.Annotation(
            x=2,
            y=5,
            xref="x",
            yref="y",
            text="dict Text",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
)

fig.show()
```

### Multiple Annotations

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))


fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig.update_layout(
    showlegend=False,
    annotations=[
        go.layout.Annotation(
            x=2,
            y=5,
            xref="x",
            yref="y",
            text="dict Text",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        go.layout.Annotation(
            x=4,
            y=4,
            xref="x",
            yref="y",
            text="dict Text 2",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
)

fig.show()
```

### 3D Annotations

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=["2017-01-01", "2017-02-10", "2017-03-20"],
    y=["A", "B", "C"],
    z=[1, 1000, 100000],
    name="z",
))

fig.update_layout(
    scene=go.layout.Scene(
        aspectratio=dict(
            x=1,
            y=1,
            z=1
        ),
        camera=dict(
            center=dict(
                x=0,
                y=0,
                z=0
            ),
            eye=dict(
                x=1.96903462608,
                y=-1.09022831971,
                z=0.405345349304
            ),
            up=dict(
                x=0,
                y=0,
                z=1
            )
        ),
        dragmode="turntable",
        xaxis=dict(
            title_text="",
            type="date"
        ),
        yaxis=dict(
            title_text="",
            type="category"
        ),
        zaxis=dict(
            title_text="",
            type="log"
        ),
        annotations=[dict(
            showarrow=False,
            x="2017-01-01",
            y="A",
            z=0,
            text="Point 1",
            xanchor="left",
            xshift=10,
            opacity=0.7
        ), dict(
            x="2017-02-10",
            y="B",
            z=4,
            text="Point 2",
            textangle=0,
            ax=0,
            ay=-75,
            font=dict(
                color="black",
                size=12
            ),
            arrowcolor="black",
            arrowsize=3,
            arrowwidth=1,
            arrowhead=1
        ), dict(
            x="2017-03-20",
            y="C",
            z=5,
            ax=50,
            ay=0,
            text="Point 3",
            arrowhead=1,
            xanchor="left",
            yanchor="bottom"
        )]
    ),
    xaxis=dict(title_text="x"),
    yaxis=dict(title_text="y")
)

fig.show()
```

### Custom Text Color and Styling

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode="lines+markers+text",
    name="Lines, Markers and Text",
    text=["Text A", "Text B", "Text C"],
    textposition="top right",
    textfont=dict(
        family="sans serif",
        size=18,
        color="crimson"
    )
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode="lines+markers+text",
    name="Lines and Text",
    text=["Text G", "Text H", "Text I"],
    textposition="bottom center",
    textfont=dict(
        family="sans serif",
        size=18,
        color="LightSeaGreen"
    )
))

fig.update_layout(showlegend=False)

fig.show()
```

### Styling and Coloring Annotations

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig.update_layout(
    showlegend=False,
    annotations=[
        go.layout.Annotation(
            x=2,
            y=5,
            xref="x",
            yref="y",
            text="max=5",
            showarrow=True,
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#ffffff"
            ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=20,
            ay=-30,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="#ff7f0e",
            opacity=0.8
        )
    ]
)

fig.show()
```

### Disabling Hover Text

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, ],
    y=[10, 30, 15],
    name="first trace",
    hoverinfo="none"
))

fig.show()
```

### Text Font as an Array - Styling Each Text Element

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lat=[45.5, 43.4, 49.13, 51.1, 53.34, 45.24, 44.64, 48.25, 49.89, 50.45],
    lon=[-73.57, -79.24, -123.06, -114.1, -113.28, -75.43, -63.57, -123.21, -97.13,
         -104.6],
    marker={
        "color": ["MidnightBlue", "IndianRed", "MediumPurple", "Orange", "Crimson",
                  "LightSeaGreen", "RoyalBlue", "LightSalmon", "DarkOrange", "MediumSlateBlue"],
        "line": {
            "width": 1
        },
        "size": 10
    },
    mode="markers+text",
    name="",
    text=["Montreal", "Toronto", "Vancouver", "Calgary", "Edmonton", "Ottawa",
          "Halifax",
          "Victoria", "Winnepeg", "Regina"],
    textfont={
        "color": ["MidnightBlue", "IndianRed", "MediumPurple", "Gold", "Crimson",
                  "LightSeaGreen",
                  "RoyalBlue", "LightSalmon", "DarkOrange", "MediumSlateBlue"],
        "family": ["Arial, sans-serif", "Balto, sans-serif", "Courier New, monospace",
                   "Droid Sans, sans-serif", "Droid Serif, serif",
                   "Droid Sans Mono, sans-serif",
                   "Gravitas One, cursive", "Old Standard TT, serif",
                   "Open Sans, sans-serif",
                   "PT Sans Narrow, sans-serif", "Raleway, sans-serif",
                   "Times New Roman, Times, serif"],
        "size": [22, 21, 20, 19, 18, 17, 16, 15, 14, 13]
    },
    textposition=["top center", "middle left", "top center", "bottom center",
                  "top right",
                  "middle left", "bottom right", "bottom left", "top right",
                  "top right"]
))

fig.update_layout(
    title_text="Canadian cities",
    geo=go.layout.Geo(
        lataxis=dict(range=[40, 70]),
        lonaxis=dict(range=[-130, -55]),
        scope="north america"
    )
)

fig.show()
```

### Adding Annotations with xref and yref as Paper

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[1, 2, 3],
    name="y",
))

fig.update_layout(
    annotations=[
        go.layout.Annotation(
            x=0.5,
            y=-0.15,
            showarrow=False,
            text="Custom x-axis title",
            xref="paper",
            yref="paper"
        ),
        go.layout.Annotation(
            x=-0.07,
            y=0.5,
            showarrow=False,
            text="Custom y-axis title",
            textangle=-90,
            xref="paper",
            yref="paper"
        )
    ],
    autosize=True,
    margin=dict(
        b=100
    ),
    title_text="Plot Title",
    xaxis=dict(
        autorange=False,
        range=[-0.05674507980728292, -0.0527310420933204],
        type="linear"
    ),
    yaxis=dict(
        autorange=False,
        range=[1.2876210047544652, 1.2977732997811402],
        type="linear"
    ),
    height=550,
    width=1137
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#layout-annotations for more information and chart attribute options!
