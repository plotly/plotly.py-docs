---
jupyter:
  jupytext:
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
    description: How to make scatterplot matrices or sploms natively in Python with
      Plotly.
    display_as: statistical
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Scatterplot Matrix
    order: 10.2
    page_type: u-guide
    permalink: python/splom/
    redirect_from: python/scatterplot-matrix/
    thumbnail: thumbnail/splom_image.jpg
    title: Python Scatterplot Matrix | Plotly
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

<!-- #region -->
#### Splom trace
A scaterplot matrix is a matrix associated to n numerical arrays (data variables),  $X_1,X_2,…,X_n$ , of the same length. The cell (i,j) of such a matrix displays the scater plot of the variable  Xi  versus  Xj ,

The Plotly splom trace implementation for the scaterplot matrix does not require to set  $x=Xi$ , and  $y=Xj$, for each scatter plot. All arrays, $X_1,X_2,…,X_n$ , are passed once, through a list of dicts called dimensions, i.e. each array/variable represents a dimension.

A trace of type `splom` is defined as follows:

```
trace=go.Splom(dimensions=[dict(label='string-1',
                                values=X1),
                           dict(label='string-2',
                                values=X2),
                           .
                           .
                           .
                           dict(label='string-n',
                                values=Xn)],
                           text=text,
                           marker=dict(...)
               )
```

The label in each dimension is assigned to the axes titles of the corresponding matrix cell.

text is either a unique string assigned to all points displayed by splom or a list of strings of the same length as the dimensions,  $X_i$. The `text[k]` is the tooltip for the $k^{th}$  point in each cell.

marker sets the markers attributes in all scatter plots.
<!-- #endregion -->

#### Splom of the Iris data set

```python
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.tools as tls
import plotly.figure_factory as ff

import copy
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

df_table = ff.create_table(df.head())
py.iplot(df_table, filename='iris-data-head')
```

The Iris dataset contains four data variables,  sepal length, sepal width, petal length petal width, for 150 iris flowers. The flowers are labeled as `Iris-setosa`, `Iris-versicolor`, `Iris-virginica`.

Extract out the flower class:

```python
classes=np.unique(df['class'].values).tolist()
classes
```

Encode the three classes by 0, 1, 2:

```python
class_code={classes[k]: k for k in range(3)}
class_code
```

The splom associated to the four data variables is intended to illustrate the patterns of the relationship between pairs of variables for each class.

The points displayed in splom are colored according to their class:

```python
color_vals=[class_code[cl] for cl in df['class']]
```

Define a discrete colorscale with three colors corresponding to the three flower classes:

```python
pl_colorscale=[[0.0, '#19d3f3'],
               [0.333, '#19d3f3'],
               [0.333, '#e763fa'],
               [0.666, '#e763fa'],
               [0.666, '#636efa'],
               [1, '#636efa']]
```

On hover over a particular point in a splom cell is displayed the corresponding iris class:

```python
text=[df.loc[ k, 'class'] for k in range(len(df))]
```

```python
trace1 = go.Splom(dimensions=[dict(label='sepal length',
                                 values=df['sepal length']),
                            dict(label='sepal width',
                                 values=df['sepal width']),
                            dict(label='petal length',
                                 values=df['petal length']),
                            dict(label='petal width',
                                 values=df['petal width'])],
                text=text,
                #default axes name assignment :
                #xaxes= ['x1','x2',  'x3'],
                #yaxes=  ['y1', 'y2', 'y3'], 
                marker=dict(color=color_vals,
                            size=7,
                            colorscale=pl_colorscale,
                            showscale=False,
                            line=dict(width=0.5,
                                      color='rgb(230,230,230)'))
                )
```

```python
axis = dict(showline=True,
          zeroline=False,
          gridcolor='#fff',
          ticklen=4)

layout = go.Layout(
    title='Iris Data set',
    dragmode='select',
    width=600,
    height=600,
    autosize=False,
    hovermode='closest',
    plot_bgcolor='rgba(240,240,240, 0.95)',
    xaxis1=dict(axis),
    xaxis2=dict(axis),
    xaxis3=dict(axis),
    xaxis4=dict(axis),
    yaxis1=dict(axis),
    yaxis2=dict(axis),
    yaxis3=dict(axis),
    yaxis4=dict(axis)
)

fig1 = dict(data=[trace1], layout=layout)
py.iplot(fig1, filename='splom-iris1')
```

The scatter plots on the principal diagonal can be removed by setting diagonal=dict(visible=False):

