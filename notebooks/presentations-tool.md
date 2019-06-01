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
    description: How to create and publish a spectacle-presentation with the Python
      API.
    display_as: file_settings
    has_thumbnail: true
    language: python
    layout: user-guide
    name: Presentations Tool
    order: 0.6
    page_type: u-guide
    permalink: python/presentations-tool/
    thumbnail: thumbnail/pres_api.jpg
    title: Presentations Tool | plotly
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Note: The presentations API is available in version <b>2.2.1.+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

#### Plotly Presentations
To use Plotly's Presentations API you will write your presentation code in a string of markdown and then pass that through the Presentations API function `pres.Presentation()`. This creates a JSON version of your presentation. To upload the presentation online pass it through `py.presentation_ops.upload()`.

In your string, use `---` on a single line to seperate two slides. To put a title in your slide, put a line that starts with any number of `#`s. Only your first title will be appear in your slide. A title looks like:

`# slide title`

Anything that comes after the title will be put as text in your slide. Check out the example below to see this in action.


#### Current Limitations
`Boldface`, _italics_ and [hypertext](https://www.w3.org/WhatIs.html) are not supported features of the Presentation API.


#### Display in Jupyter
The function below generates HTML code to display the presentation in an iframe directly in Jupyter.

```python
def url_to_iframe(url, text=True):
    html = ''
    # style
    html += '''<head>
    <style>
    div.textbox {
        margin: 30px;
        font-weight: bold;   
    }
    </style>
    </head>'
    '''
    # iframe
    html += '<iframe src=' + url + '.embed#{} width=750 height=400 frameBorder="0"></iframe>'
    if text:
        html += '''<body>
        <div class="textbox">
            <p>Click on the presentation above and use left/right arrow keys to flip through the slides.</p>
        </div>
        </body>
        '''
    return html
```

#### Simple Example

```python
import plotly.plotly as py
import plotly.presentation_objs as pres

filename = 'simple-pres'
markdown_string = """
# slide 1
There is only one slide.

---
# slide 2
Again, another slide on this page.

"""

my_pres = pres.Presentation(markdown_string)
pres_url_0 = py.presentation_ops.upload(my_pres, filename)
```

https://plot.ly/~AdamKulidjian/3700/simple-pres/

```python
import IPython

iframe_0 = url_to_iframe(pres_url_0, True)
IPython.display.HTML(iframe_0)
```

#### Insert Plotly Chart
If you want to insert a Plotly chart into your presentation, all you need to do is write a line in your presentation that takes the form:

`Plotly(url)`

where url is a Plotly url. For example:

`Plotly(https://plot.ly/~AdamKulidjian/3564)`

The Plotly url lines should be written on a separate line after your title line. You can put as many images in your slide as you want, as the API will arrange them on the slide automatically, but it is _highly_ encouraged that you use `4 OR FEWER IMAGES PER SLIDE`. This will produce the cleanest look.

`Useful Tip`: <br>
For Plotly charts it is HIGHLY ADVISED that you use a chart that has `layout['autosize']` set to `True`. If it is `False` the image may be cropped or only partially visible when it appears in the presentation slide.

```python
import plotly.plotly as py
import plotly.presentation_objs as pres

filename = 'pres-with-plotly-chart'
markdown_string = """
# 3D scatterplots
3D Scatterplot are just a collection of balls in a 3D cartesian space each of which have assigned properties like color, size, and more.

---
# simple 3d scatterplot

Plotly(https://plot.ly/~AdamKulidjian/3698)
---
# different colorscales

There are various colorscales and colorschemes to try in Plotly. Check out plotly.colors to find a list of valid and available colorscales.

Plotly(https://plot.ly/~AdamKulidjian/3582)
Plotly(https://plot.ly/~AdamKulidjian/3698)
"""

my_pres = pres.Presentation(markdown_string)
pres_url_1 = py.presentation_ops.upload(my_pres, filename)
```

https://plot.ly/~AdamKulidjian/3710/pres-with-plotly-chart/

```python
import IPython

iframe_1 = url_to_iframe(pres_url_1, True)
IPython.display.HTML(iframe_1)
```

#### Insert Web Images
To insert an image from the web, insert the a `Image(url)` where url is the image url.

```python
import plotly.plotly as py
import plotly.presentation_objs as pres

filename = 'pres-with-images'
markdown_string = """
# Animals of the Wild
---
# The Lion

Panthera leo is one of the big cats in the Felidae family and a member of genus Panthera. It has been listed as Vulnerable on the IUCN Red List since 1996, as populations in African range countries declined by about 43% since the early 1990s. Lion populations are untenable outside designated protected areas. Although the cause of the decline is not fully understood, habitat loss and conflicts with humans are the greatest causes of concern. The West African lion population is listed as Critically Endangered since 2016. The only lion population in Asia survives in and around India's Gir Forest National Park and is listed as Endangered since 1986.

Image(https://i.pinimg.com/736x/da/af/73/daaf73960eb5a21d6bca748195f12052--lion-photography-lion-kings.jpg)
---
# The Giraffe

The giraffe is a genus of African even-toed ungulate mammals, the tallest living terrestrial animals and the largest ruminants. The genus currently consists of one species, Giraffa camelopardalis, the type species. Seven other species are extinct, prehistoric species known from fossils. Taxonomic classifications of one to eight extant giraffe species have been described, based upon research into the mitochondrial and nuclear DNA, as well as morphological measurements of Giraffa, but the IUCN currently recognizes only one species with nine subspecies.

Image(https://img.purch.com/w/192/aHR0cDovL3d3dy5saXZlc2NpZW5jZS5jb20vaW1hZ2VzL2kvMDAwLzA2OC8wOTQvaTMwMC9naXJhZmZlLmpwZz8xNDA1MDA4NDQy)
Image(https://upload.wikimedia.org/wikipedia/commons/9/9f/Giraffe_standing.jpg)

"""

my_pres = pres.Presentation(markdown_string)
pres_url_2 = py.presentation_ops.upload(my_pres, filename)
```

https://plot.ly/~AdamKulidjian/3702/pres-with-images/

```python
import IPython

iframe_2 = url_to_iframe(pres_url_2, True)
IPython.display.HTML(iframe_2)
```

#### Image Stretch
If you want to ensure that your image maintains its original width:height ratio, include the parameter `imgStretch=False` in your `pres.Presentation()` function call.

```python
import plotly.plotly as py
import plotly.presentation_objs as pres

filename = 'pres-with-no-imgstretch'
markdown_string = """
# images in native aspect ratio

Image(https://raw.githubusercontent.com/jackparmer/gradient-backgrounds/master/moods1.png)
Image(https://raw.githubusercontent.com/jackparmer/gradient-backgrounds/master/moods1.png)
Image(https://raw.githubusercontent.com/jackparmer/gradient-backgrounds/master/moods1.png)
Image(https://raw.githubusercontent.com/jackparmer/gradient-backgrounds/master/moods1.png)
Image(https://raw.githubusercontent.com/jackparmer/gradient-backgrounds/master/moods1.png)
"""

my_pres = pres.Presentation(markdown_string, imgStretch=False)
pres_url_3 = py.presentation_ops.upload(my_pres, filename)
```

https://plot.ly/~AdamKulidjian/3703/pres-with-no-imgstretch/

```python
import IPython

iframe_3 = url_to_iframe(pres_url_3, False)
IPython.display.HTML(iframe_3)
```

<!-- #region -->
#### Insert Code Blocks
The Presentations API also supports the insertion of blocks of code with various available langauges to choose from.

To instantiate a "code environment" in your string, place a \`\`\` at the beginning of a line, followed by the name of the programming language you want your code block to be styled in. Then the next lines will be considered "code lines ". To close the "code environment" put another \`\`\` at the end of the line For example:

```
```python
# code goes here
``` ```

The valid languages to choose from are: arecpp, cs, css, fsharp, go, haskell, java, javascript, jsx, julia, xml, matlab, php, python, r, ruby, scala, sql and yaml.
<!-- #endregion -->

```python
import plotly.plotly as py
import plotly.presentation_objs as pres

filename = 'pres-with-code'
markdown_string = """
# Getting Started Using Code
A beginner's introduction to computer science.

---
# Python Functions
Functions are one of the most useful tools in Python. Intuitively, you select an input and get an output.

In order to set up a function use the key word "def" then the name of the function with open parentheses afterwards. Inside the parentheses, write variable names your function will use. These variables can then go into the body of your function and when you give a value to the variable in the call signature, it will pass through the guts of the function until it returns a value.

```python
def somePrintFunction():

    print("boo")

somePrintFunction()




>>>print(new_z)
10

def someAddFunction(a, b):

    print(a+b)




>>>someAddFunction(12,451)
463
```
---
# Use scala
You can write functions in other languages as well. For example, check out this scala code and notice how the print functions look different:

We write 'println()' as opposed to 'print()' as we do in Python.

```scala
/** Basic command line parsing. */
object Main {
  var verbose = false

  def main(args: Array[String]) {
    for (a <- args) a match {
      case "-h" | "-help"    =>
        println("Usage: scala Main [-help|-verbose]")
      case "-v" | "-verbose" =>
        verbose = true
      case x =>
        println("Unknown option: '" + x + "'")
    }
    if (verbose)
      println("How are you today?")
  }
}
```
---
# Under the Hood

There are many things to find when you look under the Plotly Hood. Of many things, one expected thing is the compliance and adherance to alphebetized and PEP-8'ed imports at the top of any module.

This is what the PEP-8 guide has more to say about Imports:

Wildcard imports (from <module> import *) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn't known in advance).

Image(https://help.plot.ly/images/dashboard-carousel.jpg)

```python
from __future__ import absolute_import

import copy
import json
import os
import time
import warnings
import webbrowser

import six
import six.moves
from requests.compat import json as _json

from plotly import exceptions, files, session, tools, utils
from plotly.api import v1, v2
from plotly.plotly import chunked_requests
from plotly.grid_objs import Grid, Column
from plotly.dashboard_objs import dashboard_objs as dashboard
```
"""

my_pres = pres.Presentation(markdown_string)
pres_url_4 = py.presentation_ops.upload(my_pres, filename)
```

https://plot.ly/~AdamKulidjian/3704/pres-with-code/

```python
import IPython

iframe_4 = url_to_iframe(pres_url_4, True)
IPython.display.HTML(iframe_4)
```

#### Style Your Presentation
The Presentations API currently has two styles to choose from: [_Martik_](https://www.pinterest.ca/pin/822540319412564330/) and [_Moods_](https://www.pinterest.ca/pin/822540319412564320/). These themes are inspired by  already existing PowerPoint Templates. Let's use the same `markdown_string` in the previous example but this time try the `Martik` style.

```python
import plotly.plotly as py
import plotly.presentation_objs as pres

filename = 'martik-style'
markdown_string = """
# Getting Started Using Code
A beginner's introduction to computer science.

---
# Python Functions
Functions are one of the most useful tools in Python. Intuitively, you select an input and get an output.

In order to set up a function use the key word "def" then the name of the function with open parentheses afterwards. Inside the parentheses, write variable names your function will use. These variables can then go into the body of your function and when you give a value to the variable in the call signature, it will pass through the guts of the function until it returns a value.

```python
def somePrintFunction():

    print("boo")

somePrintFunction()




>>>print(new_z)
10

def someAddFunction(a, b):

    print(a+b)




>>>someAddFunction(12,451)
463
```
---
# Use scala
You can write functions in other languages as well. For example, check out this scala code and notice how the print functions look different:

We write 'println()' as opposed to 'print()' as we do in Python.

```scala
/** Basic command line parsing. */
object Main {
  var verbose = false

  def main(args: Array[String]) {
    for (a <- args) a match {
      case "-h" | "-help"    =>
        println("Usage: scala Main [-help|-verbose]")
      case "-v" | "-verbose" =>
        verbose = true
      case x =>
        println("Unknown option: '" + x + "'")
    }
    if (verbose)
      println("How are you today?")
  }
}
```
---
# Under the Hood

There are many things to find when you look under the Plotly Hood. Of many things, one expected thing is the compliance and adherance to alphebetized and PEP-8'ed imports at the top of any module.

This is what the PEP-8 guide has more to say about Imports:

Wildcard imports (from <module> import *) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn't known in advance).

Image(https://help.plot.ly/images/dashboard-carousel.jpg)

```python
from __future__ import absolute_import

import copy
import json
import os
import time
import warnings
import webbrowser

import six
import six.moves
from requests.compat import json as _json

from plotly import exceptions, files, session, tools, utils
from plotly.api import v1, v2
from plotly.plotly import chunked_requests
from plotly.grid_objs import Grid, Column
from plotly.dashboard_objs import dashboard_objs as dashboard
```
"""

my_pres = pres.Presentation(markdown_string, style='martik')
pres_url_5 = py.presentation_ops.upload(my_pres, 'martik-style')
```

```python
import IPython

iframe_5 = url_to_iframe(pres_url_5, True)
IPython.display.HTML(iframe_5)
```

<!-- #region -->
#### Transitions
You can specify how your want your slides to transition to one another. Just like in the Plotly Presentation Application, there are 4 types of transitions: `slide`, `zoom`, `fade` and `spin`.

To apply any combination of these transition to a slide, just insert transitions at the top of the slide as follows:

`transition: slide, zoom`

Make sure that this line comes before any heading that you define in the slide, i.e. like this:

```
transition: slide, zoom
# slide title
```
<!-- #endregion -->

```python
import plotly.plotly as py
import plotly.presentation_objs as pres

filename = 'pres-with-transitions'
markdown_string = """
transition: slide
# slide
---
transition: zoom
# zoom
---
transition: fade
# fade
---
transition: spin
# spin
---
transition: spin and slide
# spin, slide
---
transition: fade zoom
# fade, zoom
---
transition: slide, zoom, fade, spin, spin, spin, zoom, fade
# slide, zoom, fade, spin

"""

my_pres = pres.Presentation(markdown_string, style='moods')
pres_url_6 = py.presentation_ops.upload(my_pres, filename)
```

```python
import IPython

iframe_6 = url_to_iframe(pres_url_6, True)
IPython.display.HTML(iframe_6)
```

#### Add Thin Border Around Text Boxes
Every `slide` has `children`, and each of these `children` have a `style` attribute. This `style` property is derived from the CSS element of the same name. Since you have the power of CSS to work with, you could customize text borders in your presentation if you want.

```python
import plotly.plotly as py
import plotly.presentation_objs as pres

filename = 'pres-with-custom-css'
markdown_string = """
# custom css
---
transition: zoom, slide, spin, fade
# fun with css

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
```python
x = 4

if x < 2:
    x = 2 * x
    if x >= 2:
        break
```

"""

my_pres = pres.Presentation(markdown_string)

# change text border style
my_pres['presentation']['slides'][1]['children'][0]['props']['style']['border'] = 'solid red'

pres_url_7 = py.presentation_ops.upload(my_pres, filename)
```

https://plot.ly/~AdamKulidjian/3709/pres-with-custom-css/

```python
import IPython

iframe_7 = url_to_iframe(pres_url_7, True)
IPython.display.HTML(iframe_7)
```

#### Reference

```python
help(py.presentation_ops)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'presentations-api.ipynb', 'python/presentations-tool/', 'Presentations Tool | plotly',
    'How to create and publish a spectacle-presentation with the Python API.',
    title = 'Presentations Tool | plotly',
    name = 'Presentations Tool',
    thumbnail='thumbnail/pres_api.jpg', language='python',
    has_thumbnail='true', display_as='file_settings', order=0.6)
```

```python

```