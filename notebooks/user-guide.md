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
    description: Plotly User Guide for Python
    has_thumbnail: false
    language: python
    layout: user-guide
    name: Plotly User Guide
    page_type: u-guide
    permalink: python/user-guide/
    thumbnail: null
    title: Plotly User Guide for Python
---

# Python API User Guide


So you've just finished the [`Getting Started document`](https://plot.ly/python/getting-started) and now you're looking to find out more. In this guide, we'll go through some of the internals of Plotly, as well as some tips and general practices that will allow you generate amazing data visualizations in no time.


### What is Plotly?:

Plotly at its core is a data visualization toolbox. Under every plotly graph is a JSON object, which is a dictionary like data structure. Simply by changing the values of some keywords in this object, we can get vastly different and ever more detailed plots. For example:

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(x=[1,2,3], y=[4,5,6], marker={'color': 'red', 'symbol': 104, 'size': 10}, 
                    mode="markers+lines",  text=["one","two","three"], name='1st Trace')
                                               
data=go.Data([trace1])
layout=go.Layout(title="First Plot", xaxis={'title':'x1'}, yaxis={'title':'x2'})
figure=go.Figure(data=data,layout=layout)
py.iplot(figure, filename='pyguide_1')
```

```python
figure
```

We can see that the figure that we're plotting with `py.iplot` is actually just a dictionary-like object. Moreover, we can customize and alter this plot simply by adding/defining the values of the **[possible keywords](https://plot.ly/python/reference/#scatter)** associated with scatter plots.

Let's say we want to change the title of our scatter plot to `Plot update`, while at the same time, make the scatter plot blue instead of red.

```python
figure.update(dict(layout=dict(title='Plot update'), data=dict(marker=dict(color='blue'))))
py.iplot(figure, filename='pyguide_2')
```

Moreover, Plotly plots are interactive, meaning you can manually explore the data by panning, selecting, zooming on the graphing surface (among other possible actions, try panning the axes!). We are also continually expanding the expressiveness of the Plotly package so we're able to graph and visualize all sorts of data. 


In no time you will be able to figure out how to make plots the way you want them, and with the information that you want to be shared with those you want. For example we can take a quick look at how we would define the objects required to generate a scatterplot comparing life expectancies and GDP Per Capita between two different continents. 

```python
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('https://raw.githubusercontent.com/yankev/test/master/life-expectancy-per-GDP-2007.csv')

americas = df[(df.continent=='Americas')]
europe = df[(df.continent=='Europe')]

trace_comp0 = go.Scatter(
    x=americas.gdp_percap,
    y=americas.life_exp,
    mode='markers',
    marker=dict(size=12,
                line=dict(width=1),
                color="navy"
               ),
    name='Americas',
    text=americas.country,
    )

trace_comp1 = go.Scatter(
    x=europe.gdp_percap,
    y=europe.life_exp,
    mode='markers',
    marker=dict(size=12,
                line=dict(width=1),
                color="red"
               ),
    name='Europe',
    text=europe.country,
        )