```python
trace2 = copy.copy(trace1)
trace2['diagonal'].update(visible=False)
fig2 = dict(data=[trace2], layout=layout)
py.iplot(fig2, filename='splom-invisible-diagonal')
```

To plot only the lower/upper half of the splom we switch the default showlowerhalf=True/showupperhalf=True to False:

```python
trace3 = copy.deepcopy(trace1)
trace3['showupperhalf']=False

fig3 = dict(data=[trace3], layout=layout)
py.iplot(fig3, filename='splom-showupperhalf')
```

Each dict in the list dimensions has a key, visible, set by default on True. We can choose to remove a variable from splom, by setting `visible=False` in its corresponding dimension. In this case the default grid associated to the scatterplot matrix keeps its number of cells, but the cells in the row and column corresponding to the visible false dimension are empty:

```python
trace4 = copy.deepcopy(trace1)
trace4['dimensions'][2].update(visible=False)
fig4 = dict(data=[trace4], layout=layout)
py.iplot(fig4, filename='splom-invisible-custom-dimensions')
```

#### Splom for the diabetes dataset

Diabetes dataset is downloaded from [kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database/data). It is used to predict the onset of diabetes based on 8 diagnostic measures.

```python
dfd = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv')

df_table = ff.create_table(dfd.head())
py.iplot(df_table, filename='diabetes-head')
```

The diabetes file contains the diagnostic measures for 768 patients, that are labeled as non-diabetic (Outcome=0), respectively diabetic (Outcome=1). The splom associated to the 8 variables can illustrate the strength of the relationship between pairs of measures for diabetic/nondiabetic patients.

```python
textd = ['non-diabetic' if cl==0 else 'diabetic' for cl in dfd['Outcome']]
color_vals = [0  if cl==0 else 1 for cl in dfd['Outcome']]
```

We define again a discrete colorscale with two colors: blue for non-diabetics and red for diabetics:

```python
pl_colorscaled = [[0., '#119dff'],
                 [0.5, '#119dff'],
                 [0.5, '#ef553b'],
                 [1, '#ef553b']]
```

```python
traced = go.Splom(dimensions=[dict(label='Pregnancies', values=dfd['Pregnancies']),
                              dict(label='Glucose', values=dfd['Glucose']),
                              dict(label='BloodPressure', values=dfd['BloodPressure']),
                              dict(label='SkinThickness', values=dfd['SkinThickness']),
                              dict(label='Insulin', values=dfd['Insulin']),
                              dict(label='BMI', values=dfd['BMI']),
                              dict(label='DiabPedigreeFun', values=dfd['DiabetesPedigreeFunction']),
                              dict(label='Age', values=dfd['Age'])],
                  marker=dict(color=color_vals,
                              size=5,
                              colorscale=pl_colorscaled,
                              line=dict(width=0.5,
                                        color='rgb(230,230,230)') ),
                  text=textd,
                  diagonal=dict(visible=False))
```

```python
axisd = dict(showline=False,
           zeroline=False,
           gridcolor='#fff',
           ticklen=4,
           titlefont=dict(size=13))
title = "Scatterplot Matrix (SPLOM) for Diabetes Dataset<br>Data source:"+\
        " <a href='https://www.kaggle.com/uciml/pima-indians-diabetes-database/data'>[1]</a>"

layout = go.Layout(title=title,
                   dragmode='select',
                   width=1000,
                   height=1000,
                   autosize=False,
                   hovermode='closest',
                   plot_bgcolor='rgba(240,240,240, 0.95)',
                   xaxis1=dict(axisd),
                   xaxis2=dict(axisd),
                   xaxis3=dict(axisd),
                   xaxis4=dict(axisd),
                   xaxis5=dict(axisd),
                   xaxis6=dict(axisd),
                   xaxis7=dict(axisd),
                   xaxis8=dict(axisd),
                   yaxis1=dict(axisd),
                   yaxis2=dict(axisd),
                   yaxis3=dict(axisd),
                   yaxis4=dict(axisd),
                   yaxis5=dict(axisd),
                   yaxis6=dict(axisd),
                   yaxis7=dict(axisd),
                   yaxis8=dict(axisd))

fig = dict(data=[traced], layout=layout)
py.iplot(fig, filename='large')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'splom.ipynb', 'python/splom/', 'Scatterplot Matrix',
    'How to make scatterplot matrices or sploms natively in Python with Plotly.',
    title = 'Python Scatterplot Matrix | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/splom_image.jpg',
    redirect_from ='python/scatterplot-matrix/',
    language='python',
    display_as='statistical', order=10.2,
    uses_plotly_offline=False)
```

```python

```