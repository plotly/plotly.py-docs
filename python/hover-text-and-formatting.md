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
    description: How to use hover text and formatting in Python with Plotly.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/198
    language: python
    layout: base
    name: Hover Text and Formatting
    order: 30.5
    permalink: python/hover-text-and-formatting/
    thumbnail: thumbnail/hover-text.png
    title: Hover Text and Formatting | Plotly
    v4upgrade: true
---

#### Hover text with plotly express
Many plotly express functions support configurable hover text. The `hover_data` argument accepts a list of column names to be added to the hover tooltip. The `hover_name` property controls which column is displayed in bold as the tooltip title.

Here is an example that creates a scatter plot using plotly express with custom hover data and a custom hover name.

```python
import plotly.express as px

gapminder_2007 = px.data.gapminder().query("year==2007")

fig = px.scatter(gapminder_2007, x="gdpPercap", y="lifeExp", log_x=True,
                 hover_name="country", hover_data=["continent"])

fig.show()
```

#### Add Hover Text

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2, 1, 6, 4, 4],
    hovertext=["Text A", "Text B", "Text C", "Text D", "Text E"],
    hoverinfo="text",
    marker=dict(
        color="green"
    ),
    showlegend=False
))

fig.show()
```

#### Format Hover Text

```python
import plotly.graph_objects as go


fig = go.Figure(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2.02825, 1.63728, 6.83839, 4.8485, 4.73463],
    hoverinfo="y",
    marker=dict(
        color="green"
    ),
    showlegend=False
))

fig.update_layout(
    title_text=("Set hover text formatting<br>" +
                "<a href= https://github.com/d3/d3-time-format/blob/master/README.md#locale_format>" +
                "https://github.com/d3/d3-time-format/blob/master/README.md#locale_format</a>"),
    title_font=dict(
        size=10
    ),
)

fig.update_xaxes(zeroline=False)
fig.update_yaxes(hoverformat=".2f")

fig.show()
```

### Customize tooltip text with a hovertemplate

To customize the tooltip on your graph you can use [hovertemplate](https://plot.ly/python/reference/#pie-hovertemplate), which is a template string used for rendering the information that appear on hoverbox. 
This template string can include `variables` in %{variable} format, `numbers` in [d3-format's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_forma), and `date` in [d3-time-fomrat's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Time-Formatting.md#format).
Hovertemplate customize the tooltip text vs. [texttemplate](https://plot.ly/python/reference/#pie-texttemplate) which customizes the text that appears on your chart. 

```python
import plotly.graph_objects as go

fig = go.Figure(go.Pie(
    name = "", 
    values = [2, 5, 3, 2.5],
    labels = ["R", "Python", "Java Script", "Matlab"],
    text = ["textA", "TextB", "TextC", "TextD"],
    hovertemplate = "%{label}: <br>Popularity: %{percent} </br> %{text}"
))

fig.show()
```

### Format Hover Template

```python
import plotly.io as pio
import plotly.express as px

df = px.data.gapminder()
A = []
B = []

for i in range(5):
    A = {'target': df['continent'][[i]].unique()}
    B.append(A)

data = [{
    'type': 'scatter',
    'mode': 'markers',
    'x': df['lifeExp'],
    'y': df['gdpPercap'],
    'text': df['continent'],
    'hovertemplate':
    "<b>%{text}</b><br><br>" +
    "GDP per Capita: %{y:$,.0f}<br>" +
    "Life Expectation: %{x:.0%}<br>" +
    "Population: %{marker.size:,}" +
    "<extra></extra>",
    'marker': {
      'size': df['pop'],
      'sizemode': 'area',
      'sizeref': 200000
  },
    'transforms': [{
      'type': 'filter',
      'target': df['year'],
      'orientation': '=',
      'value': 2002
  },{
      'type': 'groupby',
      'groups': df['continent'],
      'styles': B
  }]
}]

layout = {'yaxis': {'type': 'log'}}

pio.show({'data': data, 'layout': layout}, validate=False)
```

### Set Hover Template in Mapbox
```python
import plotly.graph_objects as go

token = open(".mapbox_token").read() # you need your own token

fig = go.Figure(go.Scattermapbox(
    name = "",
    mode = "markers+text+lines",
    lon = [-75, -80, -50], 
    lat = [45, 20, -20], 
    marker = {'size': 20, 'symbol': ["bus", "harbor", "airport"]},
    hovertemplate =
    "<b>%{marker.symbol} </b><br><br>" +
    "longitude: %{lon}<br>" +
    "latitude: %{lat}<br>" ))

fig.update_layout(
    mapbox = {
        'accesstoken': token,
        'style': "outdoors", 'zoom': 1},
    showlegend = False)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!