data_comp = [trace_comp0, trace_comp1]
layout_comp = go.Layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    hovermode='closest',
    xaxis=dict(
        title='GDP per capita (2000 dollars)',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Life Expectancy (years)',
        ticklen=5,
        gridwidth=2,
    ),
)
fig_comp = go.Figure(data=data_comp, layout=layout_comp)
py.iplot(fig_comp, filename='life-expectancy-per-GDP-2007')
```

Hopefully this gives you an idea how plots are created with the Plotly Python Library. We'll go into more detail regarding the different parts that make up the plot in later sections. But for now, I hope you can see the customizability that's possible, and how we can define these graphs programmatically. 


#### The Source of Plotly's Power

All the graphs and plots which Plotly generates are actually the product of our javascript library [`plotly.js`](https://plot.ly/javascript). Whether you see Plotly graphs in a browser, or an IPython notebook, all the visualizations and interactiveness is made possible by [`plotly.js`](https://plot.ly/javascript). Built on top of `d3.js` and `stack.gl`, [`plotly.js`](https://plot.ly/javascript) is a high-level, declarative charting library. [`plotly.js`](https://plot.ly/javascript) ships with 20 chart types, including 3D charts, statistical graphs, and SVG maps. 


### Working with the Python API


The Python API is a package designed to interact with the `Plotly.js` library in order to allow Python users to create plots in their preferred environment. This way, the package will provide functions and graph objects that will simplify the process of generating plots, which would amount to properly defining keywords in a JSON object (as seen above). To this end, the Python API provides functions and graph objects which will allow us to create our plots functionally. So let's break this down.

```python
import plotly.plotly as py
import plotly.graph_objs as go
```

These are the two main modules that we will need in order to generate our Plotly graphs. 

- `plotly.plotly` contains the functions that will help us communicate with the Plotly servers
- `plotly.graph_objs` contains the functions that will generate graph objects for us.

**Note:** If we examine the code from the example in the previous section, we can see these parts in action.


Below we will examine the different aspects/objects that define a plot in Plotly. These are:
- Data
- Layout
- Figure


#### Data

```python
data
```

We see that data is actually a list object in Python. Data will actually contain all the traces that you wish to plot. Now the question may be, what is a trace? A trace is just the name we give a collection of data and the specifications of which we want that data plotted. Notice that a trace will also be an object itself, and these will be named according to how you want the data displayed on the plotting surface.
Hence,

```python
go.Scatter(x=[1,2,3], y=[4,5,6], marker={'color': 'red', 'symbol': 104, 'size': "10"}, 
                                               mode="markers+lines",  text=["one","two","three"])
```

defines a trace producing a scatter plot. Moreover it defines the data that we want plotted, which are 3 data points (1,4), (2,5), (3,6), as well as a miriad of specifications related to plotting this data. In this example we wanted the points to be plotted as hollow x's with lines joining them, all in red.

In addition, we can add another Scatter object to our data list. We can do this by defining a new Scatter object, and including this in our definition of our data object.



```python
#First let's make up some cool data to plot:
import numpy as np
x = np.arange(1,3.2,0.2)
y = 6*np.sin(x)
y
```

```python
trace2 = go.Scatter(x=x, y=y, marker={'color': 'blue', 'symbol': 'star', 'size': 10}, mode='markers', name='2nd trace')
data = go.Data([trace1, trace2])
data
```

```python
plot2 = py.iplot(go.Figure(data=data, layout=layout), filename='pyguide_3')
plot2
```

#### Layout


The Layout object will define the look of the plot, and plot features which are unrelated to the data. So we will be able to change things like the title, axis titles, spacing, font and even draw shapes on top of your plot! In our case,

```python
layout=go.Layout(title="First Plot", xaxis={'title':'x1'}, yaxis={'title':'x2'})
layout
```

##### Annotations


We added a plot title as well as titles for all the axes. 
For fun we could add some text annotation as well in order to indicate the maximum point that's been plotted on the current plotting surface.

```python
layout.update(dict(annotations=[go.Annotation(text="Highest Point", x=3, y=6)]))
py.iplot(go.Figure(data=data, layout=layout), filename='pyguide_4')
```

##### Shapes

Let's add a rectangular block to highlight the section where trace 1 is above trace2.

```python
layout.update(dict(shapes = [
        # 1st highlight during Feb 4 - Feb 6
        {
            'type': 'rect',
            # x-reference is assigned to the x-values
            'xref': 'x',
            # y-reference is assigned to the plot paper [0,1]
            'yref': 'y',
            'x0': '1',
            'y0': 0,
            'x1': '2',
            'y1': 7,
            'fillcolor': '#d3d3d3',
            'opacity': 0.2,
            'line': {
                'width': 0,
            }
        }]
        ))

