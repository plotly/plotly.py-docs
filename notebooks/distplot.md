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
    description: How to make interactive Distplots in Python with Plotly.
    display_as: statistical
    has_thumbnail: true
    ipynb: ~notebook_demo/23
    language: python
    layout: user-guide
    name: Distplots
    order: 5
    page_type: example_index
    permalink: python/distplot/
    thumbnail: thumbnail/distplot.jpg
    title: Python Distplots | plotly
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Version Check
Note: Distplots are available in version <b>1.11.0+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version
<!-- #endregion -->

```python deletable=true editable=true
import plotly
plotly.__version__
```

<!-- #region {"deletable": true, "editable": true} -->
#### Basic Distplot 
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x = np.random.randn(1000)  
hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data, group_labels)
py.iplot(fig, filename='Basic Distplot')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Plot Multiple Datasets
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

# Add histogram data
x1 = np.random.randn(200)-2  
x2 = np.random.randn(200)  
x3 = np.random.randn(200)+2  
x4 = np.random.randn(200)+4  

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)

# Plot!
py.iplot(fig, filename='Distplot with Multiple Datasets')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Use Multiple Bin Sizes
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

# Add histogram data
x1 = np.random.randn(200)-2  
x2 = np.random.randn(200)  
x3 = np.random.randn(200)+2  
x4 = np.random.randn(200)+4  

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5, 1])

# Plot!
py.iplot(fig, filename='Distplot with Multiple Bin Sizes')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Customize Rug Text, Colors & Title
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x1 = np.random.randn(26)  
x2 = np.random.randn(26) + .5  

hist_data = [x1, x2]

group_labels = ['2014', '2015']

rug_text_one = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j', 
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z'] 

rug_text_two = ['aa', 'bb', 'cc', 'dd', 'ee',
                'ff', 'gg', 'hh', 'ii', 'jj', 
                'kk', 'll', 'mm', 'nn', 'oo',
                'pp', 'qq', 'rr', 'ss', 'tt', 
                'uu', 'vv', 'ww', 'xx', 'yy', 'zz'] 

rug_text = [rug_text_one, rug_text_two]

colors = ['rgb(0, 0, 100)', 'rgb(0, 200, 200)']

# Create distplot with custom bin_size
fig = ff.create_distplot(
    hist_data, group_labels, bin_size=.2,
    rug_text=rug_text, colors=colors)

fig['layout'].update(title='Customized Distplot')

# Plot!
py.iplot(fig, filename='Distplot Colors')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Plot Normal Curve 
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x1 = np.random.randn(200)  
x2 = np.random.randn(200) + 2    
hist_data = [x1, x2]

group_labels = ['Group 1', 'Group 2']

colors = ['#3A4750', '#F64E8B']

# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot(hist_data, group_labels, bin_size=.5, curve_type='normal', colors=colors)

# Add title
fig['layout'].update(title='Distplot with Normal Distribution')

# Plot!
py.iplot(fig, filename='Distplot with Normal Curve')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Plot Only Curve and Rug
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x1 = np.random.randn(200) - 1 
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 1 

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#333F44', '#37AA9C', '#94F3E4']

# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

# Add title
fig['layout'].update(title='Curve and Rug Plot')

# Plot!
py.iplot(fig, filename='Curve and Rug')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Plot Only Hist and Rug
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x1 = np.random.randn(200) - 1 
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 1 

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#835AF1', '#7FA6EE', '#B8F7D4']

# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot(hist_data, group_labels, colors=colors, bin_size=.25, show_curve=False)

# Add title
fig['layout'].update(title='Hist and Rug Plot')

# Plot!
py.iplot(fig, filename='Hist and Rug')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Plot Hist and Rug with Different Bin Sizes
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x1 = np.random.randn(200) - 2 
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2 

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#393E46', '#2BCDC1', '#F66095']
# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot(hist_data, group_labels, colors=colors, 
                         bin_size=[0.3, 0.2, 0.1], show_curve=False)

# Add title
fig['layout'].update(title='Hist and Rug Plot')

# Plot!
py.iplot(fig, filename='Hist and Rug Different Bin Size')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Plot Only Hist and Curve
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

x1 = np.random.randn(200) - 2 
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2 

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#A56CC1', '#A6ACEC', '#63F5EF']

# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                         bin_size=.2, show_rug=False)

# Add title
fig['layout'].update(title='Hist and Curve Plot')

# Plot!
py.iplot(fig, filename='Hist and Curve')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Distplot with Pandas
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df = pd.DataFrame({'2012': np.random.randn(200),
                   '2013': np.random.randn(200)+1})
py.iplot(ff.create_distplot([df[c] for c in df.columns], df.columns, bin_size=.25),
                            filename='distplot with pandas')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference 
<!-- #endregion -->

```python deletable=true editable=true
help(ff.create_distplot)
```

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'distplots.ipynb', 'python/distplot/', 'Python Distplots | plotly',
    'How to make interactive Distplots in Python with Plotly. ',
    title = 'Python Distplots | plotly',
    name = 'Distplots',
    has_thumbnail='true', thumbnail='thumbnail/distplot.jpg', 
    language='python', page_type='example_index', 
    display_as='statistical', order=5,
    ipynb= '~notebook_demo/23')  
```

```python deletable=true editable=true

```