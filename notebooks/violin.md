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
    description: How to make violin plots in Python with Plotly.
    display_as: statistical
    has_thumbnail: true
    ipynb: ~notebook_demo/201
    language: python
    layout: user-guide
    name: Violin Plots
    order: 12
    page_type: u-guide
    permalink: python/violin/
    thumbnail: thumbnail/violin.jpg
    title: Violin Plots | Plotly
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

#### Basic Violin Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig = {
    "data": [{
        "type": 'violin',
        "y": df['total_bill'],
        "box": {
            "visible": True
        },
        "line": {
            "color": 'black'
        },
        "meanline": {
            "visible": True
        },
        "fillcolor": '#8dd3c7',
        "opacity": 0.6,
        "x0": 'Total Bill'
    }],
    "layout" : {
        "title": "",
        "yaxis": {
            "zeroline": False,
        }
    }
}

py.iplot(fig, filename = 'violin/basic', validate = False)
```

#### Multiple Traces

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

data = []
for i in range(0,len(pd.unique(df['day']))):
    trace = {
            "type": 'violin',
            "x": df['day'][df['day'] == pd.unique(df['day'])[i]],
            "y": df['total_bill'][df['day'] == pd.unique(df['day'])[i]],
            "name": pd.unique(df['day'])[i],
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            }
        }
    data.append(trace)


fig = {
    "data": data,
    "layout" : {
        "title": "",
        "yaxis": {
            "zeroline": False,
        }
    }
}


py.iplot(fig, filename='violin/multiple', validate = False)
```

#### Grouped Violin Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig = {
    "data": [
        {
            "type": 'violin',
            "x": df['day'] [ df['sex'] == 'Male' ],
            "y": df['total_bill'] [ df['sex'] == 'Male' ],
            "legendgroup": 'M',
            "scalegroup": 'M',
            "name": 'M',
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            },
            "line": {
                "color": 'blue'
            }
        },
        {
            "type": 'violin',
            "x": df['day'] [ df['sex'] == 'Female' ],
            "y": df['total_bill'] [ df['sex'] == 'Female' ],
            "legendgroup": 'F',
            "scalegroup": 'F',
            "name": 'F',
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            },
            "line": {
                "color": 'pink'
            }
        }
    ],
    "layout" : {
        "yaxis": {
            "zeroline": False,
        },
        "violinmode": "group"
    }
}


py.iplot(fig, filename = 'violin/grouped', validate = False)
```

#### Split Violin Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig = {
    "data": [
        {
            "type": 'violin',
            "x": df['day'] [ df['smoker'] == 'Yes' ],
            "y": df['total_bill'] [ df['smoker'] == 'Yes' ],
            "legendgroup": 'Yes',
            "scalegroup": 'Yes',
            "name": 'Yes',
            "side": 'negative',
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            },
            "line": {
                "color": 'blue'
            }
        },
        {
            "type": 'violin',
            "x": df['day'] [ df['smoker'] == 'No' ],
            "y": df['total_bill'] [ df['smoker'] == 'No' ],
            "legendgroup": 'No',
            "scalegroup": 'No',
            "name": 'No',
            "side": 'positive',
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            },
            "line": {
                "color": 'green'
            }
        }
    ],
    "layout" : {
        "yaxis": {
            "zeroline": False,
        },
        "violingap": 0,
        "violinmode": "overlay"
    }
}


py.iplot(fig, filename = 'violin/split', validate = False)
```

#### Advanced Violin Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

pointposMale = [-0.9,-1.1,-0.6,-0.3]
pointposFemale = [0.45,0.55,1,0.4]
showLegend = [True,False,False,False]

data = []
for i in range(0,len(pd.unique(df['day']))):
    male = {
            "type": 'violin',
            "x": df['day'][ (df['sex'] == 'Male') & (df['day'] == pd.unique(df['day'])[i]) ],
            "y": df['total_bill'][ (df['sex'] == 'Male') & (df['day'] == pd.unique(df['day'])[i]) ],
            "legendgroup": 'M',
            "scalegroup": 'M',
            "name": 'M',
            "side": 'negative',
            "box": {
                "visible": True
            },
            "points": 'all',
            "pointpos": pointposMale[i],
            "jitter": 0,
            "scalemode": 'count',
            "meanline": {
                "visible": True
            },
            "line": {
                "color": '#8dd3c7'
            },
            "marker": {
                "line": {
                    "width": 2,
                    "color": '#8dd3c7'
                }
            },
            "span": [
                0
            ],
            "showlegend": showLegend[i]
        }
    data.append(male)
    female = {
            "type": 'violin',
            "x": df['day'] [ (df['sex'] == 'Female') & (df['day'] == pd.unique(df['day'])[i]) ],
            "y": df['total_bill'] [ (df['sex'] == 'Female') & (df['day'] == pd.unique(df['day'])[i]) ],
            "legendgroup": 'F',
            "scalegroup": 'F',
            "name": 'F',
            "side": 'positive',
            "box": {
                "visible": True
            },
            "points": 'all',
            "pointpos": pointposFemale[i],
            "jitter": 0,
            "scalemode": 'count',
            "meanline": {
                "visible": True
            },
            "line": {
                "color": '#bebada'
            },
            "marker": {
                "line": {
                    "width": 2,
                    "color": '#bebada'
                }
            },
            "span": [
                0
            ],
            "showlegend": showLegend[i]
        }
    data.append(female)


fig = {
    "data": data,
    "layout" : {
        "title": "Total bill distribution<br><i>scaled by number of bills per gender",
        "yaxis": {
            "zeroline": False,
        },
        "violingap": 0,
        "violingroupgap": 0,
        "violinmode": "overlay"
    }
}


py.iplot(fig, filename='violin/advanced', validate = False)
```

#### Reference
See https://plot.ly/python/reference/#violin for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'violin.ipynb', 'python/violin/', 'Violin Plots',
    'How to make violin plots in Python with Plotly.',
    title = 'Violin Plots | Plotly',
    has_thumbnail='true',
    thumbnail='thumbnail/violin.jpg',
    language='python',
    display_as='statistical',
    order=12,
    ipynb='~notebook_demo/201')
```

```python

```