py.iplot(go.Figure(data=data, layout=layout), filename='pyguide_5')
```

Of course, all this can be found in the `Layout` section of the [Reference Page](https://www.plot.ly/python/referece).


#### Figure


Finally, we get to the figure object. `go.Figure` just creates the final object to be plotted, and simply just creates a dictionary-like object that contains both the data object and the layout object.

```python
go.Figure(data=data, layout=layout)
```

#### Why `graph_objs`?


After viewing the outputs of these functions (ie: the objects), we can see that they are just lists or dictionaries. But they're a little more than that. Though they do inherit properties from dictionaries (traces, and layout) and lists (figure), they provide a bit more functionality as we'll soon see. Not to mention the fact that it's much simpler to create plots in this functional fashion compared to manually writing up a dictionary. 


The first neat option about using graph_objs is that you can call help on them.

```python
help(go.Figure)
```



```python
help(go.Scatter)
```

As you can see, calling help shows us all the attributes that the Scatter object takes as paremeters. Also because the scatter object is based off of a dictionary, you can see all the different methods that are attached to this object as well. For example, we've seen the use of the `update` method above.


Focussing more on the parameters, we can see that the objects have key-word/name validation. What this means is that it'll raise an exception that provides us some detail of where we went wrong.

```python
go.Scatter(markers=dict(color='blue'))
```

As you can see, it tells us that `markers` is not a key in `scatter`. Instead as we browse the list, we see that what we wanted was actually `marker` (singular, without the s), which is a keyword. Thus this little feature makes for much easier debugging and correction.



Now let's talk about the methods that come along with these objects. The one of most importance would be the `update` method. The difference here between the regular update method for dictionaries is that it allows for `nested updates`. 
Let me show you what that means.

```python
#Here we have a scatter object:
scatter_trace = go.Scatter(marker=dict(color='blue'))
```

```python
#We can add some information to it like data (x, and y), as well as update the sybmol we want the markers to be
scatter_trace.update(dict(x=[1,2,3],y=[4,5,6], marker=dict(symbol='star')))
scatter_trace
```

```python
figure = go.Figure(data=[scatter_trace], layout=layout)
py.iplot(figure, filename='pyguide_5')
```

Notice that we were able to add the data as well as add the extra feature for the markers. However if we let `scatter_trace` be just a standard dictionary then we will not be able to just add another feature for the marker in this way. Instead, the value for marker will be replaced with the dictionary we choose to update with.

```python
scatter_trace = {'marker': {'color': 'blue'},
                 'type': 'scatter',
                 ''}
```

### Looking at Examples


Examples are one of the best ways to get started and get your feet wet. Through the examples you can get a good idea of what a certain type of plot is used for, and what can be possible with it. 

Moreover, the code in the examples are self-contained, meaning you can just copy and paste the code block and run it in your Python script or Ipython Notebook. But if you happen to run into an issue running the example, please let us know at our [Community Forums](http://community.plot.ly). By examining the code, you can further understand and experience the procedure in which Plotly plots are created. Something important to look at would be the data used in these examples; Because certain plots are only able to handle certain types of data (e.g: histograms are only useful for quantitative data), you will get an idea of the limitations and purpose of different plot types. In addition, you can see the effect certain parameters have on the data visualization and hopefully give you a sense of what's possible beyond the standard/default.

It's a good place to look for what's possible in Plotly. A brief look at the page you can find sections and examples on types of plots you didn't know existed, or layout options that you had no idea were possible and within reach. Just take a look at all these guys:

[![Scientific Charts](https://cloud.githubusercontent.com/assets/12302455/14262495/cd45bc98-fa83-11e5-9d4b-7a49acd37252.png)](https://plot.ly/python)



What's more you can find layout options that will allow you to create plots with multiple axes and plots.
Check this out:
[![Layout Options](https://cloud.githubusercontent.com/assets/12302455/14262589/51792702-fa84-11e5-8e3a-b606a0211838.png)](https://plot.ly/python/#layout-options)




As an example, say we looked at two different types of plots in the `heatmap` and the `box plots`, now equipped with the knowledge of subplots, we can easily two and two together in order to put both these on the same plotting surface (for no other reason than that we can). Let's first load the packages, and then set up the data for our heatmap trace.

```python
from plotly import tools
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

heatmap = go.Heatmap(
        z=[[1, 20, 30],
           [20, 1, 60],
           [30, 60, 1]],
        showscale=False
        )

