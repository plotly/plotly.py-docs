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
    description: How to set the privacy settings of plotly graphs in python. Three
      examples of different privacy options&#58; public, private and secret.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/97
    language: python
    layout: user-guide
    name: Privacy
    order: 2
    permalink: python/privacy/
    thumbnail: thumbnail/privacy.jpg
    title: Privacy | plotly
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

#### Default Privacy
By default, `plotly.iplot()` and `plotly.plot()` create public graphs (which are free to create). With a [plotly subscription](https://plot.ly/plans) you can easily make charts private or secret via the sharing argument.


#### Public Graphs

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]
    )
]

py.iplot(data, filename='privacy-public', sharing='public')
```

Below is the URL of this public plot.  Anyone can view public plots even if they are not logged into Plotly.  Go ahead and try it out:

```python
py.plot(data, filename='privacy-public', sharing='public')
```

### Private Graphs

```python
py.iplot(data, filename='privacy-private', sharing='private')
```

Below is the URL of the private plot above. Only the owner can view the private plot. You won't be able to view this plot, try it out:

```python
py.plot(data, filename='privacy-private', sharing='private')
```

### Secret Graphs

```python
py.iplot(data, filename='privacy-secret', sharing='secret')
```

Below is the URL of this secret plot. Anyone with the secret link can view this chart. However, it will not appear in the Plotly feed, your profile, or search engines. Go ahead and try it out:

```python
py.plot(data, filename='privacy-secret', sharing='secret')
```

### Make All Future Plots Private
To make all future plots private, you can update your configuration file to create private plots by default:

```python
import plotly
plotly.tools.set_config_file(world_readable=False, sharing='private')
```

### Make All Existing Plots Private
This example uses [Plotly's REST API](https://api.plot.ly/v2/)

```python
import json
import requests
from requests.auth import HTTPBasicAuth
```

Define variables, including YOUR [USERNAME and API KEY](https://plot.ly/settings/api)

```python
username = 'private_plotly' # Replace with YOUR USERNAME
api_key = 'k0yy0ztssk' # Replace with YOUR API KEY

auth = HTTPBasicAuth(username, api_key)
headers = {'Plotly-Client-Platform': 'python'}

page_size = 500
```

Collect filenames of <b>ALL</b> of your plots and <br>update `world_readable` of each plot with a PATCH request

```python
def get_pages(username, page_size):
    url = 'https://api.plot.ly/v2/folders/all?user='+username+'&filetype=plot&page_size='+str(page_size)
    response = requests.get(url, auth=auth, headers=headers)
    if response.status_code != 200:
        return
    page = json.loads(response.content.decode('utf-8'))
    yield page
    while True:
        resource = page['children']['next']
        if not resource:
            break
        response = requests.get(resource, auth=auth, headers=headers)
        if response.status_code != 200:
            break
        page = json.loads(response.content.decode('utf-8'))
        yield page

def make_all_plots_private(username, page_size=500):
    for page in get_pages(username, page_size):
        for x in range(0, len(page['children']['results'])):
            fid = page['children']['results'][x]['fid']
            requests.patch('https://api.plot.ly/v2/files/'+fid, {"world_readable": False}, auth=auth, headers=headers)
    print('ALL of your plots are now private - visit: https://plot.ly/organize/home to view your private plots!')

make_all_plots_private(username)
```

### Reference

```python
help(py.plot)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'privacy.ipynb', 'python/privacy/', 'Privacy',
    'How to set the privacy settings of plotly graphs in python. Three examples of different privacy options: public, private and secret.',
    title = 'Privacy | plotly',
    name = 'Privacy', language='python',
    has_thumbnail= True, thumbnail= 'thumbnail/privacy.jpg',
    display_as='file_settings', order=2,
    ipynb= '~notebook_demo/97')
```

```python

```
