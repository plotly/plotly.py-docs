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
    description: How to make bubble charts in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/1/new-to-plotly-plotlys-python-library-i
    language: python
    layout: user-guide
    name: Bubble Charts
    order: 3
    page_type: u-guide
    permalink: python/bubble-charts/
    redirect_from: python/bubble-charts-tutorial/
    thumbnail: thumbnail/bubble.jpg
    title: Bubble Charts | plotly
---

### Simple Bubble Chart

```python
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4], y=[10, 11, 12, 13],
    mode='markers',
    marker_size=[40, 60, 80, 100]
)

fig = go.Figure(data=[trace0])
fig.show()
```

### Setting Marker Size and Color

```python
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4], y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        opacity=[1, 0.8, 0.6, 0.4],
        size=[40, 60, 80, 100],
    )
)

fig = go.Figure(data = [trace0])
fig.show()
```

### Scaling the Size of Bubble Charts
To scale the bubble size, use the attribute `sizeref`. We recommend using the following formula to calculate a `sizeref` value:<br>
`sizeref = 2. * max(array of size values) / (desired maximum marker size ** 2)`<br>
Note that setting 'sizeref' to a value greater than 1, decreases the rendered marker sizes, while setting 'sizeref' to less than 1, increases the rendered marker sizes. See https://plot.ly/python/reference/#scatter-marker-sizeref for more information.
Additionally, we recommend setting the sizemode attribute: https://plot.ly/python/reference/#scatter-marker-sizemode to area.

```python
import plotly.graph_objs as go

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[11, 12, 10, 11, 12, 11, 12, 13, 12, 11],
    mode='markers',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4
    )
)

fig = go.Figure(data=[trace0])
fig.show()
```

### Hover Text with Bubble Charts

```python
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4], y=[10, 11, 12, 13],
    text=['A<br>size: 40', 'B<br>size: 60', 'C<br>size: 80', 'D<br>size: 100'],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        size=[40, 60, 80, 100],
    )
)

fig = go.Figure(data=[trace0])
fig.show()
```

### Bubble Charts with Colorscale

```python
import plotly.graph_objs as go

trace = go.Scatter(
    x=[1, 3.2, 5.4, 7.6, 9.8, 12.5],
    y=[1, 3.2, 5.4, 7.6, 9.8, 12.5],
    mode='markers',
    marker=dict(
        color=[120, 125, 130, 135, 140, 145],
        size=[15, 30, 55, 70, 90, 110],
        showscale=True
        )
)
fig = go.Figure(data=[trace])
fig.show()
```

### Categorical Bubble Charts

```python
import plotly.graph_objs as go
import pandas as pd
import math

data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")
df_2007 = data[data['year']==2007]
df_2007 = df_2007.sort_values(['continent', 'country'])
slope = 2.666051223553066e-05
hover_text = []
bubble_size = []

for index, row in df_2007.iterrows():
    hover_text.append(('Country: {country}<br>'+
                      'Life Expectancy: {lifeExp}<br>'+
                      'GDP per capita: {gdp}<br>'+
                      'Population: {pop}<br>'+
                      'Year: {year}').format(country=row['country'],
                                            lifeExp=row['lifeExp'],
                                            gdp=row['gdpPercap'],
                                            pop=row['pop'],
                                            year=row['year']))
    bubble_size.append(math.sqrt(row['pop']*slope))

df_2007['text'] = hover_text
df_2007['size'] = bubble_size
sizeref = 2.*max(df_2007['size'])/(100**2)

trace0 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Africa'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Africa'],
    mode='markers',
    name='Africa',
    text=df_2007['text'][df_2007['continent'] == 'Africa'],
    marker=dict(
        symbol='circle',
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Africa'],
        line_width=2
    )
)
trace1 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Americas'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Americas'],
    mode='markers',
    name='Americas',
    text=df_2007['text'][df_2007['continent'] == 'Americas'],
    marker=dict(
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Americas'],
        line_width=2
    )
)
trace2 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Asia'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Asia'],
    mode='markers',
    name='Asia',
    text=df_2007['text'][df_2007['continent'] == 'Asia'],
    marker=dict(
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Asia'],
        line_width=2
    )
)
trace3 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Europe'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Europe'],
    mode='markers',
    name='Europe',
    text=df_2007['text'][df_2007['continent'] == 'Europe'],
    marker=dict(
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Europe'],
        line_width=2
    )
)
trace4 = go.Scatter(
    x=df_2007['gdpPercap'][df_2007['continent'] == 'Oceania'],
    y=df_2007['lifeExp'][df_2007['continent'] == 'Oceania'],
    mode='markers',
    name='Oceania',
    text=df_2007['text'][df_2007['continent'] == 'Oceania'],
    marker=dict(
        sizemode='area',
        sizeref=sizeref,
        size=df_2007['size'][df_2007['continent'] == 'Oceania'],
        line_width=2,
    )
)

layout = go.Layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    xaxis=dict(
        title='GDP per capita (2000 dollars)',
        gridcolor='rgb(255, 255, 255)',
        range=[2.003297660701705, 5.191505530708712],
        type='log',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Life Expectancy (years)',
        gridcolor='rgb(255, 255, 255)',
        range=[36.12621671352166, 91.72921793264332],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

fig = go.Figure(data=[trace0, trace1, trace2, trace3, trace4], layout=layout)
fig.show()
```

### Reference
See https://plot.ly/python/reference/#scatter for more information and chart attribute options!

