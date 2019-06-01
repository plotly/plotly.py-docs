---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  plotly:
    description: Installation and Initialization Steps for Using Plotly in Python.
    has_thumbnail: false
    ipynb: ~notebook_demo/123/installation
    language: python
    layout: getstart
    name: Getting Started with Plotly for Python
    page_type: u-guide
    permalink: python/getting-started/
    thumbnail: /images/static-image
    title: Getting Started with Plotly for Python | plotly
---

### Installation


To install Plotly's python package, use the package manager **pip** inside your terminal.<br>
If you don't have **pip** installed on your machine, [click here](https://pip.pypa.io/en/latest/installing.html) for pip's installation instructions.
<br>
<br>
`$ pip install plotly`
<br>or
<br>`$ sudo pip install plotly`
<br>
<br>
Plotly's Python package is [updated frequently](https://github.com/plotly/plotly.py/blob/master/CHANGELOG.md)! To upgrade, run:
<br>
<br>
`$ pip install plotly --upgrade`


### Initialization for Online Plotting
Plotly provides a web-service for hosting graphs! Create a [free account](https://plot.ly/api_signup) to get started. Graphs are saved inside your online Plotly account and you control the privacy. Public hosting is free, for private hosting, check out our [paid plans](https://plot.ly/products/cloud/).
<br>
<br>
After installing the Plotly package, you're ready to fire up python:
<br>
<br>
`$ python`
<br>
<br>
and set your credentials:

```python
import plotly 
plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
```

<!-- #region -->
You'll need to replace **'DemoAccount'** and **'lr1c37zw81'** with *your* Plotly username and [API key](https://plot.ly/settings/api).<br>
Find your API key [here](https://plot.ly/settings/api).
<br>
<br>
The initialization step places a special **.plotly/.credentials** file in your home directory. Your **~/.plotly/.credentials** file should look something like this:
<br>
```
{
    "username": "DemoAccount",
    "stream_ids": ["ylosqsyet5", "h2ct8btk1s", "oxz4fm883b"],
    "api_key": "lr1c37zw81"
}
```
<!-- #endregion -->

### Online Plot Privacy

Plot can be set to three different type of privacies: public, private or secret.
- **public**: Anyone can view this graph. It will appear in your profile and can appear in search engines. You do not need to be logged in to Plotly to view this chart.
- **private**: Only you can view this plot. It will not appear in the Plotly feed, your profile, or search engines. You must be logged in to Plotly to view this graph. You can privately share this graph with other Plotly users in your online Plotly account and they will need to be logged in to view this plot.
- **secret**: Anyone with this secret link can view this chart. It will not appear in the Plotly feed, your profile, or search engines. If it is embedded inside a webpage or an IPython notebook, anybody who is viewing that page will be able to view the graph. You do not need to be logged in to view this plot.

By default all plots are set to **public**.  Users with free account have the permission to keep one private plot. If you need to save private plots, [upgrade to a pro account](https://plot.ly/plans). If you're a [Personal or Professional user](https://plot.ly/settings/subscription/?modal=true&utm_source=api-docs&utm_medium=support-oss) and would like the default setting for your plots to be private, you can edit your Plotly configuration:

```python
import plotly 
plotly.tools.set_config_file(world_readable=False,
                             sharing='private')
```

For more examples on privacy settings please visit [Python privacy documentation](https://plot.ly/python/privacy/)


### Special Instructions for [Chart Studio Enterprise](https://plot.ly/product/enterprise/) Users 


Your API key for account on the public cloud will be different than the API key in Chart Studio Enterprise. Visit https://plotly.your-company.com/settings/api/ to find your Chart Studio Enterprise API key. Remember to replace "your-company.com" with the URL of your Chart Studio Enterprise server.
If your company has a Chart Studio Enterprise server, change the Python API endpoint so that it points to your company's Plotly server instead of Plotly's cloud.
<br>
<br>
In python, enter:

```python
import plotly 
plotly.tools.set_config_file(plotly_domain='https://plotly.your-company.com',
                             plotly_streaming_domain='https://stream-plotly.your-company.com')
```

Make sure to replace **"your-company.com"** with the URL of *your* Chart Studio Enterprise server.


Additionally, you can set your configuration so that you generate **private plots by default**. For more information on privacy settings see: https://plot.ly/python/privacy/<br>
<br>
In python, enter:

```python
import plotly 
plotly.tools.set_config_file(plotly_domain='https://plotly.your-company.com',
                             plotly_streaming_domain='https://stream-plotly.your-company.com', 
                             world_readable=False,
                             sharing='private')
```

### Plotly Using virtualenv
Python's `virtualenv` allows us create multiple working Python environments which can each use different versions of packages. We can use `virtualenv` from the command line to create an environment using plotly.py version 3.3.0 and a separate one using plotly.py version 2.7.0. See [the virtualenv documentation](https://virtualenv.pypa.io/en/stable) for more info.

**Install virtualenv globally**
<br>`$ sudo pip install virtualenv`
 
**Create your virtualenvs**
<br>`$ mkdir ~/.virtualenvs`
<br>`$ cd ~/.virtualenvs`
<br>`$ python -m venv plotly2.7`
<br>`$ python -m venv plotly3.3`

**Activate the virtualenv.**
You will see the name of your virtualenv in parenthesis next to the input promt.
<br>`$ source ~/.virtualenvs/plotly2.7/bin/activate`
<br>`(plotly2.7) $`

**Install plotly locally to virtualenv** (note that we don't use sudo).
<br>`(plotly2.7) $ pip install plotly==2.7`

**Deactivate to exit**
<br>
`(plotly2.7) $ deactivate`
<br>`$`


### Jupyter Setup
**Install Jupyter into a virtualenv**
<br>`$ source ~/.virtualenvs/plotly3.3/bin/activate`
<br>`(plotly3.3) $ pip install notebook`

**Start the Jupyter kernel from a virtualenv**
<br>`(plotly3.3) $ jupyter notebook`




### Start Plotting Online
When plotting online, the plot and data will be saved to your cloud account. There are two methods for plotting online: `py.plot()` and `py.iplot()`. Both options create a unique url for the plot and save it in your Plotly account.
- Use `py.plot()` to return the unique url and optionally open the url.
- Use `py.iplot()` when working in a Jupyter Notebook to display the plot in the notebook.

Copy and paste one of the following examples to create your first hosted Plotly graph using the Plotly Python library:

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

py.plot(data, filename = 'basic-line', auto_open=True)
```

Checkout the docstrings for more information:

```python
import plotly.plotly as py
help(py.plot)
```

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

py.iplot(data, filename = 'basic-line')
```

See more examples in our [IPython notebook documentation](https://plot.ly/ipython-notebooks/) or check out the `py.iplot()` docstring for more information.

```python
import plotly.plotly as py
help(py.iplot)
```

You can also create plotly graphs with **matplotlib** syntax. Learn more in our [matplotlib documentation](https://plot.ly/matplotlib/).


### Initialization for Offline Plotting
Plotly Offline allows you to create graphs offline and save them locally. There are also two methods for plotting offline: `plotly.offline.plot()` and `plotly.offline.iplot()`. 
- Use `plotly.offline.plot()` to create and standalone HTML that is saved locally and opened inside your web browser.
- Use `plotly.offline.iplot()` when working offline in a Jupyter Notebook to display the plot in the notebook.

Check your Plotly version, <b>version 1.9.4+ is needed for offline plotting:</b>

```python
import plotly
plotly.__version__
```

Copy and paste one of the following examples to create your first offline Plotly graph using the Plotly Python library:

```python
import plotly
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": go.Layout(title="hello world")
}, auto_open=True)
```

Learn more by calling `help()`:

```python
import plotly
help(plotly.offline.plot)
```

When using `plotly.offline.iplot` to plot offline in Jupyter Notebooks, there is an additional initialization step of running: `plotly.offline.init_notebook_mode()` at the start of each notebook session. <br>See the example below:

```python
import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

plotly.offline.iplot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": go.Layout(title="hello world")
})
```

```python
import plotly
help(plotly.offline.iplot)
```

For more examples on plotting offline with Plotly in python please visit our [offline documentation](https://plot.ly/python/offline/).


### Using Plotly with Pandas

To use Plotly with Pandas first `$ pip install pandas` and then import pandas in your code like in the example below.

```python
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

fig = {
    'data': [
          {
          'x': df.gdpPercap, 
            'y': df.lifeExp, 
            'text': df.country, 
            'mode': 'markers', 
            'name': '2007'},
    ],
    'layout': {
        'xaxis': {'title': 'GDP per Capita', 'type': 'log'},
        'yaxis': {'title': "Life Expectancy"}
    }
}

py.iplot(fig, filename='pandas-multiple-scatter')
```

### [MORE EXAMPLES](https://plot.ly/python/)
Check out more examples and tutorials for using Plotly in python [here](https://plot.ly/python)!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'getting-started.ipynb', 'python/getting-started/', 'Getting Started Plotly for Python',
    'Installation and Initialization Steps for Using Plotly in Python.',
    title = 'Getting Started with Plotly for Python | plotly',
    name = 'Getting Started with Plotly for Python',
    language='python', layout='getstart', has_thumbnail='false',
    ipynb= '~notebook_demo/123/installation', uses_plotly_offline=True)
```

```python

```