```

Next we'll set up the trace object for our wind rose chart, and note I'm just copying code from the example pages for each of these plot types.

```python
y0 = np.random.randn(50)
y1 = np.random.randn(50)+1

box_1 = go.Box(
    y=y0
)
box_2 = go.Box(
    y=y1
)
data = [heatmap, box_1, box_2]

```

```python
fig = tools.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2}, None]],
                          subplot_titles=('First Subplot','Second Subplot', 'Third Subplot'))

fig.append_trace(box_1, 1, 1)
fig.append_trace(box_2, 1, 2)
fig.append_trace(heatmap, 2, 1)

fig['layout'].update(height=600, width=600, title='i <3 subplots')

py.iplot(fig, filename='box_heatmap1')

```

This looks great, however we'd like for our subplots to be on the same plotting surface. So let's take a look at the dictionary representation of our figure, and customize it using what we've learned before. 

```python
fig
```

We actually see that the second boxplot has its own xaxis and yaxis. Thus we should unify it with the same axis as the first subplot. Then from the layout section, we should remove the additional xaxis and yaxis that are drawn for us. You can perform these steps seperately to see what I mean, but in this guide, I'll just show you the result of this edit/customization.

```python
fig.data[1].yaxis = 'y1'
fig.data[1].xaxis = 'x1'
del fig.layout['xaxis2']
del fig.layout['yaxis2']

```

Now we still have to remove the annotation for the `Second Subplot` title, asell as the `First Subplot` title, and then extend the range of xaxis1 to the entire plotting surface.

```python
del fig.layout.annotations[0]   #deletes annotation for `First Subplot`
del fig.layout.annotations[0]   #deletes annotation for `Second Subplot` because of shift
fig.layout.xaxis1.domain = [0.0, 1]
```

And voila! We just put together some examples that we've never seen before, and customized out plot using what we learned throughout the guide!

```python
py.iplot(fig, filename='box-heatmap-fixed')
```

### Using the Reference Page


At this point you may have a good idea of how you want to visualize your data, and which type of plot you would like to use. You've taken a look at some examples of this plot type, but there are still some details that you would like to add or change. Now is the time for you to check out the **[Reference Page!](https://plot.ly/python/reference/)** The reference page details all the parameters that can be set for every type of plot that is possible in Plotly (ie: all the trace objects). In addition it also provides details on the possible parameters that are available to change in the `Layout` object as well.

![something](https://cloud.githubusercontent.com/assets/12302455/14263600/681e8c54-fa89-11e5-8467-99e78e4f9135.png)

When you first load the page you will see a menu on the left which is segregated into `Plot Objects` and `Layout`. This exemplifies the two components of every Plotly figure. So for example if you knew you wanted to change something related to the visualization of the data, then you would look at the first section. If instead you were interested in a general aesthetic feature of the graph then the Layout will probably be your best option.

Now for example, if you decided to create a scatter plot, then you would choose `Scatter` under `Plot Objects`, and that will take you to the the section for `Scatter`. On your immediate right you will be able to see a breakdown of the Scatter section, which includes all the parameters and sub-parameters at your disposal. 



### Issues and Questions


So you've developed a better understanding of Plotly now, and you're starting to create cooler plots and visualizations for different projects you're working on. If you ever happen to get stuck with certain use cases or features in Plotly, you can let us know at our **[Community Forums](http://community.plot.ly)**. 
![Community Support](https://cloud.githubusercontent.com/assets/12302455/14265774/71a43b4a-fa91-11e5-86f8-f069037c74ea.png)
Moreover if you sign up for a Pro Plan, we also offer e-mail and intercom support as well. Finally if you think you've caught a bug or if something just doesn't function the way it should, you can create an issue on our **[GitHub Repo](https://github.com/plotly/plotly.py/issues)**.




```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install publisher --upgrade
import publisher
publisher.publish(
    'new_py_guide.ipynb', 'python/user-guide//', 'Plotly User Guide for Python',
    'Plotly User Guide for Python',
    name = 'Plotly User Guide',
    thumbnail='', language='python',
    layout='user-guide', has_thumbnail='false') 
```

```python

```