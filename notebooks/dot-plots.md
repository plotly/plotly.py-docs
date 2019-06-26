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
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to make dot plots in Python with Plotly.
    display_as: basic
    has_thumbnail: true
    ipynb: ~notebook_demo/2
    language: python
    layout: user-guide
    name: Dot Plots
    order: 3.1
    page_type: u-guide
    permalink: python/dot-plots/
    thumbnail: thumbnail/dot-plot.jpg
    title: Python Dot Plots | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Plotly's python package is updated frequently. Run `pip install plotly --upgrade` to use the latest version.

```python
import plotly
plotly.__version__
```

#### Basic Dot Plot
Dot plots show changes between two points in time or between two conditions.

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = {"x": [72, 67, 73, 80, 76, 79, 84, 78, 86, 93, 94, 90, 92, 96, 94, 112],
          "y": ["Brown", "NYU", "Notre Dame", "Cornell", "Tufts", "Yale",
                "Dartmouth", "Chicago", "Columbia", "Duke", "Georgetown",
                "Princeton", "U.Penn", "Stanford", "MIT", "Harvard"],
          "marker": {"color": "pink", "size": 12},
          "mode": "markers",
          "name": "Women",
          "type": "scatter"
}

trace2 = {"x": [92, 94, 100, 107, 112, 114, 114, 118, 119, 124, 131, 137, 141, 151, 152, 165],
          "y": ["Brown", "NYU", "Notre Dame", "Cornell", "Tufts", "Yale",
                "Dartmouth", "Chicago", "Columbia", "Duke", "Georgetown",
                "Princeton", "U.Penn", "Stanford", "MIT", "Harvard"],
          "marker": {"color": "blue", "size": 12},
          "mode": "markers",
          "name": "Men",
          "type": "scatter",
}

data = [trace1, trace2]
layout = {"title": "Gender Earnings Disparity",
          "xaxis": {"title": "Annual Salary (in thousands)", },
          "yaxis": {"title": "School"}}

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filenmae='basic_dot-plot')
```

#### Styled Categorical Dot Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

country = ['Switzerland (2011)', 'Chile (2013)', 'Japan (2014)',
           'United States (2012)', 'Slovenia (2014)', 'Canada (2011)',
           'Poland (2010)', 'Estonia (2015)', 'Luxembourg (2013)', 'Portugal (2011)']
voting_pop = [40, 45.7, 52, 53.6, 54.1, 54.2, 54.5, 54.7, 55.1, 56.6]
reg_voters = [49.1, 42, 52.7, 84.3, 51.7, 61.1, 55.3, 64.2, 91.1, 58.9]

trace0 = go.Scatter(
    x=voting_pop,
    y=country,
    mode='markers',
    name='Percent of estimated voting age population',
    marker=dict(
        color='rgba(156, 165, 196, 0.95)',
        line=dict(
            color='rgba(156, 165, 196, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=16,
    )
)
trace1 = go.Scatter(
    x=reg_voters,
    y=country,
    mode='markers',
    name='Percent of estimated registered voters',
    marker=dict(
        color='rgba(204, 204, 204, 0.95)',
        line=dict(
            color='rgba(217, 217, 217, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=16,
    )
)

data = [trace0, trace1]
layout = go.Layout(
    title="Votes cast for ten lowest voting age population in OECD countries",
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(102, 102, 102)',
        titlefont=dict(
            color='rgb(204, 204, 204)'
        ),
        tickfont=dict(
            color='rgb(102, 102, 102)',
        ),
        showticklabels=True,
        dtick=10,
        ticks='outside',
        tickcolor='rgb(102, 102, 102)',
    ),
    margin=dict(
        l=140,
        r=40,
        b=50,
        t=80
    ),
    legend=dict(
        font=dict(
            size=10,
        ),
        yanchor='middle',
        xanchor='right',
    ),
    width=800,
    height=600,
    paper_bgcolor='rgb(254, 247, 234)',
    plot_bgcolor='rgb(254, 247, 234)',
    hovermode='closest',
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='lowest-oecd-votes-cast')
```

### Reference


See https://plot.ly/python/reference/#scatter for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'dot.ipynb', 'python/dot-plots/', 'Dot Plots',
    'How to make dot plots in Python with Plotly.',
    title = 'Python Dot Plots | plotly',
    has_thumbnail='true', thumbnail='thumbnail/dot-plot.jpg',
    language='python',
    display_as='basic', order=3.1,
    ipynb= '~notebook_demo/2')
```

```python

```
